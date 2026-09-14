---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/sockets.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: false
translation_revision: 890cc22d3
order: 75490
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`AF_UNIX` (`int`)  
Familia de direcciones de socket de rutas de archivos del sistema en el Dominio Unix.

`AF_INET` (`int`)  
Familia de direcciones de socket de IPv4 en el Dominio de Internet.

`AF_INET6` (`int`)  
Familia de direcciones de socket de IPv6 en el Dominio de Internet. Solo disponible si se compila con soporte para IPv6.

`AF_DIVERT` (`int`)  
Familia de direcciones de socket para la interfaz `divert(4)` de FreeBSD, usada para recibir paquetes desviados por el cortafuegos. Disponible a partir de PHP 8.3.0 (solo FreeBSD).

`AF_PACKET` (`int`)  
Familia de direcciones de socket para sockets de paquetes de bajo nivel, usada para enviar y recibir paquetes en bruto a nivel del controlador del dispositivo (capa 2 del modelo OSI). Disponible a partir de PHP 8.5.0 (solo Linux).

`SOCK_STREAM` (`int`)  

`SOCK_DGRAM` (`int`)  

`SOCK_RAW` (`int`)  

`SOCK_SEQPACKET` (`int`)  

`SOCK_RDM` (`int`)  

`SOCK_CONN_DGRAM` (`int`)  
Establece el socket como un datagrama orientado a conexión. Disponible a partir de PHP 8.4.0. (solo NetBSD)

`SOCK_DCCP` (`int`)  
Establece el socket como un protocolo de control de congestión de datagramas. Disponible a partir de PHP 8.4.0. (solo NetBSD)

`SOCK_NONBLOCK` (`int`)  
Establece la bandera de estado de socket no bloqueante. Disponible a partir de PHP 8.4.0.

`SOCK_CLOEXEC` (`int`)  
Establece la bandera de estado de socket close-on-exec. Disponible a partir de PHP 8.4.0.

`MSG_OOB` (`int`)  

`MSG_WAITALL` (`int`)  

`MSG_PEEK` (`int`)  

`MSG_DONTROUTE` (`int`)  

`MSG_EOR` (`int`)  
No disponible en plataformas Windows.

`MSG_EOF` (`int`)  
No disponible en plataformas Windows.

`MSG_ZEROCOPY` (`int`)  
Disponible a partir de PHP 8.2.0

`SO_DEBUG` (`int`)  

`SO_REUSEADDR` (`int`)  

`SO_REUSEPORT` (`int`)  
Esta constante solo está disponible en plataformas que soportan la opción de socket `SO_REUSEPORT`: esto incluye Linux, macOS y \*BSD, pero no incluye Windows.

`SO_KEEPALIVE` (`int`)  

`SO_DONTROUTE` (`int`)  

`SO_LINGER` (`int`)  

`SO_BROADCAST` (`int`)  

`SO_OOBINLINE` (`int`)  

`SO_SNDBUF` (`int`)  

`SO_RCVBUF` (`int`)  

`SO_SNDLOWAT` (`int`)  

`SO_RCVLOWAT` (`int`)  

`SO_SNDTIMEO` (`int`)  

`SO_RCVTIMEO` (`int`)  

`SO_TYPE` (`int`)  

`SO_ERROR` (`int`)  

`SO_ZEROCOPY` (`int`)  
Disponible a partir de PHP 8.2.0

`TCP_NODELAY` (`int`)  
Usado para deshabilitar el algoritmo TCP de Nagle.

`TCP_KEEPCNT` (`int`)  
Disponible a partir de PHP 8.2.0

`TCP_KEEPIDLE` (`int`)  
Disponible a partir de PHP 8.2.0

`TCP_KEEPINTVL` (`int`)  
Disponible a partir de PHP 8.2.0

`TCP_KEEPALIVE` (`int`)  
Disponible a partir de PHP 8.2.0

`TCP_NOTSENT_LOWAT` (`int`)  
Disponible a partir de PHP 8.2.0

`SO_MARK` (`int`)  
Disponible a partir de PHP 8.1.0

`SO_USER_COOKIE` (`int`)  
Disponible a partir de PHP 8.1.0

