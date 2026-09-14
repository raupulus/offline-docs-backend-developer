---
title: '"uuid" --- UUID objects according to **RFC 9562**'
source_url: https://docs.python.org/es/3
source_path: library/uuid.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4460
---

# "uuid" --- UUID objects according to **RFC 9562**

**Código fuente:** Lib/uuid.py

======================================================================

This module provides immutable "UUID" objects (the "UUID" class) and
functions for generating UUIDs corresponding to a specific UUID
version as specified in **RFC 9562** (which supersedes **RFC 4122**),
for example, "uuid1()" for UUID version 1, "uuid3()" for UUID version
3, and so on. Note that UUID version 2 is deliberately omitted as it
is outside the scope of the RFC.

Si todo lo que quieres es una identificación única, probablemente
deberías llamar a "uuuid1()" o "uuid4()".  Ten en cuenta que "uuid1()"
puede comprometer la privacidad ya que crea un UUID que contiene la
dirección de red del ordenador. "uuid4()" crea un UUID aleatorio.

Dependiendo del soporte de la plataforma subyacente, "uuid1()" puede o
no retornar un UUID "seguro". Un UUID seguro es aquel que se genera
mediante métodos de sincronización que aseguran que ningún proceso
pueda obtener el mismo UUID. Todas las instancias de "UUID" tienen un
atributo "is_safe" que transmite cualquier información sobre la
seguridad del UUID, usando esta enumeración:

class uuid.SafeUUID

   Added in version 3.7.

   safe

      El UUID fue generado por la plataforma de una manera segura para
      multiprocesamiento.

   unsafe

      El UUID no fue generado por la plataforma de una manera segura
      de multiprocesamiento.

   unknown

      La plataforma no proporciona información sobre si el UUID se
      generó de forma segura o no.

class uuid.UUID(hex=None, bytes=None, bytes_le=None, fields=None, int=None, version=None, *, is_safe=SafeUUID.unknown)

   Crea un UUID a partir de una cadena de 32 dígitos hexadecimales,
   una cadena de 16 bytes en orden *big-endian* como el argumento
   *bytes*, una cadena de 16 bytes en orden *little-endian* como el
   argumento *bytes_le*, una tupla de seis enteros (32-bit *time_low*,
   16-bit *time_mid*, 16-bit *time_hi_version*, 8-bit
   *clock_seq_hi_variant*, 8-bit *clock_seq_low*, 48-bit *node*) como
   el argumento *fields*, o un solo entero de 128-bit como el
   argumento *int*. Cuando se da una cadena de dígitos hexadecimales,
   los corchetes, los guiones y el prefijo URN son todos opcionales.
   Por ejemplo, todas estas expresiones producen el mismo UUID:

      UUID('{12345678-1234-5678-1234-567812345678}')
      UUID('12345678123456781234567812345678')
      UUID('urn:uuid:12345678-1234-5678-1234-567812345678')
      UUID(bytes=b'\x12\x34\x56\x78'*4)
      UUID(bytes_le=b'\x78\x56\x34\x12\x34\x12\x78\x56' +
                    b'\x12\x34\x56\x78\x12\x34\x56\x78')
      UUID(fields=(0x12345678, 0x1234, 0x5678, 0x12, 0x34, 0x567812345678))
      UUID(int=0x12345678123456781234567812345678)

   Exactly one of *hex*, *bytes*, *bytes_le*, *fields*, or *int* must
   be given. The *version* argument is optional; if given, the
   resulting UUID will have its variant and version number set
   according to **RFC 9562**, overriding bits in the given *hex*,
   *bytes*, *bytes_le*, *fields*, or *int*.

   La comparación de los objetos UUID se hace mediante la comparación
   de sus atributos "UID.int".  La comparación con un objeto no UUID
   produce un "TypeError".

   "str(uuid)" retorna una cadena en la forma
   "12345678-1234-5678-1234-567812345678" donde los 32 dígitos
   hexadecimales representan el UUID.

Las instancias de "UUID" tienen estos atributos de sólo lectura:

