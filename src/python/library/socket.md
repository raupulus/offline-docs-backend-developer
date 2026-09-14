---
title: '"socket" --- Low-level networking interface'
source_url: https://docs.python.org/es/3
source_path: library/socket.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3840
---

# "socket" --- Low-level networking interface

**Código fuente:** Lib/socket.py

======================================================================

Este módulo proporciona acceso a la interfaz BSD *socket*. Está
disponible en todos los sistemas Unix modernos, Windows, MacOS y
probablemente plataformas adicionales.

Nota:

  Algunos comportamientos pueden depender de la plataforma, ya que las
  llamadas se realizan a las API de socket del sistema operativo.

Availability: not WASI.

This module does not work or is not available on WebAssembly. See
Plataformas WebAssembly for more information.

The Python interface is a straightforward transliteration of the Unix
system call and library interface for sockets to Python's object-
oriented style: the "socket()" function returns a *socket object*
whose methods implement the various socket system calls.  Parameter
types are somewhat higher-level than in the C interface: as with
"read()" and "write()" operations on Python files, buffer allocation
on receive operations is automatic, and buffer length is implicit on
send operations.

Ver también:

  Módulo "socketserver"
     Clases que simplifican la escritura de servidores de red.

  Módulo "ssl"
     Un contenedor TLS/SSL para objetos de socket.

## Familias Socket

Dependiendo del sistema y de las opciones de compilación, este módulo
admite varias familias de sockets.

El formato de dirección requerido por un objeto de socket determinado
se selecciona automáticamente en función de la familia de direcciones
especificada cuando se creó el objeto de socket.  Las direcciones de
socket se representan de la siguiente manera:

* La dirección de un socket "AF_UNIX" enlazado a un nodo del sistema
  de archivos es representado como una cadena de caracteres,
  utilizando la codificación del sistema de archivos y el controlador
  de errores "'surrogateescape'" (Observar **PEP 383**). Una dirección
  en el espacio de nombre abstracto de Linux es devuelvo como un
  *bytes-like object* con un byte inicial nulo; tenga en cuenta que
  los sockets en este nombre de espacio puede comunicarse con sockets
  normales del sistema de archivos, así que los programas destinados a
  correr en Linux podrían necesitar tratar con ambos tipos de
  direcciones. Se puede pasar un objeto similar a una cadena de
  caracteres o bytes para cualquier tipo de dirección al pasarlo como
  argumento.

  Distinto en la versión 3.3: Anteriormente, se suponía que las rutas
  de socket "AF_UNIX" utilizaban codificación UTF-8.

  Distinto en la versión 3.5: Ahora se acepta la grabación *bytes-like
  object*.

* Se utiliza un par "(host, port)" para la familia de direcciones
  "AF_INET", donde *host* es una cadena que representa un nombre de
  host en notación de dominio de Internet como "'daring.cwi.nl'" o una
  dirección IPv4 como "'100.50.200.5'", y *port* es un número entero.

  * Para direcciones IPv4, se aceptan dos formas especiales en lugar
    de una dirección de host: "’’" representa "INADDR_ANY", que se
    utiliza para enlazar a todas las interfaces, y la cadena de
    caracteres "'<broadcast>'" representa "INADDR_BROADCAST". Este
    comportamiento no es compatible con IPv6, por lo tanto, es posible
    que desee evitarlos sí tiene la intención de admitir IPv6 con sus
    programas Python.

* For "AF_INET6" address family, a four-tuple "(host, port, flowinfo,
  scope_id)" is used, where *flowinfo* and *scope_id* represent the
  "sin6_flowinfo" and "sin6_scope_id" members in "struct sockaddr_in6"
  in C.  For "socket" module methods, *flowinfo* and *scope_id* can be
  omitted just for backward compatibility.  Note, however, omission of
  *scope_id* can cause problems in manipulating scoped IPv6 addresses.

  Distinto en la versión 3.7: Para direcciones de multidifusión (con
  *scopeid* significativo) *address* puede no contener la parte
  "%scope" (o "zone id"). Esta información es superflua y puede
  omitirse de forma segura (recomendado).

* "AF_NETLINK" sockets se representan como pares "(pid, groups)".

* La compatibilidad con LINUX solo para TIPC está disponible mediante
  la familia de direcciones "AF_TIPC".  TIPC es un protocolo en red
  abierto y no basado en IP diseñado para su uso en entornos
  informáticos agrupados.  Las direcciones se representan mediante una
  tupla y los campos dependen del tipo de dirección. El formulario de
  tupla general es "(addr_type, v1, v2, v3 [, scope])", donde:

  * *addr_type* es uno de "TIPC_ADDR_NAMESEQ", "TIPC_ADDR_NAME", o
    "TIPC_ADDR_ID".

  * *scope* es una de "TIPC_ZONE_SCOPE", "TIPC_CLUSTER_SCOPE", y
    "TIPC_NODE_SCOPE".

  * Si *addr_type* es "TIPC_ADDR_NAME", entonces *v1* es el tipo de
    servidor, *v2* es el identificador de puerto, y *v3* debe ser 0.

    Si *addr_type* es "TIPC_ADDR_NAMESEQ", entonces  *v1* es el tipo
    de servidor, *v2* es el numero de puerto inferior, y *v3* es el
    numero de puerto superior.

    Si *addr_type* es "TIPC_ADDR_ID", *v1* es el nodo, *v2* es la
    referencia y *v3* debe establecerse en 0.

* Una tupla "(interface, )" es usada para la dirección de familia
  "AF_CAN", donde *interface* es una cadena de caracteres
  representando a un nombre de interfaz de red como "’can0’". La
  interfaz de red llamada "''" puede ser usada para recibir paquetes
  de todas las interfaces de red de esta familia.

  * "CAN_ISOTP" protocol requires a tuple "(interface, rx_addr,
    tx_addr)" where both additional parameters are unsigned long
    integer that represent a CAN identifier (standard or extended).

  * "CAN_J1939" protocol requires a tuple "(interface, name, pgn,
    addr)" where additional parameters are 64-bit unsigned integer
    representing the ECU name, a 32-bit unsigned integer representing
    the Parameter Group Number (PGN), and an 8-bit integer
    representing the address.

* Se utiliza una cadena o una tupla "(id, unit)" para el protocolo
  "SYSPROTO_CONTROL" de la familia "PF_SYSTEM". La cadena es el nombre
  de un control de kernel mediante un ID asignado dinámicamente. La
  tupla se puede utilizar si se conoce el ID y el número de unidad del
  control del kernel o si se utiliza un ID registrado.

  Added in version 3.3.

* "AF_BLUETOOTH" admite los siguientes protocolos y formatos de
  dirección:

  * "BTPROTO_L2CAP" accepts a tuple "(bdaddr, psm[, cid[,
    bdaddr_type]])" where:

    * "bdaddr" is a string specifying the Bluetooth address.

    * "psm" is an integer specifying the Protocol/Service Multiplexer.

    * "cid" is an optional integer specifying the Channel Identifier.
      If not given, defaults to zero.

    * "bdaddr_type" is an optional integer specifying the address
      type; one of "BDADDR_BREDR" (default), "BDADDR_LE_PUBLIC",
      "BDADDR_LE_RANDOM".

    Distinto en la versión 3.14: Added "cid" and "bdaddr_type" fields.

  * "BTPROTO_RFCOMM" acepta "(bdaddr, channel)" donde "bdaddr" es la
    dirección Bluetooth como una cadena de caracteres y "channel" es
    un entero.

  * "BTPROTO_HCI" accepts a format that depends on your OS.

    * On Linux it accepts an integer "device_id" or a tuple
      "(device_id, [channel])" where "device_id" specifies the number
      of the Bluetooth device, and "channel" is an optional integer
      specifying the HCI channel ("HCI_CHANNEL_RAW" by default).

    * On FreeBSD, NetBSD and DragonFly BSD it accepts "bdaddr" where
      "bdaddr" is the Bluetooth address as a string.

    Distinto en la versión 3.2: Se ha añadido compatibilidad con
    NetBSD y DragonFlyBSD.

    Distinto en la versión 3.13.3: FreeBSD support added.

    Distinto en la versión 3.14: Added "channel" field. "device_id"
    not packed in a tuple is now accepted.

  * "BTPROTO_SCO" accepts "bdaddr" where "bdaddr" is the Bluetooth
    address as a string or a "bytes" object. (ex.
    "'12:23:34:45:56:67'" or "b'12:23:34:45:56:67'")

    Distinto en la versión 3.14: FreeBSD support added.

* "AF_ALG" es una interfaz basada en socket solo Linux para la
  criptografía del núcleo. Un socket de algoritmo se configura con una
  tupla de dos a cuatro elementos "(type, name [, feat [, mask]])",
  donde:

  * *type* es el tipo de algoritmos como cadenas de caracteres, e.g.
    "aead", "hash", "skcipher" o "rng".

  * *name* es el nombre del algoritmo y el modo de operación como
    cadena de caracteres, e.g. "sha256", "hmac(sha256)", "cbc(aes)" o
    "drbg_nopr_ctr_aes256".

  * *feat* y *mask* son enteros de 32 bits sin signo.

  Availability: Linux >= 2.6.38.

  Algunos tipos de algoritmos requieren Kernels mas recientes.

  Added in version 3.6.

* "AF_VSOCK" permite comunicación entre maquinas virtuales y sus
  hosts. Los sockets están representando como una tupla "(CID, port)"
  donde el contexto del ID o CID y el puerto son enteros.

  Availability: Linux >= 3.9

  Véase *vsock(7)*

  Added in version 3.7.

* "AF_PACKET" is a low-level interface directly to network devices.
  The addresses are represented by the tuple "(ifname, proto[,
  pkttype[, hatype[, addr]]])" where:

  * *ifname* - Cadena que especifica el nombre del dispositivo.

  * *proto* - The Ethernet protocol number. May be "ETH_P_ALL" to
    capture all protocols, one of the ETHERTYPE_* constants or any
    other Ethernet protocol number.

  * *pkttype* - Entero opcional especificando el tipo de paquete:

    * "PACKET_HOST" (por defecto) - Paquetes diseccionado al local
      host.

    * "PACKET_BROADCAST" - Paquete de transmisión de la capa física.

    * "PACKET_MULTICAST" - Paquete enviado a una dirección de
      multidifusión de capa física.

    * "PACKET_OTHERHOST" - Paquete a otro host que haya sido capturado
      por un controlador de dispositivo en modo promiscuo.

    * "PACKET_OUTGOING" - Paquete originalmente desde el local host
      que se enlaza de nuevo a un conector de paquetes.

  * *hatype* - Entero opcional que especifica el tipo de dirección de
    hardware ARP.

  * *addr* - Objeto opcional en forma de bytes que especifica la
    dirección física del hardware, cuya interpretación depende del
    dispositivo.

  Availability: Linux >= 2.2.

* "AF_QIPCRTR" es una interfaz basada en sockets solo para Linux para
  comunicarse con servicios que se ejecutan en co-procesadores en
  plataformas Qualcomm. La familia de direcciones se representa como
  una tupla "(node, port)" donde el *node* y *port* son enteros no
  negativos.

  Availability: Linux >= 4.7.

  Added in version 3.8.