`SO_RTABLE` (`int`)  
Disponible a partir de PHP 8.2.0

`SO_ACCEPTFILTER` (`int`)  
Disponible a partir de PHP 8.1.0

`SO_DONTTRUNC` (`int`)  
Disponible a partir de PHP 8.1.0

`SO_WANTMORE` (`int`)  
Disponible a partir de PHP 8.1.0

`SO_INCOMING_CPU` (`int`)  
Disponible a partir de PHP 8.2.0

`SO_MEMINFO` (`int`)  
Disponible a partir de PHP 8.2.0

`SO_BPF_EXTENSIONS` (`int`)  
Disponible a partir de PHP 8.2.0

`SO_SETFIB` (`int`)  
Disponible a partir de PHP 8.2.0

`SO_ATTACH_REUSEPORT_CBPF` (`int`)  
Disponible a partir de PHP 8.3.0 (solo Linux)

`SO_DETACH_BPF` (`int`)  
Disponible a partir de PHP 8.3.0 (solo Linux)

`SO_DETACH_FILTER` (`int`)  
Disponible a partir de PHP 8.3.0 (solo Linux)

`SO_RERROR` (`int`)  
Disponible a partir de PHP 8.3.0 (solo NetBSD)

`SO_ZEROIZE` (`int`)  
Disponible a partir de PHP 8.3.0 (solo OpenBSD)

`SO_SPLICE` (`int`)  
Disponible a partir de PHP 8.3.0 (solo OpenBSD)

`SO_REUSEPORT_LB` (`int`)  
Disponible a partir de PHP 8.3.0 (solo FreeBSD)

`SOL_FILTER` (`int`)  
Disponible a partir de PHP 8.2.0

`SOL_UDPLITE` (`int`)  
Disponible a partir de PHP 8.3.0

`UDPLITE_RECV_CSCOV` (`int`)  
Disponible a partir de PHP 8.3.0

`UDPLITE_SEND_CSCOV` (`int`)  
Disponible a partir de PHP 8.3.0

`TCP_DEFER_ACCEPT` (`int`)  
Disponible a partir de PHP 8.1.0

`TCP_CONGESTION` (`int`)  
Disponible a partir de PHP 8.2.0

`TCP_QUICKACK` (`int`)  
Disponible a partir de PHP 8.3.0 (solo Linux)

`TCP_REPAIR` (`int`)  
Disponible a partir de PHP 8.3.0 (solo Linux)

`TCP_SYNCNT` (`int`)  
Establece el número de retransmisiones SYN que TCP debe enviar antes de abortar el intento de conexión. Disponible a partir de PHP 8.4.0 (solo Linux)

`IP_DONTFRAG` (`int`)  
Disponible a partir de PHP 8.3.0 (solo FreeBSD)

`IP_MTU_DISCOVER` (`int`)  
Disponible a partir de PHP 8.3.0 (solo Linux)

`IP_PMTUDISC_DO` (`int`)  
Disponible a partir de PHP 8.3.0 (solo Linux)

`IP_PMTUDISC_DONT` (`int`)  
Disponible a partir de PHP 8.3.0 (solo Linux)

`IP_PMTUDISC_WANT` (`int`)  
Disponible a partir de PHP 8.3.0 (solo Linux)

`IP_PMTUDISC_PROBE` (`int`)  
Disponible a partir de PHP 8.3.0 (solo Linux)

`IP_PMTUDISC_INTERFACE` (`int`)  
Disponible a partir de PHP 8.3.0 (solo Linux)

`IP_PMTUDISC_OMIT` (`int`)  
Disponible a partir de PHP 8.3.0 (solo Linux)

`IP_BIND_ADDRESS_NO_PORT` (`int`)  
Disponible a partir de PHP 8.3.0 (solo Linux)

`SOL_SOCKET` (`int`)  

`PHP_NORMAL_READ` (`int`)  

`PHP_BINARY_READ` (`int`)  

`SOL_TCP` (`int`)  

`SOL_UDP` (`int`)  

Las siguientes constantes están definidas bajo plataformas Windows y UNIX-like. Cada constante solo está definida si su equivalente está disponible en la plataforma.

