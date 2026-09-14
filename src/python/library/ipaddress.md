---
title: '"ipaddress" --- IPv4/IPv6 manipulation library'
source_url: https://docs.python.org/es/3
source_path: library/ipaddress.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3040
---

# "ipaddress" --- IPv4/IPv6 manipulation library

**Source code:** Lib/ipaddress.py

======================================================================

"ipaddress" provides the capabilities to create, manipulate and
operate on IPv4 and IPv6 addresses and networks.

Las funciones y clases de este módulo facilitan el manejo de varias
tareas relacionadas con las direcciones IP, incluida la verificación
de si dos hosts están en la misma subred, la iteración sobre todos los
hosts de una subred en particular, la verificación de si una cadena
representa un valor válido o no. Dirección IP o definición de red,
etc.

Esta es la referencia completa de la API del módulo; para obtener una
descripción general y una introducción, consulte Introducción al
modulo ipaddress.

Added in version 3.3.

## Funciones de fábrica de conveniencia

The "ipaddress" module provides factory functions to conveniently
create IP addresses, networks and interfaces:

ipaddress.ip_address(address)

   Retorna un objeto "IPv4Address" o "IPv6Address" según la dirección
   IP pasada como argumento. Se pueden proporcionar direcciones IPv4 o
   IPv6; los enteros menores que "2**32" se considerarán IPv4 de forma
   predeterminada. Se lanza un "ValueError" si *address* no representa
   una dirección IPv4 o IPv6 válida.

   >>> ipaddress.ip_address('192.168.0.1')
   IPv4Address('192.168.0.1')
   >>> ipaddress.ip_address('2001:db8::')
   IPv6Address('2001:db8::')

ipaddress.ip_network(address, strict=True)

   Retorna un objeto "IPv4Network" o "IPv6Network" dependiendo de la
   dirección IP pasada como argumento.  *address* es una cadena o
   entero que representa la red IP.  Se pueden suministrar redes IPv4
   o IPv6; los enteros menores que "2**32" se considerarán IPv4 de
   forma predeterminada. *strict* se pasa a "IPv4Network" o
   "IPv6Network" constructor.  Se genera un "ValueError" si *address*
   no representa una dirección IPv4 o IPv6 válida, o si la red tiene
   bits de host establecidos.

   >>> ipaddress.ip_network('192.168.0.0/28')
   IPv4Network('192.168.0.0/28')

ipaddress.ip_interface(address)

   Retorna un objeto "IPv4Interface" o "IPv6Interface" dependiendo de
   la dirección IP pasada como argumento.  *address* es una cadena o
   entero que representa la dirección IP.  Se pueden proporcionar
   direcciones IPv4 o IPv6; los enteros menores que "2**32" se
   considerarán IPv4 de forma predeterminada.  Se genera un
   "ValueError" si *address* no representa una dirección IPv4 o IPv6
   válida.

Una desventaja de estas funciones de conveniencia es que la necesidad
de manejar los formatos IPv4 e IPv6 significa que los mensajes de
error brindan información mínima sobre el error exacto, ya que las
funciones no saben si se pretendía usar el formato IPv4 o IPv6. Se
pueden obtener informes de errores más detallados llamando
directamente a los constructores de clases específicos de la versión
adecuada.

## Direcciones IP

### Objetos de dirección

Los objetos "IPv4Address" y "IPv6Address" comparten muchos atributos
comunes. Algunos atributos que solo son significativos para
direcciones IPv6 también son implementados por objetos "IPv4Address",
a fin de facilitar la escritura de código que maneje ambas versiones
de IP correctamente. Los objetos de dirección son *hashable*, por lo
que se pueden usar como claves en diccionarios.