* "IPPROTO_UDPLITE" es una variante de UDO que te permite especificar
  que porción del paquete es cubierta con la suma de comprobación.
  Esto agrega dos opciones al socket que pueden cambiar.
  "self.setsockopt(IPPROTO_UDPLITE, UDPLITE_SEND_CSCOV, length)"
  cambiara que parte de los paquetes salientes están cubierta por la
  suma de comprobación y "self.setsockopt(IPPROTO_UDPLITE,
  UDPLITE_RECV_CSCOV, length)" filtrara los paquetes que permitirá
  cubrir una pequeña parte de tu datos. En ambos casos "length" deben
  estar en "range(8, 2**16, 8)".

  Tal socket debe construirse como "socket(AF_INET, SOCK_DGRAM,
  IPPROTO_UDPLITE)" para IPV4 o "socket(AF_INET6, SOCK_DGRAM,
  IPPROTO_UDPLITE)" para IPV6.

  Availability: Linux >= 2.6.20, FreeBSD >= 10.1

  Added in version 3.9.

* "AF_HYPERV" es una interfaz basada en sockets exclusiva de Windows
  para comunicarse con hosts e invitados de Hyper-V. La familia de
  direcciones se representa como una tupla "(vm_id, service_id)" donde
  "vm_id" y "service_id" son cadenas UUID.

  El "vm_id" es el identificador de la máquina virtual o un conjunto
  de VMID conocidos valores si el objetivo no es una máquina virtual
  específica. Constantes VMID conocidas definidos en "socket" son:

  * "HV_GUID_ZERO"

  * "HV_GUID_BROADCAST"

  * "HV_GUID_WILDCARD" - Se utiliza para vincularse a sí mismo y
    aceptar conexiones de todas las particiones.

  * "HV_GUID_CHILDREN" - Se utiliza para vincularse a sí mismo y
    aceptar conexiones desde particiones secundarias.

  * "HV_GUID_LOOPBACK" - Se utiliza como objetivo para sí mismo.

  * "HV_GUID_PARENT" - Cuando se usa como enlace, acepta la conexión
    del padre partición. Cuando se utiliza como dirección de destino,
    se conectará al padre dividir.

  El "service_id" es el identificador del servicio registrado.

  Added in version 3.12.

Si utiliza un nombre de host en la parte *host* de la dirección de
socket IPv4/v6, el programa puede mostrar un comportamiento no
determinista, ya que Python utiliza la primera dirección devuelta por
la resolución DNS.  La dirección del socket se resolverá de manera
diferente en una dirección IPv4/v6 real, dependiendo de los resultados
de la resolución DNS y/o la configuración del host.  Para un
comportamiento determinista, utilice una dirección numérica en la
parte *host*.

Todos los errores generan excepciones. Las excepciones normales para
tipos de argumentos inválidos y condiciones de falta de memoria pueden
ser lanzadas. Los errores relacionados con la semántica de los sockets
o de las direcciones lanzan "OSError" o una de sus subclases.

El modo de no bloqueo es compatible a través de "setblocking()".  Se
admite una generalización de esto basada en los tiempos de espera a
través de "settimeout()".

## Contenido del módulo

The module "socket" exports the following elements.

### Excepciones

exception socket.error

   Un alias en desuso de "OSError".

   Distinto en la versión 3.3: Siguiendo **PEP 3151**, es clase fue
   creada como un alias de "OSError".

exception socket.herror

   Una subclase de "OSError", esta excepción se produce para los
   errores relacionados con la dirección, es decir, para las funciones
   que utilizan *h_errno* en la API de POSIX C, incluidas
   "gethostbyname_ex()" y "gethostbyaddr()". El valor adjunto es un
   par "(h_errno, string)" que representa un error devuelto por una
   llamada a la biblioteca.  *h_errno* es un valor numérico, mientras
   que *string* representa la descripción de *h_errno*, devuelta por
   la función "hstrerror()" C.

   Distinto en la versión 3.3: Esta clase fue creada como una subclase
   de "OSError".

exception socket.gaierror

   A subclass of "OSError", this exception is raised for address-
   related errors by "getaddrinfo()" and "getnameinfo()". The
   accompanying value is a pair "(error, string)" representing an
   error returned by a library call.  *string* represents the
   description of *error*, as returned by the "gai_strerror()" C
   function.  The numeric *error* value will match one of the "EAI_*"
   constants defined in this module.

   Distinto en la versión 3.3: Esta clase fue creada como una subclase
   de "OSError".

exception socket.timeout

   Un alias obsoleto de "TimeoutError".

   Una subclase de "OSError", esta excepción se genera cuando ocurre
   un *timeout* en un socket que ha tenido tiempos de espera
   habilitados a través de una llamada previa a "settimeout()" ( o
   implícitamente mediante "setdefaulttimeout()"). El valor del
   acompañamiento es una cadena de caracteres cuyo valor es
   actualmente siempre “tiempo de espera”.

   Distinto en la versión 3.3: Esta clase fue creada como una subclase
   de "OSError".

   Distinto en la versión 3.10: Esta clase se convirtió en un alias de
   "TimeoutError".

### Constantes

Las constantes AF_* y SOCK_* ahora son colecciones: "AddressFamily" y
"SocketKind" "IntEnum".

Added in version 3.4.

socket.AF_UNIX
socket.AF_INET
socket.AF_INET6

   These constants represent the address (and protocol) families, used
   for the first argument to "socket()".  If the "AF_UNIX" constant is
   not defined then this protocol is unsupported.  More constants may
   be available depending on the system.

socket.AF_UNSPEC

   "AF_UNSPEC" means that "getaddrinfo()" should return socket
   addresses for any address family (either IPv4, IPv6, or any other)
   that can be used.

socket.SOCK_STREAM
socket.SOCK_DGRAM
socket.SOCK_RAW
socket.SOCK_RDM
socket.SOCK_SEQPACKET

   These constants represent the socket types, used for the second
   argument to "socket()".  More constants may be available depending
   on the system. (Only "SOCK_STREAM" and "SOCK_DGRAM" appear to be
   generally useful.)

socket.SOCK_CLOEXEC
socket.SOCK_NONBLOCK

   Estas dos constantes, si se definen, se pueden combinar con los
   tipos de socket y le permiten establecer algunas banderas
   atómicamente (evitando así posibles condiciones de carrera y la
   necesidad de llamadas separadas).

   Ver también:

     Secure File Descriptor Handling para una explicación más
     completa.

   Availability: Linux >= 2.6.27.

   Added in version 3.2.

SO_*
socket.SOMAXCONN
MSG_*
SOL_*
SCM_*
IPPROTO_*
IPPORT_*
INADDR_*
IP_*
IPV6_*
EAI_*
AI_*
NI_*
TCP_*

   Many constants of these forms, documented in the Unix documentation
   on sockets and/or the IP protocol, are also defined in the socket
   module. They are generally used in arguments to the "setsockopt()"
   and "getsockopt()" methods of socket objects.  In most cases, only
   those symbols that are defined in the Unix header files are
   defined; for a few symbols, default values are provided.

   Distinto en la versión 3.6: "SO_DOMAIN", "SO_PROTOCOL",
   "SO_PEERSEC", "SO_PASSSEC", "TCP_USER_TIMEOUT", "TCP_CONGESTION"
   han sido agregados.

   Distinto en la versión 3.6.5: Added support for "TCP_FASTOPEN",
   "TCP_KEEPCNT" on Windows platforms when available.

   Distinto en la versión 3.7: "TCP_NOTSENT_LOWAT" ha sido
   agregada.Added support for "TCP_KEEPIDLE", "TCP_KEEPINTVL" on
   Windows platforms when available.

   Distinto en la versión 3.10: Se agregó "IP_RECVTOS". Se agregó
   "TCP_KEEPALIVE". En MacOS, esta constante se puede utilizar de la
   misma forma que "TCP_KEEPIDLE" en Linux.

   Distinto en la versión 3.11: Se agregó "TCP_CONNECTION_INFO". En
   MacOS esta constante se puede utilizar de la misma manera que
   "TCP_INFO" se utiliza en Linux y BSD.

   Distinto en la versión 3.12: Se agregaron "SO_RTABLE" y
   "SO_USER_COOKIE". En OpenBSD y FreeBSD respectivamente, esas
   constantes se pueden usar de la misma manera que "SO_MARK" es usado
   en Linux. También se agregaron opciones de socket TCP faltantes de
   Linux: "TCP_MD5SIG", "TCP_THIN_LINEAR_TIMEOUTS", "TCP_THIN_DUPACK",
   "TCP_REPAIR", "TCP_REPAIR_QUEUE", "TCP_QUEUE_SEQ",
   "TCP_REPAIR_OPTIONS", "TCP_TIMESTAMP", "TCP_CC_INFO",
   "TCP_SAVE_SYN", "TCP_SAVED_SYN", "TCP_REPAIR_WINDOW",
   "TCP_FASTOPEN_CONNECT", "TCP_ULP", "TCP_MD5SIG_EXT",
   "TCP_FASTOPEN_KEY", "TCP_FASTOPEN_NO_COOKIE",
   "TCP_ZEROCOPY_RECEIVE", "TCP_INQ", "TCP_TX_DELAY". Se agregó
   "IP_PKTINFO", "IP_UNBLOCK_SOURCE", "IP_BLOCK_SOURCE",
   "IP_ADD_SOURCE_MEMBERSHIP", "IP_DROP_SOURCE_MEMBERSHIP".

   Distinto en la versión 3.13: Added "SO_BINDTOIFINDEX". On Linux
   this constant can be used in the same way that "SO_BINDTODEVICE" is
   used, but with the index of a network interface instead of its
   name.

   Distinto en la versión 3.14: Added missing "IP_FREEBIND",
   "IP_RECVERR", "IPV6_RECVERR", "IP_RECVTTL", and
   "IP_RECVORIGDSTADDR" on Linux.

   Distinto en la versión 3.14: Added support for "TCP_QUICKACK" on
   Windows platforms when available.

socket.AF_CAN
socket.PF_CAN
SOL_CAN_*
CAN_*

   Muchas constantes de estos formularios, documentadas en la
   documentación de Linux, también se definen en el módulo de socket.

   Availability: Linux >= 2.6.25, NetBSD >= 8.

   Added in version 3.3.

   Distinto en la versión 3.11: Se ha agregado compatibilidad con
   NetBSD.

   Distinto en la versión 3.14: Restored missing "CAN_RAW_ERR_FILTER"
   on Linux.