`SOCKET_EINTR` (`int`)  
Llamada al sistema interrumpida.

`SOCKET_EBADF` (`int`)  
Número de descriptor de archivo inválido.

`SOCKET_EACCES` (`int`)  
Permiso denegado.

`SOCKET_EFAULT` (`int`)  
Dirección inválida.

`SOCKET_EINVAL` (`int`)  
Argumento inválido.

`SOCKET_EMFILE` (`int`)  
Demasiados archivos abiertos.

`SOCKET_ENAMETOOLONG` (`int`)  
Nombre de archivo demasiado largo.

`SOCKET_ENOTEMPTY` (`int`)  
Directorio no vacío.

`SOCKET_ELOOP` (`int`)  
Demasiados enlaces simbólicos encontrados.

`SOCKET_EWOULDBLOCK` (`int`)  
La operación bloquearía.

`SOCKET_EREMOTE` (`int`)  
El objeto es remoto.

`SOCKET_EUSERS` (`int`)  
Demasiados usuarios.

`SOCKET_ENOTSOCK` (`int`)  
Operación de socket en un no-socket.

`SOCKET_EDESTADDRREQ` (`int`)  
Dirección de destino requerida.

`SOCKET_EMSGSIZE` (`int`)  
Mensaje demasiado largo.

`SOCKET_EPROTOTYPE` (`int`)  
Tipo de protocolo incorrecto para el socket.

`SOCKET_EPROTONOSUPPORT` (`int`)  
Protocolo no soportado.

`SOCKET_ESOCKTNOSUPPORT` (`int`)  
Tipo de socket no soportado.

`SOCKET_EOPNOTSUPP` (`int`)  
Operación no soportada en el punto final de transporte.

`SOCKET_EPFNOSUPPORT` (`int`)  
Familia de protocolos no soportada.

`SOCKET_EAFNOSUPPORT` (`int`)  
Familia de direcciones no soportada por el protocolo.

`SOCKET_EADDRNOTAVAIL` (`int`)  
No se puede asignar la dirección solicitada.

`SOCKET_ENETDOWN` (`int`)  
La red está inactiva.

`SOCKET_ENETUNREACH` (`int`)  
La red no es accesible.

`SOCKET_ENETRESET` (`int`)  
La red interrumpió la conexión debido a un reinicio.

`SOCKET_ECONNABORTED` (`int`)  
El software causó el aborto de la conexión.

`SOCKET_ECONNRESET` (`int`)  
La conexión fue reiniciada por el otro extremo.

`SOCKET_ENOBUFS` (`int`)  
No hay espacio en el búfer disponible.

`SOCKET_EISCONN` (`int`)  
El punto final de transporte ya está conectado.

`SOCKET_ENOTCONN` (`int`)  
El punto final de transporte no está conectado.

`SOCKET_ESHUTDOWN` (`int`)  
No se puede enviar después del cierre del punto final de transporte.

`SOCKET_ETIMEDOUT` (`int`)  
La conexión expiró.

`SOCKET_ECONNREFUSED` (`int`)  
La conexión fue rechazada.

`SOCKET_EHOSTDOWN` (`int`)  
El host está inactivo.

`SOCKET_EHOSTUNREACH` (`int`)  
No hay ruta al host.

`SOCKET_EALREADY` (`int`)  
La operación ya está en progreso.

`SOCKET_EINPROGRESS` (`int`)  
La red no está disponible.

Las constantes siguientes solo están disponibles en Windows.

`SOCKET_ENOPROTOOPT` (`int`)  

`SOCKET_EADDRINUSE` (`int`)  

`SOCKET_ETOOMYREFS` (`int`)  

`SOCKET_EPROCLIM` (`int`)  

`SOCKET_EDUOT` (`int`)  

`SOCKET_ESTALE` (`int`)  

`SOCKET_EDISCON` (`int`)  

`SOCKET_SYSNOTREADY` (`int`)  

`SOCKET_VERNOTSUPPORTED` (`int`)  

`SOCKET_NOTINITIALISED` (`int`)  

`SOCKET_HOST_NOT_FOUND` (`int`)  

`SOCKET_TRY_AGAIN` (`int`)  

`SOCKET_NO_RECOVERY` (`int`)  