class ipaddress.IPv4Address(address)

   Construya una dirección IPv4. Se genera un "AddressValueError" si
   *address* no es una dirección IPv4 válida.

   Lo siguiente constituye una dirección IPv4 válida:

   1. Una cadena en notación de punto decimal, que consta de cuatro
      enteros decimales en el rango inclusivo 0-255, separados por
      puntos (por ejemplo, "192.168.0.1"). Cada entero representa un
      octeto (byte) en la dirección. No se toleran ceros iniciales
      para evitar confusiones con la notación octal.

   2. Un número entero que cabe en 32 bits.

   3. Un entero empaquetado en un objeto "bytes" de longitud 4
      (primero el octeto más significativo).

   >>> ipaddress.IPv4Address('192.168.0.1')
   IPv4Address('192.168.0.1')
   >>> ipaddress.IPv4Address(3232235521)
   IPv4Address('192.168.0.1')
   >>> ipaddress.IPv4Address(b'\xC0\xA8\x00\x01')
   IPv4Address('192.168.0.1')

   Distinto en la versión 3.8: Se toleran los ceros iniciales, incluso
   en casos ambiguos que parecen notación octal.

   Distinto en la versión 3.9.5: Los ceros iniciales ya no se toleran
   y se tratan como un error. Las cadenas de direcciones IPv4 ahora se
   analizan tan estrictamente como glibc "inet_pton()".

   version

      El número de versión apropiado: "4" para IPv4, "6" para IPv6.

      Distinto en la versión 3.14: Made available on the class.

   max_prefixlen

      El número total de bits en la representación de direcciones para
      esta versión: "32" para IPv4, "128" para IPv6.

      El prefijo define el número de bits iniciales en una dirección
      que se comparan para determinar si una dirección es parte de una
      red o no.

      Distinto en la versión 3.14: Made available on the class.

   compressed

   exploded

      Representación de cadena en notación decimal con puntos. Los
      ceros iniciales nunca se incluyen en la representación.

      Como IPv4 no define una notación abreviada para direcciones con
      octetos establecidos en cero, estos dos atributos son siempre
      los mismos que "str(addr)" para direcciones IPv4. La exposición
      de estos atributos facilita la escritura de código de
      visualización que pueda manejar direcciones IPv4 e IPv6.

   packed

      La representación binaria de esta dirección: un objeto "bytes"
      de la longitud adecuada (primero el octeto más significativo).
      Son 4 bytes para IPv4 y 16 bytes para IPv6.

   reverse_pointer

      El nombre del registro PTR de DNS inverso para la dirección IP,
      por ejemplo:

         >>> ipaddress.ip_address("127.0.0.1").reverse_pointer
         '1.0.0.127.in-addr.arpa'
         >>> ipaddress.ip_address("2001:db8::1").reverse_pointer
         '1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.8.b.d.0.1.0.0.2.ip6.arpa'

      Este es el nombre que podría usarse para realizar una búsqueda
      PTR, no el nombre de host resuelto en sí.

      Added in version 3.5.

   is_multicast

      "True" si la dirección está reservada para uso de multidifusión.
      Consulte **RFC 3171** (para IPv4) o **RFC 2373** (para IPv6).

   is_private

      "True" if the address is defined as not globally reachable by
      iana-ipv4-special-registry (for IPv4) or iana-ipv6-special-
      registry (for IPv6) with the following exceptions:

      * "is_private" is "False" for the shared address space
        ("100.64.0.0/10")

      * For IPv4-mapped IPv6-addresses the "is_private" value is
        determined by the semantics of the underlying IPv4 addresses
        and the following condition holds (see
        "IPv6Address.ipv4_mapped"):

           address.is_private == address.ipv4_mapped.is_private

      "is_private" has value opposite to "is_global", except for the
      shared address space ("100.64.0.0/10" range) where they are both
      "False".

      Distinto en la versión 3.13: Fixed some false positives and
      false negatives.

      * "192.0.0.0/24" is considered private with the exception of
        "192.0.0.9/32" and "192.0.0.10/32" (previously: only the
        "192.0.0.0/29" sub-range was considered private).

      * "64:ff9b:1::/48" is considered private.

      * "2002::/16" is considered private.

      * There are exceptions within "2001::/23" (otherwise considered
        private): "2001:1::1/128", "2001:1::2/128", "2001:3::/32",
        "2001:4:112::/48", "2001:20::/28", "2001:30::/28". The
        exceptions are not considered private.

   is_global

      "True" if the address is defined as globally reachable by iana-
      ipv4-special-registry (for IPv4) or iana-ipv6-special-registry
      (for IPv6) with the following exception:

      For IPv4-mapped IPv6-addresses the "is_private" value is
      determined by the semantics of the underlying IPv4 addresses and
      the following condition holds (see "IPv6Address.ipv4_mapped"):

         address.is_global == address.ipv4_mapped.is_global

      "is_global" has value opposite to "is_private", except for the
      shared address space ("100.64.0.0/10" range) where they are both
      "False".

      Added in version 3.4.

      Distinto en la versión 3.13: Fixed some false positives and
      false negatives, see "is_private" for details.

   is_unspecified

      "True" si la dirección no está especificada. Consulte **RFC
      5735** (para IPv4) o **RFC 2373** (para IPv6).

   is_reserved

      "True" if the address is noted as reserved by the IETF. For
      IPv4, this is only "240.0.0.0/4", the "Reserved" address block.
      For IPv6, this is all addresses allocated as "Reserved by IETF"
      for future use.

      Nota:

        For IPv4, "is_reserved" is not related to the address block
        value of the "Reserved-by-Protocol" column in iana-ipv4
        -special-registry.

      Prudencia:

        For IPv6, "fec0::/10" a former Site-Local scoped address
        prefix is currently excluded from that list (see
        "is_site_local" & **RFC 3879**).

   is_loopback

      "True" si se trata de una dirección de bucle invertido. Consulte
      **RFC 3330** (para IPv4) o **RFC 2373** (para IPv6).

   is_link_local

      "True" si se trata de una dirección de bucle invertido. Consulte
      **RFC 3330** (para IPv4) o **RFC 2373** (para IPv6). "True" si
      la dirección está reservada para uso local de enlace. Ver **RFC
      3927**.

   ipv6_mapped

      "IPv4Address" object representing the IPv4-mapped IPv6 address.
      See **RFC 4291**.

      Added in version 3.13.