socket.CAN_BCM
CAN_BCM_*

   CAN_BCM, en la familia de protocolo CAN, es el protocolo del
   administrador de difusión (BCM. Las constantes del administrador de
   difusión, documentada en la documentación de Linux, también esta
   definidos en el modulo socket.

   Availability: Linux >= 2.6.25.

   Nota:

     El indicador "CAN_BCM_CAN_FD_FRAME" esta solamente disponible en
     Linux >= 4.8.

   Added in version 3.4.

socket.CAN_RAW_FD_FRAMES

   Habilita la compatibilidad con CAN FD en un socket CAN_RAW. Esta
   opción está deshabilitada de forma predeterminada. Esto permite que
   la aplicación envíe tramas CAN y CAN FD; sin embargo, debe aceptar
   las tramas CAN y CAN FD al leer desde el socket.

   Esta constante se documenta en la documentación de Linux.

   Availability: Linux >= 3.6.

   Added in version 3.5.

socket.CAN_RAW_JOIN_FILTERS

   Se une a los filtros CAN aplicados de modo que solo las tramas CAN
   que coinciden con todos los filtros CAN dados se pasan al espacio
   del usuario.

   Esta constante se documenta en la documentación de Linux.

   Availability: Linux >= 4.1.

   Added in version 3.9.

socket.CAN_ISOTP

   CAN_ISOTP, en el protocolo de familia CAN, es el protocolo  ISO-TP
   (ISO 15765-2). Constantes ISO-TP, documentadas en la documentación
   Linux.

   Availability: Linux >= 2.6.25.

   Added in version 3.7.

socket.CAN_J1939

   CAN_J1939, en el protocolo de familias CAN, es el protocolo SAE
   J1939. Constantes J1939, documentadas en el documentación Linux.

   Availability: Linux >= 5.4.

   Added in version 3.9.

socket.AF_DIVERT
socket.PF_DIVERT

   Estas dos constantes, documentadas en la página del manual de
   FreeBSD divert(4), también están definidas en el módulo de socket.

   Availability: FreeBSD >= 14.0.

   Added in version 3.12.

socket.AF_PACKET
socket.PF_PACKET
PACKET_*

   Muchas constantes de estos formularios, documentadas en la
   documentación de Linux, también se definen en el módulo de socket.

   Availability: Linux >= 2.2.

socket.ETH_P_ALL

   El "service_id" es el identificador del servicio
   registrado.:data:*!ETH_P_ALL* se puede utilizar en el constructor
   "socket" como *proto* para la familia "AF_PACKET" para capturar
   cada paquete, independientemente del protocolo.

   Para obtener más información, consulte la página de manual
   *packet(7)*.

   Availability: Linux.

   Added in version 3.12.

socket.AF_RDS
socket.PF_RDS
socket.SOL_RDS
RDS_*

   Muchas constantes de estos formularios, documentadas en la
   documentación de Linux, también se definen en el módulo de socket.

   Availability: Linux >= 2.6.30.

   Added in version 3.3.

socket.SIO_RCVALL
socket.SIO_KEEPALIVE_VALS
socket.SIO_LOOPBACK_FAST_PATH
RCVALL_*

   Constantes para Windows’ WSAIoctl(). Las constantes se utiliza como
   argumentos al método "ioctl()" de objetos de sockets.

   Distinto en la versión 3.6: "SIO_LOOPBACK_FAST_PATH" ha sido
   agregado.

TIPC_*

   LAS constantes relacionadas con TIPC, que coinciden con las
   exportadas por la API de socket de C. Consulte la documentación de
   TIPC para obtener más información.

socket.AF_ALG
socket.SOL_ALG
ALG_*

   Constantes para la criptográfica del Kernel de Linux.

   Availability: Linux >= 2.6.38.

   Added in version 3.6.

socket.AF_VSOCK
socket.IOCTL_VM_SOCKETS_GET_LOCAL_CID
VMADDR*
SO_VM*

   Constantes para la comunicación host/invitado de Linux.

   Availability: Linux >= 4.8.

   Added in version 3.7.

socket.AF_LINK

   Availability: BSD, macOS.

   Added in version 3.4.

socket.has_ipv6

   Esta constante contiene un valor booleano que indica si IPv6 se
   admite en esta plataforma.

socket.AF_BLUETOOTH
socket.BTPROTO_L2CAP
socket.BTPROTO_RFCOMM
socket.BTPROTO_HCI
socket.BTPROTO_SCO

   Integer constants for use with Bluetooth addresses.

socket.BDADDR_ANY
socket.BDADDR_LOCAL

   Estas son constantes de cadenas que contienen direcciones Bluetooth
   con significados especiales. Por ejemplo "BDADDR_ANY" son usados
   para indicar cualquier dirección al especificar el socket
   vinculante con "BTPROTO_RFCOMM".

socket.BDADDR_BREDR
socket.BDADDR_LE_PUBLIC
socket.BDADDR_LE_RANDOM

   These constants describe the Bluetooth address type when binding or
   connecting a "BTPROTO_L2CAP" socket.

   Availability: Linux, FreeBSD

   Added in version 3.14.

socket.SOL_RFCOMM
socket.SOL_L2CAP
socket.SOL_HCI
socket.SOL_SCO
socket.SOL_BLUETOOTH

   Used in the level argument to the "setsockopt()" and "getsockopt()"
   methods of Bluetooth socket objects.

   "SOL_BLUETOOTH" is only available on Linux. Other constants are
   available if the corresponding protocol is supported.

SO_L2CAP_*
socket.L2CAP_LM
L2CAP_LM_*
SO_RFCOMM_*
RFCOMM_LM_*
SO_SCO_*
SO_BTH_*
BT_*

   Used in the option name and value argument to the "setsockopt()"
   and "getsockopt()" methods of Bluetooth socket objects.

   "BT_*" and "L2CAP_LM" are only available on Linux. "SO_BTH_*" are
   only available on Windows. Other constants may be available on
   Linux and various BSD platforms.

   Added in version 3.14.

socket.HCI_FILTER
socket.HCI_TIME_STAMP
socket.HCI_DATA_DIR
socket.SO_HCI_EVT_FILTER
socket.SO_HCI_PKT_FILTER

   Option names for use with "BTPROTO_HCI". Availability and format of
   the option values depend on platform.

   Distinto en la versión 3.14: Added "SO_HCI_EVT_FILTER" and
   "SO_HCI_PKT_FILTER" on NetBSD and DragonFly BSD. Added
   "HCI_DATA_DIR" on FreeBSD, NetBSD and DragonFly BSD.

socket.HCI_DEV_NONE

   The "device_id" value used to create an HCI socket that isn't
   specific to a single Bluetooth adapter.

   Availability: Linux

   Added in version 3.14.

socket.HCI_CHANNEL_RAW
socket.HCI_CHANNEL_USER
socket.HCI_CHANNEL_MONITOR
socket.HCI_CHANNEL_CONTROL
socket.HCI_CHANNEL_LOGGING

   Possible values for "channel" field in the "BTPROTO_HCI" address.

   Availability: Linux

   Added in version 3.14.

socket.AF_QIPCRTR

   Constante para el protocolo de router IPC de Qualcomm, que se
   utiliza para comunicarse con procesadores remotos que brindan
   servicios.

   Availability: Linux >= 4.7.

socket.SCM_CREDS2
socket.LOCAL_CREDS
socket.LOCAL_CREDS_PERSISTENT

   LOCAL_CREDS y LOCAL_CREDS_PERSISTENT pueden usarse con sockets
   SOCK_DGRAM, SOCK_STREAM, equivalente a Linux/DragonFlyBSD
   SO_PASSCRED, mientras que LOCAL_CREDS envía las credenciales en la
   primera lectura, LOCAL_CREDS_PERSISTENT envía para cada lectura,
   SCM_CREDS2 debe entonces ser usado para este último para el tipo de
   mensaje.

   Added in version 3.11.

   Availability: FreeBSD.

socket.SO_INCOMING_CPU

   Constante para optimizar la localidad CPU, a ser usada en conjunto
   con "SO_REUSEPORT".

   Added in version 3.11.

   Availability: Linux >= 3.9

socket.SO_REUSEPORT_LB

      Constant to enable duplicate address and port bindings with load
      balancing.

   Added in version 3.14.

   Availability: FreeBSD >= 12.0

socket.AF_HYPERV
socket.HV_PROTOCOL_RAW
socket.HVSOCKET_CONNECT_TIMEOUT
socket.HVSOCKET_CONNECT_TIMEOUT_MAX
socket.HVSOCKET_CONNECTED_SUSPEND
socket.HVSOCKET_ADDRESS_FLAG_PASSTHRU
socket.HV_GUID_ZERO
socket.HV_GUID_WILDCARD
socket.HV_GUID_BROADCAST
socket.HV_GUID_CHILDREN
socket.HV_GUID_LOOPBACK
socket.HV_GUID_PARENT

   Constantes para sockets Windows Hyper-V para comunicaciones
   host/invitado.

   Availability: Windows.

   Added in version 3.12.

socket.ETHERTYPE_ARP
socket.ETHERTYPE_IP
socket.ETHERTYPE_IPV6
socket.ETHERTYPE_VLAN

   Número de protocolo IEEE 802.3. constantes.

   Availability: Linux, FreeBSD, macOS.

   Added in version 3.12.

socket.SHUT_RD
socket.SHUT_WR
socket.SHUT_RDWR

   These constants are used by the "shutdown()" method of socket
   objects.

   Availability: not WASI.

### Funciones

#### Creación de sockets

Todas las siguientes funciones crean socket objects.

The "socket" class constructor creates a new socket directly; see
Objetos Socket for its parameters and full description.

socket.socketpair([family[, type[, proto]]])

   Build a pair of connected socket objects using the given address
   family, socket type, and protocol number.  Address family, socket
   type, and protocol number are as for the "socket()" function. The
   default family is "AF_UNIX" if defined on the platform; otherwise,
   the default is "AF_INET".

   Los sockets creados recientemente son non-inheritable.

   Distinto en la versión 3.2: Los objetos de socket devueltos ahora
   admiten toda la API de socket, en lugar de un subconjunto.

   Distinto en la versión 3.4: Los sockets devueltos ahora no son
   heredables.

   Distinto en la versión 3.5: Se ha agregado compatibilidad con
   Windows.

socket.create_connection(address, timeout=GLOBAL_DEFAULT, source_address=None, *, all_errors=False)

   Se conecta a un servicio TCP que esté escuchando en Internet
   *address* (un "(host, port)" de 2 tuplas) y retorna el objeto de
   socket. Esta es una función de nivel superior que
   "socket.connect()": si *host* es un nombre de host no numérico,
   intentará resolverlo para "AF_INET" y "AF_INET6", y luego intentará
   conectarse a todas las direcciones posibles sucesivamente hasta que
   la conexión se realice correctamente. Esto facilita la escritura de
   clientes que sean compatibles con IPv4 e IPv6.

   Pasando el parámetro opcional *timeout* establece el tiempo de
   espera dentro de la instancia del socket. Si no es proporcionado
   *timeout*, la configuración global de tiempo de espera
   predeterminada retornada por "getdefaulttimeout()" es usada.

   Si se suministra, *source_address* debe ser una ''(host, puerto)''
   de 2 tuplas para que el socket se enlace como su dirección de
   origen antes de conectarse.  Si el host o el puerto son '' o 0
   respectivamente, se utilizará el comportamiento predeterminado del
   sistema operativo.

   Cuando una conexión no puede ser creada, se lanza una exception.
   Por defecto, es la excepción de la última dirección en la lista. Si
   *all_errors* es "True", es un "ExceptionGroup" conteniendo los
   errores de todos los intentos.

   Distinto en la versión 3.2: *source_address* ha sido agregado.

   Distinto en la versión 3.11: *all_errors* ha sido agregado.

socket.create_server(address, *, family=AF_INET, backlog=None, reuse_port=False, dualstack_ipv6=False)

   Función conveniente que crea un socket TCP vinculado a *dirección*
   (un "(host, puerto)" de 2 tuplas) y devuelve el objeto del socket.

   *familia* debe ser "AF_INET" o "AF_INET6". *backlog* es el tamaño
   de la cola pasado a "socket.listen()"; cuando "0" se elige un valor
   predeterminado razonable. *reuse_port* dicta si se debe establecer
   la opción de socket "SO_REUSEPORT".

   If *dualstack_ipv6* is true, *family* is "AF_INET6" and the
   platform supports it the socket will be able to accept both IPv4
   and IPv6 connections, else it will raise "ValueError". Most POSIX
   platforms and Windows are supposed to support this functionality.
   When this functionality is enabled the address returned by
   "socket.getpeername()" when an IPv4 connection occurs will be an
   IPv6 address represented as an IPv4-mapped IPv6 address. If
   *dualstack_ipv6* is false it will explicitly disable this
   functionality on platforms that enable it by default (e.g. Linux).
   This parameter can be used in conjunction with
   "has_dualstack_ipv6()":

      import socket

      addr = ("", 8080)  # all interfaces, port 8080
      if socket.has_dualstack_ipv6():
          s = socket.create_server(addr, family=socket.AF_INET6, dualstack_ipv6=True)
      else:
          s = socket.create_server(addr)

   Nota:

     En plataformas POSIX la opción del socket "SO_REUSEADDR" está
     configurado para inmediatamente rehusar los sockets previos que
     estaban vinculados la misma *address* y permanecer en estado
     TIME_WAIT.

   Added in version 3.8.

socket.has_dualstack_ipv6()

   Retorna "True" si la plataforma admite la creación de un socket TCP
   que pueda manejar conexiones IPv4 e IPv6.

   Added in version 3.8.

socket.fromfd(fd, family, type, proto=0)

   Duplicate the file descriptor *fd* (an integer as returned by a
   file object's "fileno()" method) and build a socket object from the
   result.  Address family, socket type and protocol number are as for
   the "socket()" function. The file descriptor should refer to a
   socket, but this is not checked --- subsequent operations on the
   object may fail if the file descriptor is invalid. This function is
   rarely needed, but can be used to get or set socket options on a
   socket passed to a program as standard input or output (such as a
   server started by the Unix inet daemon).  The socket is assumed to
   be in blocking mode.

   El socket recién creado es non-inheritable.

   Distinto en la versión 3.4: Los sockets devueltos ahora no son
   heredables.

socket.fromshare(data)

   Cree una instancia de un socket a partir de los datos obtenidos del
   método "socket.share()".  Se supone que el socket está en modo de
   bloqueo.

   Availability: Windows.

   Added in version 3.3.

#### Otras funciones

The "socket" module also offers various network-related services:

socket.close(fd)

   Close a socket file descriptor. This is like "os.close()", but for
   sockets. On some platforms (most notably Windows) "os.close()" does
   not work for socket file descriptors.

   Added in version 3.7.

socket.getaddrinfo(host, port, family=AF_UNSPEC, type=0, proto=0, flags=0)

   This function wraps the C function "getaddrinfo" of the underlying
   system.

   Traduce el argumento *host*/*port* dentro de una secuencia de 5
   tuplas que contiene todo los argumentos necesarios para crear un
   socket conectado a ese servicio. *host* es un nombre de dominio,
   una cadena en representación de una dirección IPV4/IPV6 o "None".
   *port* es una nombre de una cadena de servicio como "'http'", un
   numero de puerto numérico o "None". Pasando "None" como el valor
   del  *host* y *port*, pasando "NULL" a la API C subyacente.

   The *family*, *type* and *proto* arguments can be optionally
   specified in order to provide options and limit the list of
   addresses returned. Pass their default values ("AF_UNSPEC", 0, and
   0, respectively) to not limit the results. See the note below for
   details.

   The *flags* argument can be one or several of the "AI_*" constants,
   and will influence how results are computed and returned. For
   example, "AI_NUMERICHOST" will disable domain name resolution and
   will raise an error if *host* is a domain name.

   La función devuelve una lista de 5 tuplas con la siguiente
   estructura:

   "(family, type, proto, canonname, sockaddr)"

   In these tuples, *family*, *type*, *proto* are all integers and are
   meant to be passed to the "socket()" function.  *canonname* will be
   a string representing the canonical name of the *host* if
   "AI_CANONNAME" is part of the *flags* argument; else *canonname*
   will be empty.  *sockaddr* is a tuple describing a socket address,
   whose format depends on the returned *family* (a "(address, port)"
   2-tuple for "AF_INET", a "(address, port, flowinfo, scope_id)"
   4-tuple for "AF_INET6"), and is meant to be passed to the
   "socket.connect()" method.

   Nota:

     If you intend to use results from "getaddrinfo()" to create a
     socket (rather than, for example, retrieve *canonname*), consider
     limiting the results by *type* (e.g. "SOCK_STREAM" or
     "SOCK_DGRAM") and/or *proto* (e.g. "IPPROTO_TCP" or
     "IPPROTO_UDP") that your application can handle.The behavior with
     default values of *family*, *type*, *proto* and *flags* is
     system-specific.Many systems (for example, most Linux
     configurations) will return a sorted list of all matching
     addresses. These addresses should generally be tried in order
     until a connection succeeds (possibly tried in parallel, for
     example, using a Happy Eyeballs algorithm). In these cases,
     limiting the *type* and/or *proto* can help eliminate
     unsuccessful or unusable connection attempts.Some systems will,
     however, only return a single address. (For example, this was
     reported on Solaris and AIX configurations.) On these systems,
     limiting the *type* and/or *proto* helps ensure that this address
     is usable.

   Genera un auditing event "socket.getaddrinfo" con los argumentos
   "host", "port", "family", "type", "protocol".

   En el ejemplo siguiente se obtiene información de dirección para
   una conexión TCP hipotética a "example.org" en el puerto 80 (los
   resultados pueden diferir en el sistema si IPv6 no está
   habilitado):

      >>> socket.getaddrinfo("example.org", 80, proto=socket.IPPROTO_TCP)
      [(socket.AF_INET6, socket.SOCK_STREAM,
       6, '', ('2606:2800:220:1:248:1893:25c8:1946', 80, 0, 0)),
       (socket.AF_INET, socket.SOCK_STREAM,
       6, '', ('93.184.216.34', 80))]

   Distinto en la versión 3.2: los parámetros ahora se pueden pasar
   mediante argumentos de palabra clave.

   Distinto en la versión 3.7: para direcciones de multidifusión IPv6,
   la cadena que representa una dirección no contendrá partes
   "%scope_id".

socket.getfqdn([name])

   Retorna un nombre de dominio completo para *name*. Si *name* se
   omite o está vacío, se interpreta como el host local. Para
   encontrar el nombre completo, se comprueba el nombre de host
   retornado por "gethostbyaddr()", seguido de los alias del host, si
   están disponibles. Se selecciona el primer nombre que incluye un
   punto. En caso de que no haya disponible un nombre de dominio
   completo y se haya proporcionado *name*, se retorna sin cambios. Si
   *name* estaba vacío o era igual a "'0.0.0.0'", se retorna el nombre
   de host de "gethostname()".

socket.gethostbyname(hostname)

   Traduce un nombre de host a un formato de dirección IPV4. La
   dirección IPV4 es retornada como una cadena, como "’100.50.200.5’".
   Si el nombre de host es una dirección IPV4 en sí, se devuelve sin
   cambios. Observa "gethostbyname_ex()" para una interfaz mas
   completa. "gethostbyname()" no soporta la resolución de nombres
   IPV6, y "getaddrinfo()" debe utilizarse en su lugar para
   compatibilidad con doble pila IPv4/v6.

   Genera un evento auditing "socket.gethostbyname" con el argumento
   "hostname".

   Availability: not WASI.

socket.gethostbyname_ex(hostname)

   Traducir un nombre de host a IPv4, formato de dirección de interfaz
   extendida. Devuelve una tupla de 3 elementos "(hostname, aliaslist,
   ipaddrlist)" donde *hostname* es el nombre de host principal del
   host, *aliaslist* es una lista (posiblemente vacía) de nombres de
   host alternativos para la misma dirección y *ipaddrlist* es una
   lista de direcciones IPv4 para la misma interfaz en el mismo host
   (a menudo, pero no siempre, una única dirección).
   "gethostbyname_ex()" no admite la resolución de nombres IPv6 y
   "getaddrinfo()" debe usarse en su lugar para la compatibilidad con
   doble pila IPv4/v6.

   Genera un evento auditing "socket.gethostbyname" con el argumento
   "hostname".

   Availability: not WASI.

socket.gethostname()

   Retorna una cadena que contenga el nombre de host de la máquina
   donde se está ejecutando actualmente el intérprete de Python.

   Genera un auditing event "socket.gethostname" sin argumentos.

   Nota: "gethostname()" no siempre retorna el nombre de dominio
   completo, usa "getfqdn()" para eso.

   Availability: not WASI.

socket.gethostbyaddr(ip_address)

   Devuelve una tupla de 3 elementos "(nombre de host, lista de alias,
   lista de ipaddr)" donde *nombre de host* es el nombre de host
   principal que responde a la *dirección_ip* dada, *lista de alias*
   es una lista (posiblemente vacía) de nombres de host alternativos
   para el mismo dirección, y *ipaddrlist* es una lista de direcciones
   IPv4/v6 para la misma interfaz en el mismo host (lo más probable es
   que contenga solo una dirección). Para encontrar el nombre de
   dominio completo, utilice la función "getfqdn()". "gethostbyaddr()"
   admite tanto IPv4 como IPv6.

   Generar un auditing event "socket.gethostbyaddr" con los argumentos
   "ip_address".

   Availability: not WASI.

socket.getnameinfo(sockaddr, flags)

   Traduce una dirección de socket  *sockaddr* en una 2-tupla "(host,
   port)". Dependiendo de la configuraciones de *flags*, el resultado
   puede contener un nombre de dominio completo o una representación
   numérica de la dirección en *host*. De igual manera, *port* puede
   contener un nombre de puerto de cadena de caracteres o un numero de
   puerto numérico.

   Para las direcciones IPv6, "%scope" se anexa a la parte del host si
   *sockaddr* contiene *scopeid* significativo. Generalmente esto
   sucede para las direcciones de multidifusión.

   Para mas información sobre *flags* pueden consultar
   *getnameinfo(3)*.

   Plantea un auditing event "socket.getnameinfo" con el argumento
   "sockaddr".

   Availability: not WASI.

socket.getprotobyname(protocolname)

   Translate an internet protocol name (for example, "'icmp'") to a
   constant suitable for passing as the (optional) third argument to
   the "socket()" function.  This is usually only needed for sockets
   opened in "raw" mode ("SOCK_RAW"); for the normal socket modes, the
   correct protocol is chosen automatically if the protocol is omitted
   or zero.

   Availability: not WASI.

socket.getservbyname(servicename[, protocolname])

   Traduzca un nombre de servicio de Internet y un nombre de protocolo
   a un número de puerto para ese servicio. El nombre de protocolo
   opcional, si se proporciona, debe ser "'tcp'" o "'udp'"; de lo
   contrario, cualquier protocolo coincidirá.

   Genera un auditing event "socket.getservbyname" con los argumentos
   "servicename", "protocolname".

   Availability: not WASI.

socket.getservbyport(port[, protocolname])

   Traduzca un número de puerto de Internet y un nombre de protocolo a
   un nombre de servicio para ese servicio. El nombre de protocolo
   opcional, si se proporciona, debe ser "'tcp'" o "'udp'"; de lo
   contrario, cualquier protocolo coincidirá.

   Genera un auditing event "socket.getservbyport" con los argumentos
   "port", "protocolname".

   Availability: not WASI.

socket.ntohl(x)

   Convierta enteros positivos de 32 bits de red a orden de bytes de
   host.  En equipos donde el orden de bytes de host es el mismo que
   el orden de bytes de red, se trata de un no-op; de lo contrario,
   realiza una operación de intercambio de 4 bytes.

socket.ntohs(x)

   Convierta enteros positivos de 16 bits de red a orden de bytes de
   host.  En equipos donde el orden de bytes de host es el mismo que
   el orden de bytes de red, se trata de un no-op; de lo contrario,
   realiza una operación de intercambio de 2 bytes.

   Distinto en la versión 3.10: Lanza "OverflowError" si *x* no cabe
   en un entero sin signo de 16 bits.

socket.htonl(x)

   Convierta enteros positivos de 32 bits del host al orden de bytes
   de red.  En equipos donde el orden de bytes de host es el mismo que
   el orden de bytes de red, se trata de un no-op; de lo contrario,
   realiza una operación de intercambio de 4 bytes.

socket.htons(x)

   Convierta enteros positivos de 16 bits del host al orden de bytes
   de red.  En equipos donde el orden de bytes de host es el mismo que
   el orden de bytes de red, se trata de un no-op; de lo contrario,
   realiza una operación de intercambio de 2 bytes.

   Distinto en la versión 3.10: Lanza "OverflowError" si *x* no cabe
   en un entero sin signo de 16 bits.

socket.inet_aton(ip_string)

   Convierte una dirección IPv4 desde el formato de cadena de cuatro
   puntos (por ejemplo, ‘123.45.67.89’) a formato binario empaquetado
   de 32 bits, como un objeto de bytes de cuatro caracteres de
   longitud. Esto es útil cuando se convierte con un programa que usa
   la librería estándar C y necesita objetos de tipo "in_addr", que es
   el tipo C para el binario empaquetado de 32 bits que devuelve esta
   función.

   Ademas "inet_aton`acepta cadena de caracteres con menos de tres
   puntos, observar la pagina del manual Unix :manpage:`inet(3)()"
   para mas detalles.

   Si la cadena de dirección IPv4 es pasada a esta función es
   invalido, "OSError" se lanzará. Tenga en cuenta que exactamente lo
   que es valido depende de la implementación C de "inet_aton()".

   "inet_aton()" no admite IPV6, y "inet_pton()" deberían utilizarse
   en su lugar para compatibilidad con doble pilas IPV4/v6.

socket.inet_ntoa(packed_ip)

   Convierte una dirección IPv4 empaquetada de 32 bits (un *bytes-like
   object* cuatro bytes de longitud) a su representación estándar de
   cadena de cuatro puntos (por ejemplo ‘123.45.67.89’). Esto es útil
   cuando convertimos con un programa que usa la librería estándar C y
   necesita objetos de tipo "in_addr", que es el tipo C para los datos
   binarios empaquetados de 32 bits que esta función toma como
   argumento.

   Si la secuencia de byte pasada a esta función no es exactamente 4
   bytes de longitud  "OSError" podría generarse "inet_ntoa()" no
   soporta IPV6, y "inet_ntop()" debe utilizarse en su lugar para
   compatibilidad con doble pila IPv4 / v6.

   Distinto en la versión 3.5: Ahora se acepta la grabación *bytes-
   like object*.

socket.inet_pton(address_family, ip_string)

   Convierte una dirección IP desde su formato de cadena específico de
   la familia a un formato binario empaquetado. "inet_pton()" es útil
   cuando una librería o protocolo de red llama desde un objeto de
   tipo "in_addr" (similar a "inet_aton()") o "in6_addr".

   Los Valores soportados para *address_family* son actualmente
   "AF_INET" y "AF_INET6". Si la cadena de dirección IP *ip_string* no
   es válida, "OSError" se genera. Tenga en cuenta que exactamente lo
   que es válido depende tanto del valor de *address_family* como de
   la implementación subyacente de "inet_pton()".

   Availability: Unix, Windows.

   Distinto en la versión 3.4: Se ha añadido compatibilidad con
   Windows

socket.inet_ntop(address_family, packed_ip)

   Convierte una dirección IP empaquetada (un *bytes-like object* de
   algún numero de bytes) a su representación estándar de cadena
   específica de la familia (por ejemplo "’7.10.0.5’" o
   "’5aef:2b::8’"). "inet_ntop()" es útil cuando una librería o
   protocolo de red retorna un objeto de tipo "in_addr" (similar para
   "inet_ntoa()") o "in6_addr".

   Los valores soportados para *address_family* actualmente son
   "AF_INET" y "AF_INET6". Si los objetos de bytes *packed_ip* no
   tienen la longitud correcta para la familia de direcciones
   especificas, "ValueError" podría generarse. "OSError" se genera
   para errores desde la llamada a "inet_ntop()".

   Availability: Unix, Windows.

   Distinto en la versión 3.4: Se ha añadido compatibilidad con
   Windows

   Distinto en la versión 3.5: Ahora se acepta la grabación *bytes-
   like object*.

socket.CMSG_LEN(length)

   Retorna la longitud total, sin relleno de arrastre, de un elemento
   de datos auxiliares con datos asociados del *length*. Este valor se
   puede utilizar a menudo como tamaño de búfer para "recvmsg()" para
   recibir un solo valor de datos auxiliares, pero **RFC 3542**
   requiere aplicaciones portables para usar "CMSG_SPACE()" y así
   incluir espacio para el relleno, incluso cuando el elemento será el
   último en el búfer. Genera  "OverflowError" si *length* está fuera
   del rango de valores permitido.

   Availability: Unix, not WASI.

   La mayoría de las plataformas Unix.

   Added in version 3.3.

socket.CMSG_SPACE(length)

   Retorna el tamaño del buffer necesario por "recvmsg()" para recibir
   un elemento de datos auxiliares con datos asociados del *length*
   dado, junto con cualquier relleno final. El espacio de buffer
   necesario para recibir múltiples elementos es la suma de los
   valores de "CMSG_SPACE()" para los datos asociados con la
   longitudes. Genera "OverflowError" si *length* está fuera del rango
   de valores permitido.

   Tenga en cuenta que algunos sistemas pueden admitir datos
   auxiliares sin proporcionar esta función.  Tenga en cuenta también
   que establecer el tamaño del búfer utilizando los resultados de
   esta función puede no limitar con precisión la cantidad de datos
   auxiliares que se pueden recibir, ya que los datos adicionales
   pueden caber en el área de relleno.

   Availability: Unix, not WASI.

   la mayoría de las plataformas Unix.

   Added in version 3.3.

socket.getdefaulttimeout()

   Retorna el tiempo de espera por defecto en segundos (flotante) para
   los objetos de un nuevo socket. Un valor de "None" indicada que los
   objetos del nuevo socket no tiene un tiempo de espera. Cuando el
   modulo socket es importado primero, por defecto es "None".

socket.setdefaulttimeout(timeout)

   Selecciona el tiempo de espera por defecto en segundos (flotante )
   para los objetos nuevos del socket. Cuando el modulo socket es
   importado primero, el valor por defecto es "None". Observar
   "settimeout()" para posible valores y sus respectivos significados.

socket.sethostname(name)

   Establece el nombre de host de la maquina en *name*. Esto genera un
   "OSError" si no tiene suficientes derechos.

   Plantea un auditing event "socket.sethostname" con el argumento
   "name".

   Availability: Unix, not Android.

   Added in version 3.3.

socket.if_nameindex()

   Retorna una lista de tuplas de información de interfaz de red
   (índice int, cadena de nombre). "OSError" si se produce un error en
   la llamada del sistema.

   Availability: Unix, Windows, not WASI.

   Added in version 3.3.

   Distinto en la versión 3.8: Se ha agregado compatibilidad con
   Windows.

   Nota:

     En Windows las interfaces de redes tienen diferentes nombres en
     diferentes contextos (todos los nombres son ejemplos):

     * UUID: "{FB605B73-AAC2-49A6-9A2F-25416AEA0573}"

     * nombre: "ethernet_32770"

     * nombre amigable: "vEthernet (nat)"

     * descripción: "Hyper-V Virtual Ethernet Adapter"

     Esta función retorna los nombres del segundo formulario de la
     lista, en este caso de ejemplo "ethernet_32770".

socket.if_nametoindex(if_name)

   Retorna un número de índice de interfaz de red correspondiente a un
   nombre de interfaz. "OSError" si no existe ninguna interfaz con el
   nombre especificado.

   Availability: Unix, Windows, not WASI.

   Added in version 3.3.

   Distinto en la versión 3.8: Se ha agregado compatibilidad con
   Windows.

   Ver también:

     “”Interface name” es un nombre como se documenta en
     "if_nameindex()".

socket.if_indextoname(if_index)

   Retorna un nombre de interfaz de red correspondiente a un número de
   índice de interfaz. "OSError" si no existe ninguna interfaz con el
   índice dado.

   Availability: Unix, Windows, not WASI.

   Added in version 3.3.

   Distinto en la versión 3.8: Se ha agregado compatibilidad con
   Windows.

   Ver también:

     “”Interface name” es un nombre como se documenta en
     "if_nameindex()".

socket.send_fds(sock, buffers, fds[, flags[, address]])

   Send the list of file descriptors *fds* over an "AF_UNIX" socket
   *sock*. The *fds* parameter is a sequence of file descriptors.
   Consult "sendmsg()" for the documentation of these parameters.

   Availability: Unix, not WASI.

   Plataformas Unix que soporten "sendmsg()" y el mecanismo
   "SCM_RIGHTS".

   Added in version 3.9.

socket.recv_fds(sock, bufsize, maxfds[, flags])

   Receive up to *maxfds* file descriptors from an "AF_UNIX" socket
   *sock*. Return "(msg, list(fds), flags, addr)". Consult "recvmsg()"
   for the documentation of these parameters.

   Availability: Unix, not WASI.

   Unix platforms supporting "recvmsg()" and "SCM_RIGHTS" mechanism.

   Added in version 3.9.

   Nota:

     Cualquier número entero truncado al final de la lista de
     descriptores de archivo.

## Objetos Socket

class socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)

   Crear un nuevo socket usando la dirección de familia dada, tipo de
   socket y el numero de protocolo. La dirección de familia debería
   ser "AF_INET" (por defecto), "AF_INET6", "AF_UNIX", "AF_CAN",
   "AF_PACKET", o "AF_RDS". El tipo de socket debería ser
   "SOCK_STREAM" (por defecto), "SOCK_DGRAM", "SOCK_RAW" o quizás una
   de las otras constantes "SOCK_". El numero de protocolo es
   usualmente cero u omitirse o en el caso donde la familia de
   dirección es "AF_CAN" el protocolo debería ser uno de "CAN_RAW",
   "CAN_BCM", "CAN_ISOTP" o "CAN_J1939".

   If *fileno* is specified, the values for *family*, *type*, and
   *proto* are auto-detected from the specified file descriptor.
   Auto-detection can be overruled by calling the function with
   explicit *family*, *type*, or *proto* arguments.  This only affects
   how Python represents e.g. the return value of
   "socket.getpeername()" but not the actual OS resource.  Unlike
   "socket.fromfd()", *fileno* will return the same socket and not a
   duplicate. This may help close a detached socket using
   "socket.close()".

   El socket recién creado es non-inheritable.

   Genera un auditing event "socket.__new__" con los argumentos
   "self", "family", "type", "protocol".

   Distinto en la versión 3.3: Se añadió la familia AF_CAN. Se añadió
   la familia AF_RDS.

   Distinto en la versión 3.4: El protocolo CAN_BCM ha sido agregado.

   Distinto en la versión 3.4: Los sockets devueltos ahora no son
   heredables.

   Distinto en la versión 3.7: El protocolo CAN_ISOTP ha sido
   agregado.

   Distinto en la versión 3.7: Cuando las banderas bit "SOCK_NONBLOCK"
   or "SOCK_CLOEXEC" están aplicadas a *type*, se borran, y
   "socket.type" no las reflejará. Igual se pasan a la llamada *socket
   ()* del sistema subyacente. Por lo tanto,

      sock = socket.socket(
          socket.AF_INET,
          socket.SOCK_STREAM | socket.SOCK_NONBLOCK)

   seguirá creando un socket sin bloqueo en los sistemas operativos
   que admiten "SOCK_NONBLOCK", pero "sock.type" se establecerá en
   "socket.SOCK_STREAM".

   Distinto en la versión 3.9: El protocolo CAN_J1939 ha sido
   agregado.

   Distinto en la versión 3.10: Se agregó el protocolo IPPROTO_MPTCP.

   Los objetos socket tienen los siguientes métodos. Excepto para
   "makefile()", esto corresponde al sistema de llamadas Unix para
   sockets.

   Distinto en la versión 3.2: El soporte para el protocolo *context
   manager* ha sido agregado. Salir del gestor de contexto es
   equivalente para el llamado "close()".

   accept()

      Acepta una conexión. El socket debe estar vinculado a una
      dirección y estar escuchando las conexiones. El valor de retorno
      es el par "(conn, address)" cuando *conn* es un *new* objeto
      socket usado para enviar y recibir información en la conexión, y
      *address* es la dirección vinculada al socket en el extremo de
      la conexión.

      El socket recién creado es non-inheritable.

      Distinto en la versión 3.4: El socket ahora no es heredable.

      Distinto en la versión 3.5: Si se interrumpe la llamada del
      sistema y el controlador de señal no genera una excepción, el
      método ahora vuelve a intentar la llamada del sistema en lugar
      de generar una excepción "InterruptedError" (consulte **PEP
      475** para la lógica).

   bind(address)

      Bind the socket to *address*.  The socket must not already be
      bound. The format of *address* depends on the address family ---
      see Familias Socket.

      Genera un auditing event "socket.getaddrinfo" con los argumentos
      "host", "port", "family", "type", "protocol".

      Availability: not WASI.

   close()

      Mark the socket closed.  The underlying system resource (e.g. a
      file descriptor) is also closed when all file objects from
      "makefile()" are closed.  Once that happens, all future
      operations on the socket object will fail. The remote end will
      receive no more data (after queued data is flushed).

      Los sockets se cierran automáticamente cuando se recogen basura,
      pero se recomienda "cerrarlos()" explícitamente, o usar una
      instrucción "with" alrededor de ellos.

      Distinto en la versión 3.6: "OSError" is now raised if an error
      occurs when the underlying "close()" call is made.

      Nota:

        "close()" releases the resource associated with a connection
        but does not necessarily close the connection immediately.  If
        you want to close the connection in a timely fashion, call
        "shutdown()" before "close()".

   connect(address)

      Connect to a remote socket at *address*. The format of *address*
      depends on the address family --- see Familias Socket.

      If the connection is interrupted by a signal, the method waits
      until the connection completes, or raises a "TimeoutError" on
      timeout, if the signal handler doesn't raise an exception and
      the socket is blocking or has a timeout. For non-blocking
      sockets, the method raises an "InterruptedError" exception if
      the connection is interrupted by a signal (or the exception
      raised by the signal handler).

      Genera un auditing event "socket.connect" con los argumentos
      "self", "address".

      Distinto en la versión 3.5: El método ahora espera hasta que se
      completa la conexión en lugar de generar una excepción
      "InterruptedError" si la conexión se interrumpe por una señal,
      el controlador de señal no genera una excepción y el socket está
      bloqueando o tiene un tiempo de espera (consulte el **PEP 475**
      para la razón de ser).

      Availability: not WASI.

   connect_ex(address)

      Like "connect(address)", but return an error indicator instead
      of raising an exception for errors returned by the C-level
      "connect()" call (other problems, such as "host not found," can
      still raise exceptions).  The error indicator is "0" if the
      operation succeeded, otherwise the value of the "errno"
      variable.  This is useful to support, for example, asynchronous
      connects.

      Genera un auditing event "socket.connect" con los argumentos
      "self", "address".

      Availability: not WASI.

   detach()

      Coloque el objeto de socket en estado cerrado sin cerrar
      realmente el descriptor de archivo subyacente.  Se devuelve el
      descriptor de archivo y se puede reutilizar para otros fines.

      Added in version 3.2.

   dup()

      Duplica el socket.

      El socket recién creado es non-inheritable.

      Distinto en la versión 3.4: El socket ahora no es heredable.

      Availability: not WASI.

   fileno()

      Retorna un archivo descriptor del socket (un entero pequeño), o
      -1 si falla. Esto es útil con "select.select()".

      En Windows el pequeño entero retornado por este método no puede
      ser usado donde un descriptor de un archivo pueda ser usado
      (como una "os.fdopen()"). Unix no tiene esta limitación.

   get_inheritable()

      Obtiene el inheritable flag del descriptor del archivo del
      socket o el controlador del socket: "True" si el socket puede
      ser heredada en procesos secundarios, "False" si falla.

      Added in version 3.4.

   getpeername()

      Return the remote address to which the socket is connected.
      This is useful to find out the port number of a remote IPv4/v6
      socket, for instance. The format of the address returned depends
      on the address family --- see Familias Socket. On some systems
      this function is not supported.

   getsockname()

      Return the socket's own address.  This is useful to find out the
      port number of an IPv4/v6 socket, for instance. The format of
      the address returned depends on the address family --- see
      Familias Socket.

   getsockopt(level, optname[, buflen])

      Return the value of the given socket option (see the Unix man
      page *getsockopt(2)*).  The needed symbolic constants (SO_*
      etc.) are defined in this module.  If *buflen* is absent, an
      integer option is assumed and its integer value is returned by
      the function.  If *buflen* is present, it specifies the maximum
      length of the buffer used to receive the option in, and this
      buffer is returned as a bytes object.  It is up to the caller to
      decode the contents of the buffer (see the optional built-in
      module "struct" for a way to decode C structures encoded as byte
      strings).

      Availability: not WASI.

   getblocking()

      Retorna "True" si el socket está en modo de bloqueo, "False" si
      está en sin bloqueo.

      Esto es equivalente a comprobar "socket.gettimeout() != 0".

      Added in version 3.7.

   gettimeout()

      Retorna el tiempo de espera en segundos (flotante) asociado con
      las operaciones del socket, o "None" si el tiempo de espera no
      es seleccionado. Esto refleja la ultima llamada al
      "setblocking()" o "settimeout()".

   ioctl(control, option)

      El método "ioctl()" es una interfaz limitada para el sistema de
      interfaces WSAIoctl. Por favor refiérase a Win32 documentation
      para mas información.

      En otras plataformas, las funciones genéricas "fcntl.fcntl()" y
      "fcntl.ioctl()" podrían ser usadas; ellas aceptan un objeto
      socket como su primer argumento.

      Actualmente solo el siguiente control de códigos está
      soportados: "SIO_RCVALL", "SIO_KEEPALIVE_VALS", y
      "SIO_LOOPBACK_FAST_PATH".

      Availability: Windows

      Distinto en la versión 3.6: "SIO_LOOPBACK_FAST_PATH" ha sido
      agregado.

   listen([backlog])

      Habilita un servidor para aceptar conexiones. Si *backlog* es
      especifico, debe ser al menos 0 (si es menor, se establece en
      0); especifica el número de conexiones no aceptadas que
      permitirá el sistema antes de rechazar nuevas conexiones. Si no
      se especifica, se elige un valor razonable predeterminado.

      Availability: not WASI.

      Distinto en la versión 3.5: El parámetro *backlog* ahora es
      opcional.

   makefile(mode='r', buffering=None, *, encoding=None, errors=None, newline=None)

      Return a *file object* associated with the socket.  The exact
      returned type depends on the arguments given to "makefile()".
      These arguments are interpreted the same way as by the built-in
      "open()" function, except the only supported *mode* values are
      "'r'" (default), "'w'", "'b'", or a combination of those.

      El socket debe estar en modo de bloqueo; puede tener un tiempo
      de espera, pero el búfer interno del objeto de archivo puede
      terminar en un estado incoherente si se produce un tiempo de
      espera.

      Cerrar el objeto de archivo devuelto por "makefile()" no cerrará
      el socket original a menos que se hayan cerrado todos los demás
      objetos de archivo y "socket.close()" se haya llamado al objeto
      socket.

      Nota:

        En Windows, el objeto similar a un archivo creado por
        "makefile()" no se puede utilizar cuando se espera un objeto
        de archivo con un descriptor de archivo, como los argumentos
        de secuencia de "subprocess.Popen()".

   recv(bufsize[, flags])

      Receive data from the socket.  The return value is a bytes
      object representing the data received.  The maximum amount of
      data to be received at once is specified by *bufsize*. A
      returned empty bytes object indicates that the client has
      disconnected. See the Unix manual page *recv(2)* for the meaning
      of the optional argument *flags*; it defaults to zero.

      Distinto en la versión 3.5: Si se interrumpe la llamada del
      sistema y el controlador de señal no genera una excepción, el
      método ahora vuelve a intentar la llamada del sistema en lugar
      de generar una excepción "InterruptedError" (consulte **PEP
      475** para la lógica).

   recvfrom(bufsize[, flags])

      Receive data from the socket.  The return value is a pair
      "(bytes, address)" where *bytes* is a bytes object representing
      the data received and *address* is the address of the socket
      sending the data.  See the Unix manual page *recv(2)* for the
      meaning of the optional argument *flags*; it defaults to zero.
      The format of *address* depends on the address family --- see
      Familias Socket.

      Distinto en la versión 3.5: Si se interrumpe la llamada del
      sistema y el controlador de señal no genera una excepción, el
      método ahora vuelve a intentar la llamada del sistema en lugar
      de generar una excepción "InterruptedError" (consulte **PEP
      475** para la lógica).

      Distinto en la versión 3.7: Para direcciones IPv6 de
      multidifusión, el primer elemento de *address* ya no contiene la
      parte "%scope_id". Para obtener la dirección IPV6 completa, use
      "getnameinfo()".

   recvmsg(bufsize[, ancbufsize[, flags]])

      Reciba datos normales (hasta *bufsize* bytes) y datos auxiliares
      del socket.  El argumento *ancbufsize* establece el tamaño en
      bytes del búfer interno utilizado para recibir los datos
      auxiliares; el valor predeterminado es 0, lo que significa que
      no se recibirán datos auxiliares.  Los tamaños de búfer
      adecuados para los datos auxiliares se pueden calcular mediante
      "CMSG_SPACE()" o "CMSG_LEN()", y los elementos que no caben en
      el búfer pueden truncarse o descartarse.  El valor
      predeterminado del argumento *flags* es 0 y tiene el mismo
      significado que para "recv()".

      El valor de retorno es una tupla de 4: "(data, ancdata,
      msg_flags, address)". El valor *data* es un objeto "bytes" que
      contiene los datos no auxiliares recibidos. El valor *ancdata*
      es una lista de cero o mas tuplas "(cmsg_level, cmsg_type,
      cmsg_data)" representado los datos auxiliares (control de
      mensajes) recibidos: *cmsg_level* y *cmsg_type* son enteros
      especificando el nivel de protocolo y tipo específico de
      protocolo respectivamente, y *cmsg_data* es un objeto "bytes"
      sosteniendo los datos asociados. El valor *msg_flags* es el OR
      bit a bit de varios indicadores que indican condiciones en el
      mensaje recibido; consulte la documentación de su sistema para
      obtener más detalles. Si la toma de recepción no está conectada,
      *address* es la dirección de el socket enviado, si está
      disponible; de lo contrario, su valor no se especifica.

      En algunos sistemas, "sendmsg()" y "recvmsg()" pueden utilizarse
      para pasar descriptores de fichero entre procesos a través de un
      socket "AF_UNIX".  Cuando se utiliza esta funcionalidad (a
      menudo está restringida a los sockets "SOCK_STREAM"),
      "recvmsg()" devolverá, en sus datos auxiliares, elementos del
      formulario "(socket.SOL_SOCKET, socket.SCM_RIGHTS, fds)", donde
      *fds* es un objeto "bytes" que representa los nuevos
      descriptores de archivo como una arreglo binario del tipo nativo
      C int.  Si "recvmsg()" lanza una excepción después del retorno
      de la llamada al sistema, primero intentará cerrar cualquier
      descriptor de fichero recibido a través de este mecanismo.

      Algunos sistemas no indican la longitud truncada de los
      elementos de datos auxiliares que solo se han recibido
      parcialmente.  Si un elemento parece extenderse más allá del
      final del búfer, "recvmsg()" emitirá un "RuntimeWarning", y
      devolverá la parte de él que está dentro del búfer siempre que
      no se haya truncado antes del inicio de sus datos asociados.

      On systems which support the "SCM_RIGHTS" mechanism, the
      following function will receive up to *maxfds* file descriptors,
      returning the message data and a list containing the descriptors
      (while ignoring unexpected conditions such as unrelated control
      messages being received).  See also "sendmsg()".

         import socket, array

         def recv_fds(sock, msglen, maxfds):
             fds = array.array("i")   # Array of ints
             msg, ancdata, flags, addr = sock.recvmsg(msglen, socket.CMSG_LEN(maxfds * fds.itemsize))
             for cmsg_level, cmsg_type, cmsg_data in ancdata:
                 if cmsg_level == socket.SOL_SOCKET and cmsg_type == socket.SCM_RIGHTS:
                     # Append data, ignoring any truncated integers at the end.
                     fds.frombytes(cmsg_data[:len(cmsg_data) - (len(cmsg_data) % fds.itemsize)])
             return msg, list(fds)

      Availability: Unix.

      La mayoría de las plataformas Unix.

      Added in version 3.3.

      Distinto en la versión 3.5: Si se interrumpe la llamada del
      sistema y el controlador de señal no genera una excepción, el
      método ahora vuelve a intentar la llamada del sistema en lugar
      de generar una excepción "InterruptedError" (consulte **PEP
      475** para la lógica).

   recvmsg_into(buffers[, ancbufsize[, flags]])

      Recibir datos normales y datos auxiliares desde el socket,
      comportándose como "recvmsg()" lo haría, pero dispersar los
      datos no auxiliares en una serie de buffers en lugar de devolver
      un nuevo objeto bytes.  El argumento *buffers* debe ser un
      iterable de objetos que exportan buffers de escritura (por
      ejemplo, objetos "bytearray"); estos se llenarán con fragmentos
      sucesivos de los datos no auxiliares hasta que se hayan escrito
      todos o no haya más buffers.  El sistema operativo puede
      establecer un límite ("sysconf()" valor "SC_IOV_MAX") en el
      número de buffers que se pueden utilizar.  Los argumentos
      *ancbufsize* y *flags* tienen el mismo significado que para
      "recvmsg()".

      El valor de retorno es tupla de 4: "(nbytes, ancdata, msg_flags,
      address)", donde *nbytes* es el numero total de bytes de datos
      no auxiliares escrito dentro de los bufetes, y *ancdata*,
      *msg_flags* y *address* son lo mismo que para "recvmsg()".

      Ejemplo:

         >>> import socket
         >>> s1, s2 = socket.socketpair()
         >>> b1 = bytearray(b'----')
         >>> b2 = bytearray(b'0123456789')
         >>> b3 = bytearray(b'--------------')
         >>> s1.send(b'Mary had a little lamb')
         22
         >>> s2.recvmsg_into([b1, memoryview(b2)[2:9], b3])
         (22, [], 0, None)
         >>> [b1, b2, b3]
         [bytearray(b'Mary'), bytearray(b'01 had a 9'), bytearray(b'little lamb---')]

      Availability: Unix.

      La mayoría de las plataformas Unix.

      Added in version 3.3.

   recvfrom_into(buffer[, nbytes[, flags]])

      Receive data from the socket, writing it into *buffer* instead
      of creating a new bytestring.  The return value is a pair
      "(nbytes, address)" where *nbytes* is the number of bytes
      received and *address* is the address of the socket sending the
      data.  See the Unix manual page *recv(2)* for the meaning of the
      optional argument *flags*; it defaults to zero. The format of
      *address* depends on the address family --- see Familias Socket.

   recv_into(buffer[, nbytes[, flags]])

      Recibe hasta *nbytes* bytes desde el socket, almacenado los
      datos en un búfer en lugar de crear una nueva cadena de bytes.
      Si *nbytes* no esta especificado (o 0), recibir hasta el tamaño
      disponible en el búfer dado. Retorna  el número de bytes
      recibidos. Ver la página del manual de Unix *recv(2)* para el
      significado del argumento opcional *flags*; por defecto es cero.

   send(bytes[, flags])

      Send data to the socket.  The socket must be connected to a
      remote socket.  The optional *flags* argument has the same
      meaning as for "recv()". Returns the number of bytes sent.
      Applications are responsible for checking that all data has been
      sent; if only some of the data was transmitted, the application
      needs to attempt delivery of the remaining data. For further
      information on this topic, consult the HOW TO - Programación con
      sockets.

      Distinto en la versión 3.5: Si se interrumpe la llamada del
      sistema y el controlador de señal no genera una excepción, el
      método ahora vuelve a intentar la llamada del sistema en lugar
      de generar una excepción "InterruptedError" (consulte **PEP
      475** para la lógica).

   sendall(bytes[, flags])

      Send data to the socket.  The socket must be connected to a
      remote socket.  The optional *flags* argument has the same
      meaning as for "recv()". Unlike "send()", this method continues
      to send data from *bytes* until either all data has been sent or
      an error occurs.  "None" is returned on success.  On error, an
      exception is raised, and there is no way to determine how much
      data, if any, was successfully sent.

      Distinto en la versión 3.5: El tiempo de espera del socket ya no
      se restablece cada vez que los datos se envían correctamente. El
      tiempo de espera del socket es ahora la duración total máxima
      para enviar todos los datos.

      Distinto en la versión 3.5: Si se interrumpe la llamada del
      sistema y el controlador de señal no genera una excepción, el
      método ahora vuelve a intentar la llamada del sistema en lugar
      de generar una excepción "InterruptedError" (consulte **PEP
      475** para la lógica).

   sendto(bytes, address)
   sendto(bytes, flags, address)

      Send data to the socket.  The socket should not be connected to
      a remote socket, since the destination socket is specified by
      *address*.  The optional *flags* argument has the same meaning
      as for "recv()".  Return the number of bytes sent. The format of
      *address* depends on the address family --- see Familias Socket.

      Genera un auditing event "socket.sendto" con los argumentos
      "self", "address".

      Distinto en la versión 3.5: Si se interrumpe la llamada del
      sistema y el controlador de señal no genera una excepción, el
      método ahora vuelve a intentar la llamada del sistema en lugar
      de generar una excepción "InterruptedError" (consulte **PEP
      475** para la lógica).

   sendmsg(buffers[, ancdata[, flags[, address]]])

      Enviar datos normales y auxiliares al socket, recopilar los
      datos no auxiliares de una serie de buffers y concatenando en un
      único mensaje.  El argumento *buffers* especifica los datos no
      auxiliares como un iterable de *bytes-como objetos* (por
      ejemplo: objetos "bytes"); el sistema operativo puede establecer
      un límite ("os.sysconf()" valor "SC_IOV_MAX") en el número de
      buffers que se pueden utilizar.  El argumento *ancdata*
      especifica los datos auxiliares (mensajes de control) como un
      iterable de cero o más tuplas "(cmsg_level, cmsg_type,
      cmsg_data)", donde *cmsg_level* y *cmsg_type* son enteros que
      especifican el nivel de protocolo y el tipo específico del
      protocolo respectivamente, y *cmsg_data* es un objeto similar a
      bytes que contiene los datos asociados.  Tenga en cuenta que
      algunos sistemas (en particular, sistemas sin "CMSG_SPACE()")
      pueden admitir el envío de solo un mensaje de control por
      llamada.  El valor predeterminado del argumento *flags* es 0 y
      tiene el mismo significado que para "send()".  Si se proporciona
      *address* y no "None", establece una dirección de destino para
      el mensaje.  El valor devuelto es el número de bytes de datos no
      auxiliares enviados.

      The following function sends the list of file descriptors *fds*
      over an "AF_UNIX" socket, on systems which support the
      "SCM_RIGHTS" mechanism.  See also "recvmsg()".

         import socket, array

         def send_fds(sock, msg, fds):
             return sock.sendmsg([msg], [(socket.SOL_SOCKET, socket.SCM_RIGHTS, array.array("i", fds))])

      Availability: Unix, not WASI.

      La mayoría de las plataformas Unix.

      Genera un auditing event "socket.sendmsg" con los argumentos
      "self", "address".

      Added in version 3.3.

      Distinto en la versión 3.5: Si se interrumpe la llamada del
      sistema y el controlador de señal no genera una excepción, el
      método ahora vuelve a intentar la llamada del sistema en lugar
      de generar una excepción "InterruptedError" (consulte **PEP
      475** para la lógica).

   sendmsg_afalg([msg, ]*, op[, iv[, assoclen[, flags]]])

      Versión especializada de "sendmsg()" para el socket "AF_ALG".
      Modo de ajuste, IV, longitud de datos asociados a AEAD y
      banderas para el socket "AF_ALG".

      Availability: Linux >= 2.6.38.

      Added in version 3.6.

   sendfile(file, offset=0, count=None)

      Enviar un archivo hasta que se alcance EOF mediante el uso de
      alto rendimiento "os.sendfile" y devolver el número total de
      bytes que se enviaron. *file* debe ser un objeto de archivo
      normal abierto en modo binario. Si "os.sendfile" no está
      disponible (por ejemplo, Windows) o *file* no es un archivo
      normal "send()" se utilizará en su lugar. *offset* indica desde
      dónde empezar a leer el archivo. Si se especifica, *count* es el
      número total de bytes para transmitir en lugar de enviar el
      archivo hasta que se alcance EOF. La posición del archivo se
      actualiza a la vuelta o también en caso de error en cuyo caso
      "file.tell()" se puede utilizar para averiguar el número de
      bytes que se enviaron. El socket debe ser de tipo "SOCK_STREAM"
      No se admiten sockets sin bloqueo.

      Added in version 3.5.

   set_inheritable(inheritable)

      Selecciona el inheritable flag descriptor del archivo del socket
      o el controlador del socket.

      Added in version 3.4.

   setblocking(flag)

      Establecer el modo de bloqueo o no bloqueo del socket: si *flag*
      es false, el socket se establece en modo sin bloqueo, de lo
      contrario en modo de bloqueo.

      El método es una abreviatura para ciertas llamadas
      "settimeout()":

      * "sock.setblocking(True)" es equivalente a
        "sock.settimeout(None)"

      * "sock.setblocking(False)" es equivalente a
        "sock.settimeout(0.0)"

      Distinto en la versión 3.7: El método ya no aplica la bandera
      "SOCK_NONBLOCK" en "socket.type".

   settimeout(value)

      Set a timeout on blocking socket operations.  The *value*
      argument can be a nonnegative real number expressing seconds, or
      "None". If a non-zero value is given, subsequent socket
      operations will raise a "timeout" exception if the timeout
      period *value* has elapsed before the operation has completed.
      If zero is given, the socket is put in non-blocking mode. If
      "None" is given, the socket is put in blocking mode.

      Para obtener más información, consulte las notas notas sobre los
      tiempos de espera del socket.

      Distinto en la versión 3.7: El método ya no cambia la bandera
      "SOCK_NONBLOCK" en  "socket.type".

   setsockopt(level, optname, value: int | Buffer)
   setsockopt(level, optname, None, optlen: int)

      Set the value of the given socket option (see the Unix manual
      page *setsockopt(2)*).  The needed symbolic constants are
      defined in this module (*SO_* etc. <socket-unix-constants>*).
      The value can be an integer, "None" or a *bytes-like object*
      representing a buffer. In the latter case it is up to the caller
      to ensure that the bytestring contains the proper bits (see the
      optional built-in module "struct" for a way to encode C
      structures as bytestrings). When *value* is set to "None",
      *optlen* argument is required. It's equivalent to calling
      "setsockopt()" C function with "optval=NULL" and
      "optlen=optlen".

      Distinto en la versión 3.5: Ahora se acepta la grabación *bytes-
      like object*.

      Distinto en la versión 3.6: setsockopt(level, optname, None,
      optlen: int) form added.

      Availability: not WASI.

   shutdown(how)

      Apague una o ambas mitades de la conexión. Si *how* es
      "SHUT_RD", más recibe no se permiten. Si *how* es  "SHUT_WR",
      mas recibe no se permiten. Si *how* es "SHUT_RDWR", más recibe
      no se permiten.

      Availability: not WASI.

   share(process_id)

      Duplica un socket y lo prepara para compartirlo con el proceso
      de destino. El proceso de destino debe estar provisto de
      *process_id*. el objeto de bytes resultante luego se puede pasar
      al proceso de destino usando alguna forma de comunicación entre
      procesos y el socket se puede recrear allí usando
      "fromshare()". Una vez que se ha llamado a este método, es
      seguro cerrar el socket ya que el sistema operativo ya lo ha
      duplicado para el proceso de destino.

      Availability: Windows.

      Added in version 3.3.

   Note that there are no methods "read()" or "write()"; use "recv()"
   and "send()" without *flags* argument instead.

   Los objetos de socket también tienen estos atributos (de solo
   lectura) que corresponden a los valores dados al constructor
   "socket".

   family

      La familia socket.

   type

      El tipo de socket.

   proto

      The socket protocol.

class socket.SocketType

   The base class of the "socket" type, re-exported from "_socket".
   An instance check such as "isinstance(socket(...), SocketType)" is
   true, but "SocketType" is not the same as "type(socket(...))",
   which is "socket" itself.

## Notas sobre los tiempos de espera del socket

Un objeto de socket puede estar en uno de los tres modos: bloqueo, no
bloqueo o tiempo de espera.  Los sockets se crean de forma
predeterminada siempre en modo de bloqueo, pero esto se puede cambiar
llamando a "setdefaulttimeout()".

* En el modo *bloqueo*, las operaciones se bloquean hasta que se
  completan o el sistema devuelve un error (como tiempo de espera de
  conexión agotado).

* En *modo sin bloqueo*, las operaciones fallan (con un error que
  desafortunadamente depende del sistema) si no se pueden completar
  inmediatamente: las funciones del módulo "select" se pueden usar
  para saber cuándo y si un socket está disponible para leer o
  escribir.

* En *timeout mode*, las operaciones fallan si no se puede completan
  el tiempo de espera especifico para el socket (ellos lanzan una
  excepción "timeout") o si el sistema devuelve un error.

Nota:

  At the operating system level, sockets in *timeout mode* are
  internally set in non-blocking mode.  Also, the blocking and timeout
  modes are shared between file descriptors and socket objects that
  refer to the same network endpoint. This implementation detail can
  have visible consequences if e.g. you decide to use the "fileno()"
  of a socket.

### Tiempos de espera y el método "connect"

La operación "connect()" también está sujeta a la configuración de
tiempo de espera, y en general se recomienda llamar a "settimeout()"
antes de llamar a "connect()" o pasar un parámetro de tiempo de espera
a "create_connection()".  Sin embargo, la pila de red del sistema
también puede devolver un error de tiempo de espera de conexión propio
independientemente de cualquier configuración de tiempo de espera del
socket de Python.

### Tiempos de espera y el método "accept"

Si "getdefaulttimeout()" no es una "None", los sockets devuelto por el
método "accept()" heredan ese tiempo de espera. De lo contrario, el
comportamiento depende de la configuración de la toma de escucha:

* si los sockets están escuchando en *blocking mode* o en el *timeout
  mode*, el socket devuelve el "accept()" en un *blocking mode*;

* si los sockets están escuchando en *non-blocking mode*, ya sea el
  socket devuelto por "accept()" es un modo de bloqueo o no bloque
  depende del sistema operativo. Si desea garantizar un comportamiento
  multiplataforma, se recomienda que se anule manualmente esta
  configuración.

## Ejemplo

Here are four minimal example programs using the TCP/IP protocol: a
server that echoes all data that it receives back (servicing only one
client), and a client using it.  Note that a server must perform the
sequence "socket()", "bind()", "listen()", "accept()" (possibly
repeating the "accept()" to service more than one client), while a
client only needs the sequence "socket()", "connect()".  Also note
that the server does not "sendall()"/"recv()" on the socket it is
listening on but on the new socket returned by "accept()".

Los dos primeros ejemplos solo admiten IPv4.

   # Echo server program
   import socket

   HOST = ''                 # Symbolic name meaning all available interfaces
   PORT = 50007              # Arbitrary non-privileged port
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
       s.bind((HOST, PORT))
       s.listen(1)
       conn, addr = s.accept()
       with conn:
           print('Connected by', addr)
           while True:
               data = conn.recv(1024)
               if not data: break
               conn.sendall(data)

   # Echo client program
   import socket

   HOST = 'daring.cwi.nl'    # The remote host
   PORT = 50007              # The same port as used by the server
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
       s.connect((HOST, PORT))
       s.sendall(b'Hello, world')
       data = s.recv(1024)
   print('Received', repr(data))

The next two examples are identical to the above two, but support both
IPv4 and IPv6. The server side will listen to the first address family
available (it should listen to both instead). On most of IPv6-ready
systems, IPv6 will take precedence and the server may not accept IPv4
traffic. The client side will try to connect to all the addresses
returned as a result of the name resolution, and sends traffic to the
first one connected successfully.

   # Echo server program
   import socket
   import sys

   HOST = None               # Symbolic name meaning all available interfaces
   PORT = 50007              # Arbitrary non-privileged port
   s = None
   for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC,
                                 socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
       af, socktype, proto, canonname, sa = res
       try:
           s = socket.socket(af, socktype, proto)
       except OSError as msg:
           s = None
           continue
       try:
           s.bind(sa)
           s.listen(1)
       except OSError as msg:
           s.close()
           s = None
           continue
       break
   if s is None:
       print('could not open socket')
       sys.exit(1)
   conn, addr = s.accept()
   with conn:
       print('Connected by', addr)
       while True:
           data = conn.recv(1024)
           if not data: break
           conn.send(data)

   # Echo client program
   import socket
   import sys

   HOST = 'daring.cwi.nl'    # The remote host
   PORT = 50007              # The same port as used by the server
   s = None
   for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
       af, socktype, proto, canonname, sa = res
       try:
           s = socket.socket(af, socktype, proto)
       except OSError as msg:
           s = None
           continue
       try:
           s.connect(sa)
       except OSError as msg:
           s.close()
           s = None
           continue
       break
   if s is None:
       print('could not open socket')
       sys.exit(1)
   with s:
       s.sendall(b'Hello, world')
       data = s.recv(1024)
   print('Received', repr(data))

El siguiente ejemplo muestra cómo escribir un rastreador de red muy
simple con sockets sin procesar en Windows. El ejemplo requiere
privilegios de administrador para modificar la interfaz:

   import socket

   # the public network interface
   HOST = socket.gethostbyname(socket.gethostname())

   # create a raw socket and bind it to the public interface
   s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
   s.bind((HOST, 0))

   # Include IP headers
   s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

   # receive all packets
   s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

   # receive a packet
   print(s.recvfrom(65565))

   # disabled promiscuous mode
   s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

En el ejemplo siguiente se muestra cómo utilizar la interfaz de socket
para comunicarse con una red CAN mediante el protocolo de socket sin
procesar. Para utilizar CAN con el protocolo de gestor de difusión en
su lugar, abra un socket con:

   socket.socket(socket.AF_CAN, socket.SOCK_DGRAM, socket.CAN_BCM)

Después de vincular ("CAN_RAW") o conectar ("CAN_BCM") el socket,
puede usar las operaciones "socket.send()" y "socket.recv()" (y sus
contrapartes) en el objeto socket como de costumbre.

Este último ejemplo puede requerir privilegios especiales:

   import socket
   import struct

   # CAN frame packing/unpacking (see 'struct can_frame' in <linux/can.h>)

   can_frame_fmt = "=IB3x8s"
   can_frame_size = struct.calcsize(can_frame_fmt)

   def build_can_frame(can_id, data):
       can_dlc = len(data)
       data = data.ljust(8, b'\x00')
       return struct.pack(can_frame_fmt, can_id, can_dlc, data)

   def dissect_can_frame(frame):
       can_id, can_dlc, data = struct.unpack(can_frame_fmt, frame)
       return (can_id, can_dlc, data[:can_dlc])

   # create a raw socket and bind it to the 'vcan0' interface
   s = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
   s.bind(('vcan0',))

   while True:
       cf, addr = s.recvfrom(can_frame_size)

       print('Received: can_id=%x, can_dlc=%x, data=%s' % dissect_can_frame(cf))

       try:
           s.send(cf)
       except OSError:
           print('Error sending CAN frame')

       try:
           s.send(build_can_frame(0x01, b'\x01\x02\x03'))
       except OSError:
           print('Error sending CAN frame')

Ejecutar un ejemplo varias veces con un retraso demasiado pequeño
entre ejecuciones, podría dar lugar a este error:

   OSError: [Errno 98] Address already in use

Esto se debe a que la ejecución anterior ha dejado el socket en un
estado "TIME_WAIT" y no se puede reutilizar inmediatamente.

There is a "socket" flag to set, in order to prevent this,
"socket.SO_REUSEADDR":

   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   s.bind((HOST, PORT))

el indicador "SO_REUSEADDR" indica al kernel que reutilice un socket
local en estado "TIME_WAIT", sin esperar a que expire su tiempo de
espera natural.

Ver también:

  Para obtener una introducción a la programación de sockets (en C),
  consulte los siguientes documentos:

  * *An Introductory 4.3BSD Interprocess Communication Tutorial*, por
    Stuart Sechrest

  * *An Advanced 4.3BSD Interprocess Communication Tutorial*, por
    Samuel J.  Leffler et al,

  ambos en el manual del programador de Unix, documentos
  suplementarios 1 ( secciones  PS1:7 y PS1:8). La plataforma
  especifica material de referencia para las diversas llamadas al
  sistema también son una valiosa fuente de información en los
  detalles de la semántica del socket. Para Unix, referencia a las
  paginas del manual, para Windows, observa la especificación WinSock
  (o WinSock 2). Para APIS listas IPV6, los lectores pueden querer
  referirse al titulado Extensiones básicas de interfaz de socket para
  IPv6 **RFC 3493** .