`SOCKET_NO_DATA` (`int`)  

`SOCKET_NO_ADDRESS` (`int`)  

Las siguientes constantes solo están disponibles en plataformas similares a UNIX. Cada constante solo está definida si su equivalente está disponible en la plataforma.

`SOCKET_EPERM` (`int`)  
Operación no permitida.

`SOCKET_ENOENT` (`int`)  
No existe el archivo o directorio.

`SOCKET_EIO` (`int`)  
Error de E/S.

`SOCKET_ENXIO` (`int`)  
No existe el dispositivo o dirección.

`SOCKET_E2BIG` (`int`)  
Lista de argumentos demasiado larga.

`SOCKET_EAGAIN` (`int`)  
Inténtelo de nuevo.

`SOCKET_ENOMEM` (`int`)  
Sin memoria.

`SOCKET_ENOTBLK` (`int`)  
Se requiere un dispositivo de bloque.

`SOCKET_EBUSY` (`int`)  
Dispositivo o recurso ocupado.

`SOCKET_EEXIST` (`int`)  
El archivo existe.

`SOCKET_EXDEV` (`int`)  
Enlace entre dispositivos.

`SOCKET_ENODEV` (`int`)  
No existe el dispositivo.

`SOCKET_ENOTDIR` (`int`)  
No es un directorio.

`SOCKET_EISDIR` (`int`)  
Es un directorio.

`SOCKET_ENFILE` (`int`)  
Desbordamiento de la tabla de archivos.

`SOCKET_ENOTTY` (`int`)  
No es un terminal.

`SOCKET_ENOSPC` (`int`)  
No hay espacio disponible en el dispositivo.

`SOCKET_ESPIPE` (`int`)  
Búsqueda ilegal.

`SOCKET_EROFS` (`int`)  
Sistema de archivos de solo lectura.

`SOCKET_EMLINK` (`int`)  
Demasiados enlaces.

`SOCKET_EPIPE` (`int`)  
Tubo roto.

`SOCKET_ENOLCK` (`int`)  
No hay bloqueos de registros disponibles.

`SOCKET_ENOSYS` (`int`)  
Función no implementada.

`SOCKET_ENOMSG` (`int`)  
No hay mensaje del tipo deseado.

`SOCKET_EIDRM` (`int`)  
Identificador eliminado.

`SOCKET_ECHRNG` (`int`)  
Número de canal fuera de rango.

`SOCKET_EL2NSYNC` (`int`)  
Nivel 2 no sincronizado.

`SOCKET_EL3HLT` (`int`)  
Nivel 3 detenido.

`SOCKET_EL3RST` (`int`)  
Nivel 3 reiniciado.

`SOCKET_ELNRNG` (`int`)  
Número de enlace fuera de rango.

`SOCKET_EUNATCH` (`int`)  
Controlador de protocolo no adjunto.

`SOCKET_ENOCSI` (`int`)  
No hay estructura CSI disponible.

`SOCKET_EL2HLT` (`int`)  
Nivel 2 detenido.

`SOCKET_EBADE` (`int`)  
Intercambio inválido.

`SOCKET_EBADR` (`int`)  
Descriptor de solicitud inválido.

`SOCKET_EXFULL` (`int`)  
Intercambio lleno.

`SOCKET_ENOANO` (`int`)  
No hay ánodo.

`SOCKET_EBADRQC` (`int`)  
Código de solicitud inválido.

`SOCKET_EBADSLT` (`int`)  
Ranura inválida.

`SOCKET_ENOSTR` (`int`)  
El dispositivo no es un flujo.

`SOCKET_ENODATA` (`int`)  
No hay datos disponibles.

`SOCKET_ETIME` (`int`)  
El temporizador expiró.

`SOCKET_ENOSR` (`int`)  
Sin recursos de flujo.

`SOCKET_ENONET` (`int`)  
La máquina no está en la red.

`SOCKET_ENOLINK` (`int`)  
El enlace ha sido cortado.

`SOCKET_EADV` (`int`)  
Error de anuncio.

`SOCKET_ESRMNT` (`int`)  
Error de srmount.

`SOCKET_ECOMM` (`int`)  
Error de comunicación al enviar.