UUID.bytes

   El UUID como una cadena de 16 bytes (que contiene los seis campos
   enteros en orden de bytes *big-endian*).

UUID.bytes_le

   El UUID como una cadena de 16 bytes (con *time_low*, *time_mid*, y
   *time_hi_version* en el orden de bytes *little-endian*).

UUID.fields

   Una tupla de los seis campos enteros de la UUID, que también están
   disponibles como seis atributos individuales y dos atributos
   derivados:

# | Campo                                              | Significado                                        |

| UUID.time_low                                      | The first 32 bits of the UUID. Only relevant to    |
## |                                                    | version 1.                                         |

| UUID.time_mid                                      | The next 16 bits of the UUID. Only relevant to     |
## |                                                    | version 1.                                         |

| UUID.time_hi_version                               | The next 16 bits of the UUID. Only relevant to     |
## |                                                    | version 1.                                         |

| UUID.clock_seq_hi_variant                          | The next 8 bits of the UUID. Only relevant to      |
## |                                                    | versions 1 and 6.                                  |

| UUID.clock_seq_low                                 | The next 8 bits of the UUID. Only relevant to      |
## |                                                    | versions 1 and 6.                                  |

| UUID.node                                          | The last 48 bits of the UUID. Only relevant to     |
## |                                                    | version 1.                                         |

| UUID.time                                          | The 60-bit timestamp as a count of 100-nanosecond  |
|                                                    | intervals since Gregorian epoch (1582-10-15        |
|                                                    | 00:00:00) for versions 1 and 6, or the 48-bit      |
|                                                    | timestamp in milliseconds since Unix epoch         |
## |                                                    | (1970-01-01 00:00:00) for version 7.               |

| UUID.clock_seq                                     | The 14-bit sequence number. Only relevant to       |
## |                                                    | versions 1 and 6.                                  |

UUID.hex

   El UUID como una cadena hexadecimal en minúsculas de 32 caracteres.

UUID.int

   El UUID como un entero de 128 bits.

UUID.urn

   The UUID as a URN as specified in **RFC 9562**.

UUID.variant

   La variante UUID, que determina la disposición interna del UUID.
   Esta será una de las constantes "RESERVED_NCS", "RFC_4122",
   "RESERVED_MICROSOFT", o "RESERVED_FUTURE".

UUID.version

   The UUID version number (1 through 8, meaningful only when the
   variant is "RFC_4122").

   Distinto en la versión 3.14: Added UUID versions 6, 7 and 8.

UUID.is_safe

   Una enumeración de "SafeUUID" que indica si la plataforma generó el
   UUID de forma segura para el multiprocesamiento.

   Added in version 3.7.

The "uuid" module defines the following functions:

uuid.getnode()

   Obtiene la dirección del hardware como un entero positivo de 48
   bits.  La primera vez que esto se ejecute, puede lanzar un programa
   separado, que podría ser bastante lento.  Si todos los intentos de
   obtener la dirección de hardware fallan, elegimos un número
   aleatorio de 48 bits con el bit multicast (el bit menos
   significativo del primer octeto) puesto a 1 como se recomienda en
   **RFC 4122**.  "Dirección de hardware" significa la dirección MAC
   de una interfaz de red.  En una máquina con múltiples interfaces de
   red, las direcciones MAC administradas universalmente (es decir,
   donde el segundo bit menos significativo del primer octeto es
   *unset*) se preferirán a las direcciones MAC administradas
   localmente, pero sin otras garantías de orden.

   Distinto en la versión 3.7: Se prefieren las direcciones MAC
   administradas universalmente a las administradas localmente, ya que
   se garantiza que las primeras son únicas a nivel mundial, mientras
   que las segundas no lo son.

uuid.uuid1(node=None, clock_seq=None)

   Generate a UUID from a host ID, sequence number, and the current
   time according to **RFC 9562, §5.1**.

   When *node* is not specified, "getnode()" is used to obtain the
   hardware address as a 48-bit positive integer. When a sequence
   number *clock_seq* is not specified, a pseudo-random 14-bit
   positive integer is generated.

   If *node* or *clock_seq* exceed their expected bit count, only
   their least significant bits are kept.