IPv4Address.__format__(fmt)

   Devuelve una representación de cadena de la dirección IP,
   controlada por una cadena de formato explícito. *fmt* puede ser uno
   de los siguientes: "'s'", la opción predeterminada, equivalente a
   "str()", "'b'" para una cadena binaria con relleno de ceros, "'X'"
   o "'x'" para una representación hexadecimal en mayúsculas o
   minúsculas, o "'n'", que es equivalente a "'b'" para direcciones
   IPv4 y "'x'" para IPv6. Para representaciones binarias y
   hexadecimales, el especificador de formulario "'#'" y la opción de
   agrupación "'_'" están disponibles. "__format__" es utilizado por
   "format", "str.format" y f-strings.

   >>> format(ipaddress.IPv4Address('192.168.0.1'))
   '192.168.0.1'
   >>> '{:#b}'.format(ipaddress.IPv4Address('192.168.0.1'))
   '0b11000000101010000000000000000001'
   >>> f'{ipaddress.IPv6Address("2001:db8::1000"):s}'
   '2001:db8::1000'
   >>> format(ipaddress.IPv6Address('2001:db8::1000'), '_X')
   '2001_0DB8_0000_0000_0000_0000_0000_1000'
   >>> '{:#_n}'.format(ipaddress.IPv6Address('2001:db8::1000'))
   '0x2001_0db8_0000_0000_0000_0000_0000_1000'

   Added in version 3.9.

class ipaddress.IPv6Address(address)

   Construya una dirección IPv6. Se genera un "AddressValueError" si
   *address* no es una dirección IPv6 válida.

   Lo siguiente constituye una dirección IPv6 válida:

   1. Una cadena que consta de ocho grupos de cuatro dígitos
      hexadecimales, cada grupo representa 16 bits. Los grupos están
      separados por dos puntos. Esto describe una notación *explotada*
      (a mano). La cadena también se puede *comprimir* (notación
      abreviada) por varios medios. Consulte **RFC 4291** para obtener
      más detalles. Por ejemplo,
      ""0000:0000:0000:0000:0000:0abc:0007:0def"" se puede comprimir
      en ""::abc:7:def"".

      Opcionalmente, la cadena también puede tener un ID de zona de
      alcance, expresado con un sufijo "%scope_id". Si está presente,
      el ID de alcance no debe estar vacío y no puede contener "%".
      Consulte **RFC 4007** para obtener más detalles. Por ejemplo,
      "fe80::1234%1" podría identificar la dirección "fe80::1234" en
      el primer enlace del nodo.

   2. Un número entero que cabe en 128 bits.

   3. Un entero empaquetado en un objeto "bytes" de longitud 16, big-
      endian.

   >>> ipaddress.IPv6Address('2001:db8::1000')
   IPv6Address('2001:db8::1000')
   >>> ipaddress.IPv6Address('ff02::5678%1')
   IPv6Address('ff02::5678%1')

   compressed

   La forma corta de la representación de la dirección, con ceros a la
   izquierda en los grupos omitidos y la secuencia más larga de grupos
   que consta completamente de ceros colapsó en un solo grupo vacío.

   Este también es el valor devuelto por "str(addr)" para las
   direcciones IPv6.

   exploded

   La forma larga de la representación de la dirección, con todos los
   ceros a la izquierda y los grupos que constan completamente de
   ceros incluidos.

   Para los siguientes atributos y métodos, consulte la documentación
   correspondiente de la clase "IPv4Address":

   packed

   reverse_pointer

   version

   max_prefixlen

   is_multicast

   is_private

   is_global

      Added in version 3.4.

   is_unspecified

   is_reserved

   is_loopback

   is_link_local

   is_site_local

      "True" si la dirección está reservada para uso local del sitio.
      Tenga en cuenta que el espacio de direcciones local del sitio ha
      quedado obsoleto por **RFC 3879**. Utilice "is_private" para
      probar si esta dirección está en el espacio de direcciones
      locales únicas como se define en **RFC 4193**.

   ipv4_mapped

      For addresses that appear to be IPv4 mapped addresses in the
      range "::FFFF:0:0/96" as defined by **RFC 4291**, this property
      reports the embedded IPv4 address. For any other address, this
      property will be "None".

   scope_id

      Para las direcciones de ámbito definido por **RFC 4007**, esta
      propiedad identifica la zona particular del ámbito de la
      dirección a la que pertenece la dirección, como una cadena.
      Cuando no se especifica ninguna zona de alcance, esta propiedad
      será "None".

   sixtofour

      Para direcciones que parecen ser direcciones 6to4 (comenzando
      con "2002::/16") según lo definido por **RFC 3056**, esta
      propiedad informará la dirección IPv4 incrustada. Para cualquier
      otra dirección, esta propiedad será "None".

   teredo

      Para las direcciones que parecen ser direcciones Teredo (que
      comienzan con "2001::/32") según lo definido por **RFC 4380**,
      esta propiedad informará el par de direcciones IP "(servidor,
      cliente)" incrustado. Para cualquier otra dirección, esta
      propiedad será "None".