`SOCKET_EPROTO` (`int`)  
Error de protocolo.

`SOCKET_EMULTIHOP` (`int`)  
Se intentó un multihop.

`SOCKET_EBADMSG` (`int`)  
No es un mensaje de datos.

`SOCKET_ENOTUNIQ` (`int`)  
El nombre no es único en la red.

`SOCKET_EBADFD` (`int`)  
El descriptor de archivo está en mal estado.

`SOCKET_EREMCHG` (`int`)  
La dirección remota cambió.

`SOCKET_ERESTART` (`int`)  
La llamada al sistema interrumpida debe reiniciarse.

`SOCKET_ESTRPIPE` (`int`)  
Error de tubería de flujos.

`SOCKET_EPROTOOPT` (`int`)  
Protocolo no disponible.

`SOCKET_ADDRINUSE` (`int`)  
La dirección ya está en uso.

`SOCKET_ETOOMANYREFS` (`int`)  
Demasiadas referencias: no se puede insertar.

`SOCKET_EISNAM` (`int`)  
Es un archivo de tipo nombrado.

`SOCKET_EREMOTEIO` (`int`)  
Error de E/S remoto.

`SOCKET_EDQUOT` (`int`)  
Cuota excedida.

`SOCKET_ENOMEDIUM` (`int`)  
No se encontró medio.

`SOCKET_EMEDIUMTYPE` (`int`)  
Tipo de medio incorrecto.

`SCM_RIGHTS` (`int`)  
Enviar o recibir un conjunto de descriptores de archivo abiertos de otro proceso.

`SCM_CREDENTIALS` (`int`)  

`SCM_CREDS` (`int`)  
Disponible a partir de PHP 8.2.0

`SCM_CREDS2` (`int`)  
Disponible a partir de PHP 8.2.0

`LOCAL_CREDS` (`int`)  
Disponible a partir de PHP 8.2.0

`LOCAL_CREDS_PERSISTENT` (`int`)  
Disponible a partir de PHP 8.2.0

`SKF_AD_OFF` (`int`)  
Disponible a partir de PHP 8.2.0

`SKF_AD_PROTOCOL` (`int`)  
Disponible a partir de PHP 8.2.0

`SKF_AD_PKTTYPE` (`int`)  
Disponible a partir de PHP 8.2.0

`SKF_AD_IFINDEX` (`int`)  
Disponible a partir de PHP 8.2.0

`SKF_AD_NLATTR` (`int`)  
Disponible a partir de PHP 8.2.0

`SKF_AD_NLATTR_NEST` (`int`)  
Disponible a partir de PHP 8.2.0

`SKF_AD_MARK` (`int`)  
Disponible a partir de PHP 8.2.0

`SKF_AD_QUEUE` (`int`)  
Disponible a partir de PHP 8.2.0

`SKF_AD_HATYPE` (`int`)  
Disponible a partir de PHP 8.2.0

`SKF_AD_RXHASH` (`int`)  
Disponible a partir de PHP 8.2.0

`SKF_AD_CPU` (`int`)  
Disponible a partir de PHP 8.2.0

`SKF_AD_ALU_XOR_X` (`int`)  
Disponible a partir de PHP 8.2.0

`SKF_AD_VLAN_TAG` (`int`)  
Disponible a partir de PHP 8.2.0

`SKF_AD_VLAN_TAG_PRESENT` (`int`)  
Disponible a partir de PHP 8.2.0

`SKF_AD_PAY_OFFSET` (`int`)  
Disponible a partir de PHP 8.2.0

`SKF_AD_RANDOM` (`int`)  
Disponible a partir de PHP 8.2.0

`SKF_AD_VLAN_TPID` (`int`)  
Disponible a partir de PHP 8.2.0

`SKF_AD_MAX` (`int`)  
Disponible a partir de PHP 8.2.0

`AI_ADDRCONFIG` (`int`)  

`AI_ALL` (`int`)  

`AI_CANONIDN` (`int`)  

`AI_CANONNAME` (`int`)  

`AI_IDN` (`int`)  

`AI_NUMERICHOST` (`int`)  

`AI_NUMERICSERV` (`int`)  