uuid.uuid3(namespace, name)

   Generate a UUID based on the MD5 hash of a namespace identifier
   (which is a UUID) and a name (which is a "bytes" object or a string
   that will be encoded using UTF-8) according to **RFC 9562, §5.3**.

uuid.uuid4()

   Generate a random UUID in a cryptographically-secure method
   according to **RFC 9562, §5.4**.

uuid.uuid5(namespace, name)

   Generate a UUID based on the SHA-1 hash of a namespace identifier
   (which is a UUID) and a name (which is a "bytes" object or a string
   that will be encoded using UTF-8) according to **RFC 9562, §5.5**.

uuid.uuid6(node=None, clock_seq=None)

   Generate a UUID from a sequence number and the current time
   according to **RFC 9562, §5.6**.

   This is an alternative to "uuid1()" to improve database locality.

   When *node* is not specified, "getnode()" is used to obtain the
   hardware address as a 48-bit positive integer. When a sequence
   number *clock_seq* is not specified, a pseudo-random 14-bit
   positive integer is generated.

   If *node* or *clock_seq* exceed their expected bit count, only
   their least significant bits are kept.

   Added in version 3.14.

uuid.uuid7()

   Generate a time-based UUID according to **RFC 9562, §5.7**.

   For portability across platforms lacking sub-millisecond precision,
   UUIDs produced by this function embed a 48-bit timestamp and use a
   42-bit counter to guarantee monotonicity within a millisecond.

   Added in version 3.14.

uuid.uuid8(a=None, b=None, c=None)

   Generate a pseudo-random UUID according to **RFC 9562, §5.8**.

   When specified, the parameters *a*, *b* and *c* are expected to be
   positive integers of 48, 12 and 62 bits respectively. If they
   exceed their expected bit count, only their least significant bits
   are kept; non-specified arguments are substituted for a pseudo-
   random integer of appropriate size.

   By default, *a*, *b* and *c* are not generated by a
   cryptographically secure pseudo-random number generator (CSPRNG).
   Use "uuid4()" when a UUID needs to be used in a security-sensitive
   context.

   Added in version 3.14.

The "uuid" module defines the following namespace identifiers for use
with "uuid3()" or "uuid5()".

uuid.NAMESPACE_DNS

   Cuando se especifica este espacio de nombres, la cadena *name* es
   un nombre de dominio completamente calificado.

uuid.NAMESPACE_URL

   Cuando se especifica este espacio de nombres, la cadena *name* es
   una URL.

uuid.NAMESPACE_OID

   Cuando se especifica este espacio de nombres, la cadena *name* es
   un OID ISO.

uuid.NAMESPACE_X500

   Cuando se especifica este espacio de nombres, la cadena *name* es
   un X.500 DN en DER o un formato de salida de texto.

The "uuid" module defines the following constants for the possible
values of the "variant" attribute:

uuid.RESERVED_NCS

   Reservado para la compatibilidad con NCS.

uuid.RFC_4122

   Specifies the UUID layout given in **RFC 4122**. This constant is
   kept for backward compatibility even though **RFC 4122** has been
   superseded by **RFC 9562**.

uuid.RESERVED_MICROSOFT

   Reservado para la compatibilidad con Microsoft.

uuid.RESERVED_FUTURE

   Reservado para una futura definición.

The "uuid" module defines the special Nil and Max UUID values:

uuid.NIL

   A special form of UUID that is specified to have all 128 bits set
   to zero according to **RFC 9562, §5.9**.

   Added in version 3.14.

uuid.MAX

   A special form of UUID that is specified to have all 128 bits set
   to one according to **RFC 9562, §5.10**.

   Added in version 3.14.

Ver también:

  **RFC 9562** - A Universally Unique IDentifier (UUID) URN Namespace
     Esta especificación define un espacio de nombres de recursos
     uniforme para los UUID, el formato interno de los UUID y los
     métodos de generación de los UUID.

## Uso de la línea de comandos