IPv6Address.__format__(fmt)

   Consulte la documentación del método correspondiente en
   "IPv4Address".

   Added in version 3.9.

### Conversión a cadenas y enteros

Para interoperar con interfaces de red como el módulo de socket, las
direcciones deben convertirse en cadenas o números enteros. Esto se
maneja usando las funciones integradas "str()" y "int()"

   >>> str(ipaddress.IPv4Address('192.168.0.1'))
   '192.168.0.1'
   >>> int(ipaddress.IPv4Address('192.168.0.1'))
   3232235521
   >>> str(ipaddress.IPv6Address('::1'))
   '::1'
   >>> int(ipaddress.IPv6Address('::1'))
   1

Tenga en cuenta que las direcciones de ámbito IPv6 se convierten en
números enteros sin ID de zona de ámbito.

### Operadores

Los objetos de dirección admiten algunos operadores. A menos que se
indique lo contrario, los operadores solo se pueden aplicar entre
objetos compatibles (es decir, IPv4 con IPv4, IPv6 con IPv6).

#### Operadores de comparación

Los objetos de dirección se pueden comparar con el conjunto habitual
de operadores de comparación. Las mismas direcciones IPv6 con
diferentes ID de zona de alcance no son iguales. Algunos ejemplos:

   >>> IPv4Address('127.0.0.2') > IPv4Address('127.0.0.1')
   True
   >>> IPv4Address('127.0.0.2') == IPv4Address('127.0.0.1')
   False
   >>> IPv4Address('127.0.0.2') != IPv4Address('127.0.0.1')
   True
   >>> IPv6Address('fe80::1234') == IPv6Address('fe80::1234%1')
   False
   >>> IPv6Address('fe80::1234%1') != IPv6Address('fe80::1234%2')
   True

#### Operadores aritméticos

Los números enteros se pueden sumar o restar de los objetos de
dirección. Algunos ejemplos:

   >>> IPv4Address('127.0.0.2') + 3
   IPv4Address('127.0.0.5')
   >>> IPv4Address('127.0.0.2') - 3
   IPv4Address('126.255.255.255')
   >>> IPv4Address('255.255.255.255') + 1
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   ipaddress.AddressValueError: 4294967296 (>= 2**32) is not permitted as an IPv4 address

## Definiciones de red IP

Los objetos "IPv4Network" y "IPv6Network" proporcionan un mecanismo
para definir e inspeccionar las definiciones de red IP. Una definición
de red consta de una * máscara * y una * dirección de red * y, como
tal, define un rango de direcciones IP que son iguales a la dirección
de red cuando están enmascaradas (Y binario) con la máscara. Por
ejemplo, una definición de red con la máscara "255.255.255.0" y la
dirección de red "192.168.1.0" consta de direcciones IP en el rango
inclusivo de "192.168.1.0" a "192.168.1.255".

### Prefijo, máscara de red y máscara de host

Hay varias formas equivalentes de especificar máscaras de red IP. Un
*prefix* "/<nbits>" es una notación que indica cuántos bits de orden
superior se establecen en la máscara de red. Una máscara de red
(*mask*) es una dirección IP con una cierta cantidad de bits de orden
superior establecidos. Por lo tanto, el prefijo "/24" es equivalente a
la máscara de red "255.255.255.0" en IPv4, o "ffff:ff00::" en IPv6.
Además, una * máscara de host * es el inverso lógico de una * máscara
de red * y, a veces, se utiliza (por ejemplo, en las listas de control
de acceso de Cisco) para indicar una máscara de red. La máscara de
host equivalente a "/24" en IPv4 es "0.0.0.255".

### Objetos de red

Todos los atributos implementados por objetos de dirección también son
implementados por objetos de red. Además, los objetos de red
implementan atributos adicionales. Todos estos son comunes entre
"IPv4Network" y "IPv6Network", por lo que para evitar la duplicación
solo se documentan para "IPv4Network". Los objetos de red son
*hashable*, por lo que se pueden usar como claves en diccionarios.