`AI_PASSIVE` (`int`)  

`AI_V4MAPPED` (`int`)  

`FIL_ATTACH` (`int`)  

`FIL_DETACH` (`int`)  

`IPPROTO_IP` (`int`)  

`IPPROTO_IPV6` (`int`)  

`IPV6_HOPLIMIT` (`int`)  

`IPV6_MULTICAST_HOPS` (`int`)  

`IPV6_MULTICAST_IF` (`int`)  

`IPV6_MULTICAST_LOOP` (`int`)  

`IPV6_PKTINFO` (`int`)  

`IPV6_RECVHOPLIMIT` (`int`)  

`IPV6_RECVPKTINFO` (`int`)  

`IPV6_RECVTCLASS` (`int`)  

`IPV6_TCLASS` (`int`)  

`IPV6_UNICAST_HOPS` (`int`)  

`IPV6_V6ONLY` (`int`)  

`IP_MULTICAST_IF` (`int`)  

`IP_MULTICAST_LOOP` (`int`)  

`IP_MULTICAST_TTL` (`int`)  

`IP_PORTRANGE` (`int`)  
Establece el rango de puertos utilizado para seleccionar un número de puerto local. Disponible a partir de PHP 8.4.0. (Solo FreeBSD/NetBSD/OpenBSD)

`IP_PORTRANGE_DEFAULT` (`int`)  
Usa el rango predeterminado de valores de puerto. Disponible a partir de PHP 8.4.0. (Solo FreeBSD/NetBSD/OpenBSD)

`IP_PORTRANGE_HIGH` (`int`)  
Usa un rango alto de valores de puerto. Disponible a partir de PHP 8.4.0. (Solo FreeBSD/NetBSD/OpenBSD)

`IP_PORTRANGE_LOW` (`int`)  
Usa un rango bajo de valores de puerto. Disponible a partir de PHP 8.4.0. (Solo FreeBSD/NetBSD/OpenBSD)

`MCAST_BLOCK_SOURCE` (`int`)  

`MCAST_JOIN_GROUP` (`int`)  

`MCAST_JOIN_SOURCE_GROUP` (`int`)  

`MCAST_LEAVE_GROUP` (`int`)  

`MCAST_LEAVE_SOURCE_GROUP` (`int`)  

`MCAST_UNBLOCK_SOURCE` (`int`)  

`MSG_CMSG_CLOEXEC` (`int`)  

`MSG_CONFIRM` (`int`)  

`MSG_CTRUNC` (`int`)  

`MSG_DONTWAIT` (`int`)  

`MSG_ERRQUEUE` (`int`)  

`MSG_MORE` (`int`)  

`MSG_NOSIGNAL` (`int`)  

`MSG_TRUNC` (`int`)  

`MSG_WAITFORONE` (`int`)  

`SOL_LOCAL` (`int`)  

`SOMAXCONN` (`int`)  

`SO_BINDTODEVICE` (`int`)  

`SO_FAMILY` (`int`)  

`SO_LABEL` (`int`)  

`SO_LISTENQLEN` (`int`)  

`SO_LISTENQLIMIT` (`int`)  

`SO_PASSCRED` (`int`)  

`SO_PEERLABEL` (`int`)  

`SO_EXCLUSIVEADDRUSE` (`int`)  
Evita que otros sockets se vinculen de forma forzada a la misma dirección y puerto. Disponible a partir de PHP 8.4.0. (Solo Windows)

`SO_EXCLBIND` (`int`)  
Habilita/deshabilita la vinculación exclusiva del socket. Disponible a partir de PHP 8.4.0. (Solo Solaris)

`SO_NOSIGPIPE` (`int`)  
Controla la generación de SIGPIPE para el socket. Disponible a partir de PHP 8.4.0. (Solo macOs y FreeBSD)

`SO_LINGER_SEC` (`int`)  
Similar a `SO_LINGER` pero el tiempo de espera es en segundos en lugar de ticks de tiempo en macOs. Disponible a partir de PHP 8.4.0. (Solo macOs)

`SO_BINDTOIFINDEX` (`int`)  
Vincula un socket a una interfaz de red específica por su índice. Disponible a partir de PHP 8.4.0.