Added in version 3.12.

The "uuid" module can be executed as a script from the command line.

   python -m uuid [-h] [-u {uuid1,uuid3,uuid4,uuid5,uuid6,uuid7,uuid8}] [-n NAMESPACE] [-N NAME]

Se aceptan las siguientes opciones:

-h, --help

   Muestra el mensaje de ayuda y libera la linea de comando.

-u <uuid>
--uuid <uuid>

   Especifica el nombre de la función que se utilizará para generar el
   uuid. Por defecto se utiliza "uuid4()".

   Distinto en la versión 3.14: Allow generating UUID versions 6, 7
   and 8.

-n <namespace>
--namespace <namespace>

   El espacio de nombres es un "UUID" o "@ns" donde "ns" es un UUID
   predefinido conocido dirigido por el nombre del espacio de nombres.
   Como "@dns", "@url", "@oid" y "@x500". Solo se requiere para las
   funciones "uuid3()" / "uuid5()".

-N <name>
--name <name>

   El nombre utilizado como parte de la generación del uuid. Solo se
   requiere para las funciones "uuid3()" / "uuid5()".

-C <num>
--count <num>

   Generate *num* fresh UUIDs.

   Added in version 3.14.

## Ejemplo

Here are some examples of typical usage of the "uuid" module:

   >>> import uuid

   >>> # make a UUID based on the host ID and current time
   >>> uuid.uuid1()
   UUID('a8098c1a-f86e-11da-bd1a-00112444be1e')

   >>> # make a UUID using an MD5 hash of a namespace UUID and a name
   >>> uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org')
   UUID('6fa459ea-ee8a-3ca4-894e-db77e160355e')

   >>> # make a random UUID
   >>> uuid.uuid4()
   UUID('16fd2706-8baf-433b-82eb-8c7fada847da')

   >>> # make a UUID using a SHA-1 hash of a namespace UUID and a name
   >>> uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org')
   UUID('886313e1-3b8a-5372-9b90-0c9aee199e5d')

   >>> # make a UUID from a string of hex digits (braces and hyphens ignored)
   >>> x = uuid.UUID('{00010203-0405-0607-0809-0a0b0c0d0e0f}')

   >>> # convert a UUID to a string of hex digits in standard form
   >>> str(x)
   '00010203-0405-0607-0809-0a0b0c0d0e0f'

   >>> # get the raw 16 bytes of the UUID
   >>> x.bytes
   b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f'

   >>> # make a UUID from a 16-byte string
   >>> uuid.UUID(bytes=x.bytes)
   UUID('00010203-0405-0607-0809-0a0b0c0d0e0f')

   >>> # get the Nil UUID
   >>> uuid.NIL
   UUID('00000000-0000-0000-0000-000000000000')

   >>> # get the Max UUID
   >>> uuid.MAX
   UUID('ffffffff-ffff-ffff-ffff-ffffffffffff')

   >>> # same as UUIDv1 but with fields reordered to improve DB locality
   >>> uuid.uuid6()
   UUID('1f0799c0-98b9-62db-92c6-a0d365b91053')

   >>> # get UUIDv7 creation (local) time as a timestamp in milliseconds
   >>> u = uuid.uuid7()
   >>> u.time
   1743936859822

   >>> # get UUIDv7 creation (local) time as a datetime object
   >>> import datetime as dt
   >>> dt.datetime.fromtimestamp(u.time / 1000)
   datetime.datetime(...)

   >>> # make a UUID with custom blocks
   >>> uuid.uuid8(0x12345678, 0x9abcdef0, 0x11223344)
   UUID('00001234-5678-8ef0-8000-000011223344')

## Ejemplo de línea de comandos

Here are some examples of typical usage of the "uuid" command-line
interface:

   # generate a random UUID - by default uuid4() is used
   $ python -m uuid

   # generate a UUID using uuid1()
   $ python -m uuid -u uuid1

   # generate a UUID using uuid5
   $ python -m uuid -u uuid5 -n @url -N example.com

   # generate 42 random UUIDs
   $ python -m uuid -C 42