class ipaddress.IPv4Network(address, strict=True)

   Construya una definición de red IPv4. *address* puede ser una de
   las siguientes:

   1. Una cadena que consta de una dirección IP y una máscara
      opcional, separadas por una barra ("/"). La dirección IP es la
      dirección de red y la máscara puede ser un solo número, lo que
      significa que es un *prefix*, o una representación de cadena de
      caracteres de una dirección IPv4.  Si es la última, la máscara
      es interpretada como una *net mask* si comienza con un campo no
      nulo, o como una *host mask* si comienza con un campo cero, con
      la excepción de una máscara de solo ceros la cual es tratada
      como una *net mask*. Si no se proporciona una máscara, se
      considera "/32".

      Por ejemplo, las siguientes especificaciones de *address* son
      equivalentes: "192.168.1.0/24", "192.168.1.0/255.255.255.0" y
      "192.168.1.0/0.0.0.255".

   2. Un número entero que cabe en 32 bits. Esto es equivalente a una
      red de una sola dirección, con la dirección de red *address* y
      la máscara "/32".

   3. Un entero empaquetado en un objeto "bytes" de longitud 4, big-
      endian. La interpretación es similar a una *address* entera.

   4. A two-tuple of an address description and a netmask, where the
      address description is either a string, a 32-bits integer, a
      4-bytes packed integer, or an existing "IPv4Address" object; and
      the netmask is either an integer representing the prefix length
      (e.g. "24") or a string representing the prefix mask (e.g.
      "255.255.255.0").

   Se genera un "AddressValueError" si *address* no es una dirección
   IPv4 válida. A "NetmaskValueError" se genera si la máscara no es
   válida para una dirección IPv4.

   Si *strict* es "True" y los bits de host están configurados en la
   dirección proporcionada, entonces "ValueError" se genera. De lo
   contrario, los bits del host se enmascaran para determinar la
   dirección de red adecuada.

   A menos que se indique lo contrario, todos los métodos de red que
   acepten otros objetos de red / dirección generarán "TypeError" si
   la versión de IP del argumento es incompatible con "self".

   Distinto en la versión 3.5: Se agregó la forma de dos tuplas para
   el parámetro de constructor *address*.

   version

   max_prefixlen

      Consulte la documentación del atributo correspondiente en
      "IPv4Address".

   is_multicast

   is_private

   is_unspecified

   is_reserved

   is_loopback

   is_link_local

      Estos atributos son verdaderos para la red en su conjunto si lo
      son tanto para la dirección de red como para la dirección de
      transmisión.

   network_address

      La dirección de red de la red. La dirección de red y la longitud
      del prefijo juntos definen de forma única una red.

   broadcast_address

      La dirección de transmisión de la red. Todos los hosts de la red
      deben recibir los paquetes enviados a la dirección de
      transmisión.

   hostmask

      La máscara de host, como un objeto "IPv4Address".

   netmask

      La máscara de red, como un objeto "IPv4Address".

   with_prefixlen

   compressed

   exploded

      Una representación de cadena de la red, con la máscara en
      notación de prefijo.

      "with_prefixlen" y "compressed" son siempre lo mismo que
      "str(red)". "exploded" utiliza la forma explosionada de la
      dirección de red.

   with_netmask

      Una representación de cadena de la red, con la máscara en
      notación de máscara de red.

   with_hostmask

      Una representación de cadena de la red, con la máscara en
      notación de máscara de host.

   num_addresses

      El número total de direcciones en la red.

   prefixlen

      Longitud del prefijo de red, en bits.

   hosts()

      Longitud de Devuelve un iterador sobre los hosts utilizables en
      la red. Los hosts utilizables son todas las direcciones IP que
      pertenecen a la red, excepto la dirección de red en sí y la
      dirección de transmisión de la red. Para redes con una longitud
      de máscara de 31, la dirección de red y la dirección de
      transmisión de red también se incluyen en el resultado. Las
      redes con una máscara de 32 devolverán una lista que contiene la
      dirección de host única, el prefijo de red, en bits.

      >>> list(ip_network('192.0.2.0/29').hosts())
      [IPv4Address('192.0.2.1'), IPv4Address('192.0.2.2'),
       IPv4Address('192.0.2.3'), IPv4Address('192.0.2.4'),
       IPv4Address('192.0.2.5'), IPv4Address('192.0.2.6')]
      >>> list(ip_network('192.0.2.0/31').hosts())
      [IPv4Address('192.0.2.0'), IPv4Address('192.0.2.1')]
      >>> list(ip_network('192.0.2.1/32').hosts())
      [IPv4Address('192.0.2.1')]

   overlaps(other)

      "True" si esta red está total o parcialmente contenida en
      *other* o *other* está completamente contenido en esta red.

   address_exclude(network)

      Calcula las definiciones de red resultantes de eliminar la
      *network* dada de esta. Devuelve un iterador de objetos de red.
      Genera "ValueError" si *network* no está completamente contenido
      en esta red.

      >>> n1 = ip_network('192.0.2.0/28')
      >>> n2 = ip_network('192.0.2.1/32')
      >>> list(n1.address_exclude(n2))
      [IPv4Network('192.0.2.8/29'), IPv4Network('192.0.2.4/30'),
       IPv4Network('192.0.2.2/31'), IPv4Network('192.0.2.0/32')]

   subnets(prefixlen_diff=1, new_prefix=None)

      Las subredes que se unen para crear la definición de red actual,
      según los valores de los argumentos. *prefixlen_diff* es la
      cantidad en la que se debe aumentar la longitud de nuestro
      prefijo. *new_prefix* es el nuevo prefijo deseado de las
      subredes; debe ser más grande que nuestro prefijo. Se debe
      establecer uno y solo uno de *prefixlen_diff* y *new_prefix*.
      Devuelve un iterador de objetos de red.

      >>> list(ip_network('192.0.2.0/24').subnets())
      [IPv4Network('192.0.2.0/25'), IPv4Network('192.0.2.128/25')]
      >>> list(ip_network('192.0.2.0/24').subnets(prefixlen_diff=2))
      [IPv4Network('192.0.2.0/26'), IPv4Network('192.0.2.64/26'),
       IPv4Network('192.0.2.128/26'), IPv4Network('192.0.2.192/26')]
      >>> list(ip_network('192.0.2.0/24').subnets(new_prefix=26))
      [IPv4Network('192.0.2.0/26'), IPv4Network('192.0.2.64/26'),
       IPv4Network('192.0.2.128/26'), IPv4Network('192.0.2.192/26')]
      >>> list(ip_network('192.0.2.0/24').subnets(new_prefix=23))
      Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
          raise ValueError('new prefix must be longer')
      ValueError: new prefix must be longer
      >>> list(ip_network('192.0.2.0/24').subnets(new_prefix=25))
      [IPv4Network('192.0.2.0/25'), IPv4Network('192.0.2.128/25')]

   supernet(prefixlen_diff=1, new_prefix=None)

      La superred que contiene esta definición de red, según los
      valores de los argumentos. *prefixlen_diff* es la cantidad en la
      que se debe reducir la longitud de nuestro prefijo. *new_prefix*
      es el nuevo prefijo deseado de la superred; debe ser más pequeño
      que nuestro prefijo. Se debe establecer uno y solo uno de
      *prefixlen_diff* y *new_prefix*. Devuelve un solo objeto de red.

      >>> ip_network('192.0.2.0/24').supernet()
      IPv4Network('192.0.2.0/23')
      >>> ip_network('192.0.2.0/24').supernet(prefixlen_diff=2)
      IPv4Network('192.0.0.0/22')
      >>> ip_network('192.0.2.0/24').supernet(new_prefix=20)
      IPv4Network('192.0.0.0/20')

   subnet_of(other)

      Devuelve "True" si esta red es una subred de *other*.

      >>> a = ip_network('192.168.1.0/24')
      >>> b = ip_network('192.168.1.128/30')
      >>> b.subnet_of(a)
      True

      Added in version 3.7.

   supernet_of(other)

      Devuelve "True" si esta red es una superred de *other*.

      >>> a = ip_network('192.168.1.0/24')
      >>> b = ip_network('192.168.1.128/30')
      >>> a.supernet_of(b)
      True

      Added in version 3.7.

   compare_networks(other)

      Compare esta red con *other*. En esta comparación solo se
      consideran las direcciones de red; los bits de host no lo son.
      Devuelve "-1", "0" o "1".

      >>> ip_network('192.0.2.1/32').compare_networks(ip_network('192.0.2.2/32'))
      -1
      >>> ip_network('192.0.2.1/32').compare_networks(ip_network('192.0.2.0/32'))
      1
      >>> ip_network('192.0.2.1/32').compare_networks(ip_network('192.0.2.1/32'))
      0

      Obsoleto desde la versión 3.7: Utiliza el mismo algoritmo de
      ordenación y comparación que "<", "==" y ">"

class ipaddress.IPv6Network(address, strict=True)

   Construya una definición de red IPv6. *address* puede ser una de
   las siguientes:

   1. Una cadena que consta de una dirección IP y una longitud de
      prefijo opcional, separados por una barra ("/"). La dirección IP
      es la dirección de red y la longitud del prefijo debe ser un
      solo número, el *prefix*. Si no se proporciona una longitud de
      prefijo, se considera que es "/128".

      Tenga en cuenta que las máscaras de red expandidas actualmente
      no son compatibles. Eso significa que "2001:db00::0/24" es un
      argumento válido mientras que "2001:db00::0/ffff:ff00::" no lo
      es.

   2. Un número entero que cabe en 128 bits. Esto es equivalente a una
      red de una sola dirección, con la dirección de red *address* y
      la máscara "/128".

   3. Un entero empaquetado en un objeto "bytes" de longitud 16, big-
      endian. La interpretación es similar a una *address* entera.

   4. A two-tuple of an address description and a netmask, where the
      address description is either a string, a 128-bits integer, a
      16-bytes packed integer, or an existing "IPv6Address" object;
      and the netmask is an integer representing the prefix length.

   Se genera un "AddressValueError" si *address* no es una dirección
   IPv6 válida. A "NetmaskValueError" se genera si la máscara no es
   válida para una dirección IPv6.

   Si *strict* es "True" y los bits de host están configurados en la
   dirección proporcionada, entonces "ValueError" se genera. De lo
   contrario, los bits del host se enmascaran para determinar la
   dirección de red adecuada.

   Distinto en la versión 3.5: Se agregó la forma de dos tuplas para
   el parámetro de constructor *address*.

   version

   max_prefixlen

   is_multicast

   is_private

   is_unspecified

   is_reserved

   is_loopback

   is_link_local

   network_address

   broadcast_address

   hostmask

   netmask

   with_prefixlen

   compressed

   exploded

   with_netmask

   with_hostmask

   num_addresses

   prefixlen

   hosts()

      Devuelve un iterador sobre los hosts utilizables en la red. Los
      hosts utilizables son todas las direcciones IP que pertenecen a
      la red, excepto la dirección Anycast del Subnet-Router. Para
      redes con una longitud de máscara de 127, la dirección anycast
      del Subnet-Router también se incluye en el resultado. Las redes
      con una máscara de 128 devolverán una lista que contiene la
      única dirección de host.

   overlaps(other)

   address_exclude(network)

   subnets(prefixlen_diff=1, new_prefix=None)

   supernet(prefixlen_diff=1, new_prefix=None)

   subnet_of(other)

   supernet_of(other)

   compare_networks(other)

      Consulte la documentación del atributo correspondiente en
      "IPv4Network".

   is_site_local

      This attribute is true for the network as a whole if it is true
      for both the network address and the broadcast address.

### Operadores

Este atributo es verdadero para la red en su conjunto si es cierto
para ambos objetos de red que admiten algunos operadores. A menos que
se indique lo contrario, los operadores solo se pueden aplicar entre
objetos compatibles (es decir, IPv4 con IPv4, IPv6 con IPv6).

#### Operadores lógicos

Los objetos de red se pueden comparar con el conjunto habitual de
operadores lógicos. Los objetos de red se ordenan primero por
dirección de red y luego por máscara de red.

#### Iteración

Los objetos de red se pueden iterar para enumerar todas las
direcciones que pertenecen a la red. Para la iteración, se devuelven
*todos* los hosts, incluidos los hosts inutilizables (para hosts
utilizables, use el método "hosts()"). Un ejemplo:

   >>> for addr in IPv4Network('192.0.2.0/28'):
   ...     addr
   ...
   IPv4Address('192.0.2.0')
   IPv4Address('192.0.2.1')
   IPv4Address('192.0.2.2')
   IPv4Address('192.0.2.3')
   IPv4Address('192.0.2.4')
   IPv4Address('192.0.2.5')
   IPv4Address('192.0.2.6')
   IPv4Address('192.0.2.7')
   IPv4Address('192.0.2.8')
   IPv4Address('192.0.2.9')
   IPv4Address('192.0.2.10')
   IPv4Address('192.0.2.11')
   IPv4Address('192.0.2.12')
   IPv4Address('192.0.2.13')
   IPv4Address('192.0.2.14')
   IPv4Address('192.0.2.15')

#### Redes como contenedores de direcciones

Los objetos de red pueden actuar como contenedores de direcciones.
Algunos ejemplos:

   >>> IPv4Network('192.0.2.0/28')[0]
   IPv4Address('192.0.2.0')
   >>> IPv4Network('192.0.2.0/28')[15]
   IPv4Address('192.0.2.15')
   >>> IPv4Address('192.0.2.6') in IPv4Network('192.0.2.0/28')
   True
   >>> IPv4Address('192.0.3.6') in IPv4Network('192.0.2.0/28')
   False

## Objetos de interfaz

Los objetos de interfaz son *hashable*, por lo que se pueden usar como
claves en diccionarios.

class ipaddress.IPv4Interface(address)

   Construya una interfaz IPv4. El significado de *address* es como en
   el constructor de "IPv4Network", excepto que siempre se aceptan
   direcciones de host arbitrarias.

   "IPv4Interface" es una subclase de "IPv4Address", por lo que hereda
   todos los atributos de esa clase. Además, están disponibles los
   siguientes atributos:

   ip

      The address ("IPv4Address") without network information.

      >>> interface = IPv4Interface('192.0.2.5/24')
      >>> interface.ip
      IPv4Address('192.0.2.5')

   network

      La red ("IPv4Network") a la que pertenece esta interfaz.

      >>> interface = IPv4Interface('192.0.2.5/24')
      >>> interface.network
      IPv4Network('192.0.2.0/24')

   with_prefixlen

      Una representación de cadena de la interfaz con la máscara en
      notación de prefijo.

      >>> interface = IPv4Interface('192.0.2.5/24')
      >>> interface.with_prefixlen
      '192.0.2.5/24'

   with_netmask

      Una representación de cadena de la interfaz con la red como
      máscara de red.

      >>> interface = IPv4Interface('192.0.2.5/24')
      >>> interface.with_netmask
      '192.0.2.5/255.255.255.0'

   with_hostmask

      Una representación de cadena de la interfaz con la red como
      máscara de host.

      >>> interface = IPv4Interface('192.0.2.5/24')
      >>> interface.with_hostmask
      '192.0.2.5/0.0.0.255'

class ipaddress.IPv6Interface(address)

   Construya una interfaz IPv6. El significado de *address* es como en
   el constructor de "IPv6Network", excepto que siempre se aceptan
   direcciones de host arbitrarias.

   "IPv6Interface" es una subclase de "IPv6Address", por lo que hereda
   todos los atributos de esa clase. Además, están disponibles los
   siguientes atributos:

   ip

   network

   with_prefixlen

   with_netmask

   with_hostmask

      Consulte la documentación del atributo correspondiente en
      "IPv4Interface".

### Operadores

Los objetos de interfaz admiten algunos operadores. A menos que se
indique lo contrario, los operadores solo se pueden aplicar entre
objetos compatibles (es decir, IPv4 con IPv4, IPv6 con IPv6).

#### Operadores lógicos

Los objetos de interfaz se pueden comparar con el conjunto habitual de
operadores lógicos.

Para la comparación de igualdad ("==" y "!="), Tanto la dirección IP
como la red deben ser iguales para que los objetos sean iguales. Una
interfaz no se comparará con ninguna dirección u objeto de red.

Para ordenar ("<", ">", etc) las reglas son diferentes. Los objetos de
interfaz y dirección con la misma versión de IP se pueden comparar, y
los objetos de dirección siempre se clasificarán antes que los objetos
de interfaz. Primero se comparan dos objetos de interfaz por sus redes
y, si son iguales, luego por sus direcciones IP.

## Otras funciones de nivel de módulo

El módulo también proporciona las siguientes funciones de nivel de
módulo:

ipaddress.v4_int_to_packed(address)

   Represente una dirección como 4 bytes empaquetados en orden de red
   (big-endian). *address* es una representación entera de una
   dirección IP IPv4. A "ValueError" se genera si el número entero es
   negativo o demasiado grande para ser una dirección IP IPv4.

   >>> ipaddress.ip_address(3221225985)
   IPv4Address('192.0.2.1')
   >>> ipaddress.v4_int_to_packed(3221225985)
   b'\xc0\x00\x02\x01'

ipaddress.v6_int_to_packed(address)

   Representa una dirección como 16 bytes empaquetados en orden de red
   (big-endian). *address* es una representación entera de una
   dirección IP IPv6. A "ValueError" se genera si el número entero es
   negativo o demasiado grande para ser una dirección IP IPv6.

ipaddress.summarize_address_range(first, last)

   Devuelve un iterador del rango de red resumido dadas la primera y
   la última dirección IP. *first* es el primero "IPv4Address" o
   "IPv6Address" en el rango y *last* es el último "IPv4Address" o
   "IPv6Address" en el rango. A "TypeError" se genera si *first* o
   *last* no son direcciones IP o no son de la misma versión. A
   "ValueError" se genera si *last* no es mayor que *first* o si la
   *first* versión de la dirección no es 4 o 6.

   >>> [ipaddr for ipaddr in ipaddress.summarize_address_range(
   ...    ipaddress.IPv4Address('192.0.2.0'),
   ...    ipaddress.IPv4Address('192.0.2.130'))]
   [IPv4Network('192.0.2.0/25'), IPv4Network('192.0.2.128/31'), IPv4Network('192.0.2.130/32')]

ipaddress.collapse_addresses(addresses)

   Return an iterator of the collapsed "IPv4Network" or "IPv6Network"
   objects.  *addresses* is an *iterable* of "IPv4Network" or
   "IPv6Network" objects.  A "TypeError" is raised if *addresses*
   contains mixed version objects.

   >>> [ipaddr for ipaddr in
   ... ipaddress.collapse_addresses([ipaddress.IPv4Network('192.0.2.0/25'),
   ... ipaddress.IPv4Network('192.0.2.128/25')])]
   [IPv4Network('192.0.2.0/24')]

ipaddress.get_mixed_type_key(obj)

   Devuelve una clave adecuada para clasificar entre redes y
   direcciones. Los objetos de dirección y red no se pueden ordenar de
   forma predeterminada; son fundamentalmente diferentes, por lo que
   la expresión

      IPv4Address('192.0.2.0') <= IPv4Network('192.0.2.0/24')

   doesn't make sense.  There are some times however, where you may
   wish to have "ipaddress" sort these anyway.  If you need to do
   this, you can use this function as the *key* argument to
   "sorted()".

   *obj* es un objeto de red o de dirección.

## Excepciones personalizadas

Para admitir informes de errores más específicos de los constructores
de clases, el módulo define las siguientes excepciones:

exception ipaddress.AddressValueError(ValueError)

   Cualquier error de valor relacionado con la dirección.

exception ipaddress.NetmaskValueError(ValueError)

   Cualquier error de valor relacionado con la máscara de red.
