---
title: '"hashlib" --- Secure hashes and message digests'
source_url: https://docs.python.org/es/3
source_path: library/hashlib.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2790
---

# "hashlib" --- Secure hashes and message digests

**Código fuente:** Lib/hashlib.py

======================================================================

This module implements a common interface to many different hash
algorithms. Included are the FIPS secure hash algorithms SHA224,
SHA256, SHA384, SHA512, (defined in the FIPS 180-4 standard), the
SHA-3 series (defined in the FIPS 202 standard) as well as the legacy
algorithms SHA1 (formerly part of FIPS) and the MD5 algorithm (defined
in internet **RFC 1321**).

Nota:

  Si quieres las funciones de hash adler32 o crc32, están disponibles
  en el módulo "zlib".

## Algoritmos de hash

There is one constructor method named for each type of *hash*.  All
return a hash object with the same simple interface. For example: use
"sha256()" to create a SHA-256 hash object. You can now feed this
object with *bytes-like objects* (normally "bytes") using the "update"
method.  At any point you can ask it for the *digest* of the
concatenation of the data fed to it so far using the "digest()" or
"hexdigest()" methods.

To allow multithreading, the Python *GIL* is released while computing
a hash supplied more than 2047 bytes of data at once in its
constructor or ".update" method.

Constructors for hash algorithms that are always present in this
module are "sha1()", "sha224()", "sha256()", "sha384()", "sha512()",
"sha3_224()", "sha3_256()", "sha3_384()", "sha3_512()", "shake_128()",
"shake_256()", "blake2b()", and "blake2s()". "md5()" is normally
available as well, though it may be missing or blocked if you are
using a rare "FIPS compliant" build of Python. These correspond to
"algorithms_guaranteed".

Additional algorithms may also be available if your Python
distribution's "hashlib" was linked against a build of OpenSSL that
provides others. Others *are not guaranteed available* on all
installations and will only be accessible by name via "new()".  See
"algorithms_available".

Advertencia:

  Some algorithms have known hash collision weaknesses (including MD5
  and SHA1). Refer to Attacks on cryptographic hash algorithms and the
  hashlib-seealso section at the end of this document.

Added in version 3.6: SHA3 (Keccak) and SHAKE constructors
"sha3_224()", "sha3_256()", "sha3_384()", "sha3_512()", "shake_128()",
"shake_256()" were added. "blake2b()" and "blake2s()" were added.

Distinto en la versión 3.9: Todos los constructores hashlib toman un
argumento de solo palabra clave *usedforsecurity* con el valor
predeterminado "True". Un valor falso permite el uso de algoritmos
hash inseguros y bloqueados en entornos restringidos. "False" indica
que el algoritmo hash no se utiliza en un contexto de seguridad, por
ejemplo, como una función de compresión unidireccional no
criptográfica.

Distinto en la versión 3.9: Hashlib now uses SHA3 and SHAKE from
OpenSSL if it provides it.

Distinto en la versión 3.12: For any of the MD5, SHA1, SHA2, or SHA3
algorithms that the linked OpenSSL does not provide we fall back to a
verified implementation from the HACL* project.

## Usage

To obtain the digest of the byte string "b"Nobody inspects the
spammish repetition"":

   >>> import hashlib
   >>> m = hashlib.sha256()
   >>> m.update(b"Nobody inspects")
   >>> m.update(b" the spammish repetition")
   >>> m.digest()
   b'\x03\x1e\xdd}Ae\x15\x93\xc5\xfe\\\x00o\xa5u+7\xfd\xdf\xf7\xbcN\x84:\xa6\xaf\x0c\x95\x0fK\x94\x06'
   >>> m.hexdigest()
   '031edd7d41651593c5fe5c006fa5752b37fddff7bc4e843aa6af0c950f4b9406'

Más resumido:

>>> hashlib.sha256(b"Nobody inspects the spammish repetition").hexdigest()
'031edd7d41651593c5fe5c006fa5752b37fddff7bc4e843aa6af0c950f4b9406'

## Constructors

hashlib.new(name, [data, ]*, usedforsecurity=True)

   Is a generic constructor that takes the string *name* of the
   desired algorithm as its first parameter.  It also exists to allow
   access to the above listed hashes as well as any other algorithms
   that your OpenSSL library may offer.

Using "new()" with an algorithm name:

>>> h = hashlib.new('sha256')
>>> h.update(b"Nobody inspects the spammish repetition")
>>> h.hexdigest()
'031edd7d41651593c5fe5c006fa5752b37fddff7bc4e843aa6af0c950f4b9406'

hashlib.md5([data, ]*, usedforsecurity=True)

hashlib.sha1([data, ]*, usedforsecurity=True)

hashlib.sha224([data, ]*, usedforsecurity=True)

hashlib.sha256([data, ]*, usedforsecurity=True)

hashlib.sha384([data, ]*, usedforsecurity=True)

hashlib.sha512([data, ]*, usedforsecurity=True)

hashlib.sha3_224([data, ]*, usedforsecurity=True)

hashlib.sha3_256([data, ]*, usedforsecurity=True)

hashlib.sha3_384([data, ]*, usedforsecurity=True)

hashlib.sha3_512([data, ]*, usedforsecurity=True)

Named constructors such as these are faster than passing an algorithm
name to "new()".

## Attributes

Hashlib provides the following constant module attributes:

hashlib.algorithms_guaranteed

   Un conjunto que contiene los nombres de los algoritmos garantizados
   a ser soportados por este módulo en todas las plataformas. Ten en
   cuenta que 'md5' se encuentra en esta lista a pesar de que algunos
   proveedores ofrecen una extraña construcción Python "compatible con
   FIPS" que la excluye.

   Added in version 3.2.

hashlib.algorithms_available

   Un conjunto que contiene los nombres de los algoritmos de hash que
   están disponibles en el intérprete de Python en ejecución. Estos
   nombres serán reconocidos cuando sean pasados a "new()".
   "algorithms_guaranteed" siempre será un subconjunto. El mismo
   algoritmo puede aparecer múltiples veces en este conjunto bajo
   diferentes nombres (gracias a OpenSSL).

   Added in version 3.2.

## Hash Objects

Los siguientes valores son provistos como atributos constantes de los
objetos hash retornados por los constructores:

hash.digest_size

   El tamaño del hash resultante en bytes.

hash.block_size

   El tamaño del bloque interno del algoritmo de hash en bytes.

Un objeto hash tiene los siguientes atributos:

hash.name

   El nombre canónico de este hash, siempre en minúsculas y siempre
   adecuado como un parámetro a "new()" para crear otro hash de este
   tipo.

   Distinto en la versión 3.4: El atributo *name* ha estado presente
   en CPython desde su inicio, pero desde Python 3.4 no fue
   especificado formalmente, por lo que puede no existir en algunas
   plataformas.

Un objeto hash tiene los siguientes métodos:

hash.update(data)

   Actualiza el objeto de hash con el *bytes-like object*.
   Invocaciones repetidas son equivalentes a una única invocación con
   la concatenación de todos los argumentos: "m.update(a);
   m.update(b)" es equivalente a "m.update(a+b)".

hash.digest()

   Retorna el resumen de los datos pasados al método "update()" hasta
   el momento. Este es un objeto de bytes de tamaño "digest_size" el
   cual puede contener bytes en el rango completo desde 0 a 255.

hash.hexdigest()

   Como "digest()" excepto que el resumen es retornado como un objeto
   de cadena del doble de largo, conteniendo sólo dígitos
   hexadecimales. Este puede ser usado para intercambiar el valor de
   forma segura en correos electrónicos u otros entornos no binarios.

hash.copy()

   Retorna una copia ("clon") del objeto hash. Este puede ser usado
   para calcular eficientemente los resúmenes de datos compartiendo
   una subcadena inicial común.

## Resúmenes SHAKE de largo variable

hashlib.shake_128([data, ]*, usedforsecurity=True)

hashlib.shake_256([data, ]*, usedforsecurity=True)

Los algoritmos "shake_128()" y "shake_256()" proveen resúmenes de
largo variable con largo_en_bits//2 hasta 128 ó 256 bits de seguridad.
Como tales, sus métodos de resumen requieren un largo. El largo máximo
no está limitado por el algoritmo SHAKE.

shake.digest(length)

   Return the digest of the data passed to the "update()" method so
   far. This is a bytes object of size *length* which may contain
   bytes in the whole range from 0 to 255.

shake.hexdigest(length)

   Like "digest()" except the digest is returned as a string object of
   double length, containing only hexadecimal digits.  This may be
   used to exchange the value in email or other non-binary
   environments.

Example use:

>>> h = hashlib.shake_256(b'Nobody inspects the spammish repetition')
>>> h.hexdigest(20)
'44709d6fcb83d92a76dcb0b668c98e1b1d3dafe7'

## Cifrado de archivos

El módulo hashlib proporciona una función de ayuda para el cifrado
eficiente de un archivo o un objeto similar a un archivo.

hashlib.file_digest(fileobj, digest, /)

   Retorna un objeto digest que ha sido actualizado con el contenido
   del objeto de tipo archivo.

   *fileobj* must be a file-like object opened for reading in binary
   mode. It accepts file objects from  builtin "open()", "BytesIO"
   instances, SocketIO objects from "socket.socket.makefile()", and
   similar. *fileobj* must be opened in blocking mode, otherwise a
   "BlockingIOError" may be raised.

   The function may bypass Python's I/O and use the file descriptor
   from "fileno()" directly. *fileobj* must be assumed to be in an
   unknown state after this function returns or raises. It is up to
   the caller to close *fileobj*.

   *digest* debe ser un nombre de algoritmo de cifrado como *str*, un
   constructor de cifrado o un invocable que devuelva un objeto
   cifrado.

   Ejemplo:

   >>> import io, hashlib, hmac
   >>> with open("library/hashlib.rst", "rb") as f:
   ...     digest = hashlib.file_digest(f, "sha256")
   ...
   >>> digest.hexdigest()
   '...'

   >>> buf = io.BytesIO(b"somedata")
   >>> mac1 = hmac.HMAC(b"key", digestmod=hashlib.sha512)
   >>> digest = hashlib.file_digest(buf, lambda: mac1)

   >>> digest is mac1
   True
   >>> mac2 = hmac.HMAC(b"key", b"somedata", digestmod=hashlib.sha512)
   >>> mac1.digest() == mac2.digest()
   True

   Added in version 3.11.

   Distinto en la versión 3.14: Now raises a "BlockingIOError" if the
   file is opened in non-blocking mode. Previously, spurious null
   bytes were added to the digest.

## Derivación de clave

Los algoritmos de derivación de clave y estiramiento de clave están
diseñados para el cifrado seguro de contraseña. Algoritmos ingenuos
como "sha1(password)" no son resistentes contra ataques de fuerza
bruta. Una buena función hash de contraseña debe ser afinable, lenta e
incluir una sal.

hashlib.pbkdf2_hmac(hash_name, password, salt, iterations, dklen=None)

   La función provee contraseñas PKCS#5 basadas en función de
   derivación de clave 2. Usa HMAC como función de pseudoaleatoriedad.

   La cadena *hash_name* es el nombre deseado del algoritmo de resumen
   de hash para HMAC, ej. 'sha1' o 'sha256'. *password* y *salt* son
   interpretados como búferes de bytes. Aplicaciones y bibliotecas
   deberían limitar *password* a un largo razonable (ej. 1024). *salt*
   debería ser sobre 16 o más bytes desde una fuente adecuada, ej.
   "os.urandom()".

   El número de *iterations* debe elegirse en función del algoritmo de
   cifrado y la potencia de cálculo. A partir de 2022, se sugieren
   cientos de miles de iteraciones de SHA-256. Para saber por qué y
   cómo elegir lo mejor para su aplicación, lea el *Apéndice A.2.2* de
   NIST-SP-800-132. Las respuestas sobre stackexchange pbkdf2
   iterations question  lo explican en detalle.

   *dklen* is the length of the derived key in bytes. If *dklen* is
   "None" then the digest size of the hash algorithm *hash_name* is
   used, e.g. 64 for SHA-512.

   >>> from hashlib import pbkdf2_hmac
   >>> our_app_iters = 500_000  # Application specific, read above.
   >>> dk = pbkdf2_hmac('sha256', b'password', b'bad salt' * 2, our_app_iters)
   >>> dk.hex()
   '15530bba69924174860db778f2c6f8104d3aaf9d26241840c8c4a641c8d000a9'

   Function only available when Python is compiled with OpenSSL.

   Added in version 3.4.

   Distinto en la versión 3.12: Function now only available when
   Python is built with OpenSSL. The slow pure Python implementation
   has been removed.

hashlib.scrypt(password, *, salt, n, r, p, maxmem=0, dklen=64)

   La función provee una contraseña scrypt basada en una función
   derivación de clave como es definida en **RFC 7914**.

   *password* y *salt* deben ser *objetos de bytes*. Aplicaciones y
   bibliotecas deberían limitar *password* a un largo razonable (ej.
   1024). *salt* debería ser aproximadamente 16 o más bytes de una
   fuente adecuada, ej. "os.unrandom()".

   *n* is the CPU/Memory cost factor, *r* the block size, *p*
   parallelization factor and *maxmem* limits memory (OpenSSL 1.1.0
   defaults to 32 MiB). *dklen* is the length of the derived key in
   bytes.

   Added in version 3.6.

## BLAKE2

BLAKE2 es una función de hash criptográfico definida en **RFC 7693**
que viene en dos sabores:

* **BLAKE2b**, optimizada para plataformas de 64 bits y produce
  resúmenes de cualquier tamaño entre 1 y 64 bytes,

* **BLAKE2s**, optimizada para plataformas de 8 a 32 bits y produce
  resúmenes de cualquier tamaño entre 1 y 32 bytes.

BLAKE2 proporciona el **modo keyed** (un remplazamiento más simple
rápido para HMAC), **cifrado salado** (*salted hashing*),
**personalización** y **cifrado de árbol**.

Hash objects from this module follow the API of standard library's
"hashlib" objects.

### Creando objetos hash

Se crean nuevos objetos hash invocando a las funciones de constructor:

hashlib.blake2b(data=b'', *, digest_size=64, key=b'', salt=b'', person=b'', fanout=1, depth=1, leaf_size=0, node_offset=0, node_depth=0, inner_size=0, last_node=False, usedforsecurity=True)

hashlib.blake2s(data=b'', *, digest_size=32, key=b'', salt=b'', person=b'', fanout=1, depth=1, leaf_size=0, node_offset=0, node_depth=0, inner_size=0, last_node=False, usedforsecurity=True)

Estas funciones retornan los objetos hash correspondientes para
calcular BLAKE2b o BLAKE2s. Ellas toman opcionalmente estos parámetros
generales:

* *data*: trozo inicial de datos a cifrar, el cual debe ser un *bytes-
  like object*. Puede ser pasado sólo como argumento posicional.

* *digest_size*: tamaño del resumen de salida en bytes.

* *key*: clave para el cifrado de clave (*keyed hashing*) (hasta 64
  bytes para BLAKE2b, hasta 32 bytes para BLAKE2s).

* *salt*: sal para el cifrado aleatorio (hasta 16 bytes para BLAKE2b,
  hasta 8 bytes para BLAKE2s).

* *person*: cadena de personalización (hasta 16 bytes para BLAKE2b,
  hasta 8 bytes para BLAKE2s).

La siguiente tabla muestra los límites para parámetros generales (en
bytes):

+---------+-------------+----------+-----------+-------------+
| Cifrado | digest_size | len(key) | len(salt) | len(person) |
|=========|=============|==========|===========|=============|
## | BLAKE2b | 64          | 64       | 16        | 16          |

## | BLAKE2s | 32          | 32       | 8         | 8           |

Nota:

  La especificación BLAKE2 define largos constantes para los
  parámetros de sal y personalización, sin embargo, por conveniencia,
  esta implementación acepta cadenas de bytes de cualquier tamaño
  hasta el largo especificado. Si el largo del parámetro es menor que
  el especificado, es acolchado con ceros, por lo tanto, por ejemplo,
  "b'salt'" y "b'salt\x00'" es el mismo valor. (Este no es el caso
  para *key*.)

Estos tamaños están disponibles como constantes del módulo descritas
abajo.

Las funciones constructoras también aceptan los siguientes parámetros
de cifrado de árbol:

* *fanout*: despliegue en abanico (0 a 255, 0 si ilimitado, 1 en modo
  secuencial).

* *depth*: profundidad máxima del árbol (1 a 255, 255 si ilimitado, 1
  en modo secuencial).

* *leaf_size*: tamaño máximo en bytes de hoja (0 a "2**32-1", 0 si
  ilimitado o en modo secuencial).

* *node_offset*: desplazamiento del nodo (0 a "2**64-1" para BLAKE2b,
  0 a "2**48-1" para BLAKE2s, 0 para la primera hoja más a la
  izquierda, o en modo secuencial).

* *node_depth*: profundidad de nodo (0 a 255, 0 para hojas o en modo
  secuencial).

* *inner_size*: tamaño interno del resumen (0 a 64 para BLAKE2b, 0 a
  32 para BLAKE2s, 0 en modo secuencial).

* *last_node*: booleano indicando si el nodo procesado es el último
  ("False" para modo secuencial).

   [imagen: Explicación de los parámetros del modo árbol.][imagen]

See section 2.10 in BLAKE2 specification for comprehensive review of
tree hashing.

### Constantes

blake2b.SALT_SIZE

blake2s.SALT_SIZE

Largo de sal (largo máximo aceptado por los constructores).

blake2b.PERSON_SIZE

blake2s.PERSON_SIZE

Largo de cadena de personalización (largo máximo aceptado por los
constructores).

blake2b.MAX_KEY_SIZE

blake2s.MAX_KEY_SIZE

Tamaño máximo de clave.

blake2b.MAX_DIGEST_SIZE

blake2s.MAX_DIGEST_SIZE

Tamaño máximo de resumen que puede producir la función hash.

### Ejemplos

#### Cifrado simple

To calculate hash of some data, you should first construct a hash
object by calling the appropriate constructor function ("blake2b()" or
"blake2s()"), then update it with the data by calling "update()" on
the object, and, finally, get the digest out of the object by calling
"digest()" (or "hexdigest()" for hex-encoded string).

>>> from hashlib import blake2b
>>> h = blake2b()
>>> h.update(b'Hello world')
>>> h.hexdigest()
'6ff843ba685842aa82031d3f53c48b66326df7639a63d128974c5c14f31a0f33343a8c65551134ed1ae0f2b0dd2bb495dc81039e3eeb0aa1bb0388bbeac29183'

Como atajo, puedes pasar el primer trozo de datos para actualizar
directamente el constructor como el argumento posicional:

>>> from hashlib import blake2b
>>> blake2b(b'Hello world').hexdigest()
'6ff843ba685842aa82031d3f53c48b66326df7639a63d128974c5c14f31a0f33343a8c65551134ed1ae0f2b0dd2bb495dc81039e3eeb0aa1bb0388bbeac29183'

Puedes invocar "hash.update()" tantas veces como necesites para
actualizar el hash iterativamente:

>>> from hashlib import blake2b
>>> items = [b'Hello', b' ', b'world']
>>> h = blake2b()
>>> for item in items:
...     h.update(item)
...
>>> h.hexdigest()
'6ff843ba685842aa82031d3f53c48b66326df7639a63d128974c5c14f31a0f33343a8c65551134ed1ae0f2b0dd2bb495dc81039e3eeb0aa1bb0388bbeac29183'

#### Usar diferentes tamaños de resumen

BLAKE2 tiene tamaño de resúmenes configurables de hasta 64 bytes para
BLAKE2b y 32 bytes para BLAKE2s. Por ejemplo, para remplazar SHA-1 con
BLAKE2b sin cambiar el tamaño de la salida, puedes decirle a BLAKE2b
que produzca resúmenes de 20 bytes:

>>> from hashlib import blake2b
>>> h = blake2b(digest_size=20)
>>> h.update(b'Replacing SHA1 with the more secure function')
>>> h.hexdigest()
'd24f26cf8de66472d58d4e1b1774b4c9158b1f4c'
>>> h.digest_size
20
>>> len(h.digest())
20

Objetos hash con diferentes tamaños de resumen tienen salidas
completamente diferentes (hashes más cortos *no* son prefijos de
hashes más largos); BLAKE2b y BLAKE2s producen salidas diferentes
incluso si el largo de salida es el mismo:

>>> from hashlib import blake2b, blake2s
>>> blake2b(digest_size=10).hexdigest()
'6fa1d8fcfd719046d762'
>>> blake2b(digest_size=11).hexdigest()
'eb6ec15daf9546254f0809'
>>> blake2s(digest_size=10).hexdigest()
'1bf21a98c78a1c376ae9'
>>> blake2s(digest_size=11).hexdigest()
'567004bf96e4a25773ebf4'

#### Cifrado de clave

El cifrado de clave puede ser usado para autentificación como un
remplazo más rápido y simple para Código de autentificación de
mensajes en clave-hash (HMAC). BLAKE2 puede ser usado de forma segura
en modo de prefijo MAC gracias a la propiedad de indiferenciabilidad
heredada de BLAKE.

Este ejemplo muestra como obtener un código de autentificación
(codificado como hexadecimal) de 128 bits para el mensaje "b'message
data'" con la clave "b'pseudorandom key'":

   >>> from hashlib import blake2b
   >>> h = blake2b(key=b'pseudorandom key', digest_size=16)
   >>> h.update(b'message data')
   >>> h.hexdigest()
   '3d363ff7401e02026f4a4687d4863ced'

Como ejemplo práctico, una aplicación web puede firmar simétricamente
cookies enviadas a los usuarios y verificarlas más tarde para asegurar
que no fueron manipuladas con:

   >>> from hashlib import blake2b
   >>> from hmac import compare_digest
   >>>
   >>> SECRET_KEY = b'pseudorandomly generated server secret key'
   >>> AUTH_SIZE = 16
   >>>
   >>> def sign(cookie):
   ...     h = blake2b(digest_size=AUTH_SIZE, key=SECRET_KEY)
   ...     h.update(cookie)
   ...     return h.hexdigest().encode('utf-8')
   >>>
   >>> def verify(cookie, sig):
   ...     good_sig = sign(cookie)
   ...     return compare_digest(good_sig, sig)
   >>>
   >>> cookie = b'user-alice'
   >>> sig = sign(cookie)
   >>> print("{0},{1}".format(cookie.decode('utf-8'), sig))
   user-alice,b'43b3c982cf697e0c5ab22172d1ca7421'
   >>> verify(cookie, sig)
   True
   >>> verify(b'user-bob', sig)
   False
   >>> verify(cookie, b'0102030405060708090a0b0c0d0e0f00')
   False

Incluso aunque hay un modo de cifrado de claves nativo, BLAKE2 puede,
por supuesto, ser usado en construcción de HMAC con el módulo "hmac":

   >>> import hmac, hashlib
   >>> m = hmac.new(b'secret key', digestmod=hashlib.blake2s)
   >>> m.update(b'message')
   >>> m.hexdigest()
   'e3c8102868d28b5ff85fc35dda07329970d1a01e273c37481326fe0c861c8142'

#### Cifrado aleatorio

Definiendo el parámetro *salt* los usuarios pueden introducir
aleatoriedad a la función hash. El cifrado aleatorio es útil para
proteger contra ataques de colisión en la función hash usada en firmas
digitales.

   El cifrado aleatorio está diseñado para situaciones en las que una
   parte, el preparador del mensaje, genera todo o parte de un mensaje
   para ser firmado por una segunda parte, el firmante del mensaje. Si
   el preparador del mensaje es capaz de encontrar colisiones de
   funciones hash criptográficas (ej., dos mensajes produciendo el
   mismo valor de hash), entonces ellos pueden preparar versiones
   significativas del mensaje que producirían el mismo valor de hash y
   firma digital, pero con diferentes resultados (ej., transfiriendo
   1,000,000 $ a una cuenta, en lugar de 10 $), Las funciones de hash
   criptográfico han sido diseñadas con resistencia de colisión como
   objetivo principal, pero la concentración actual en el ataque a las
   funciones hash criptográficas puede resultar en una función hash
   criptográfica dada que provea menor resistencia de colisión de la
   esperada. El cifrado aleatorio ofrece al firmante protección
   adicional reduciendo la probabilidad de que un preparador puede
   generar dos o más mensajes que en última instancia producen el
   mismo valor hash durante el proceso de generación de la firma
   digital, --- incluso si es práctico encontrar colisiones para la
   función hash. Sin embargo, el uso de cifrado aleatorio puede
   reducir la cantidad de seguridad provista por una firma digital
   cuando todas las porciones del mensaje son preparadas por el
   firmante.

   (NIST SP-800-106 "Randomized Hashing for Digital Signatures")

En BLAKE2 la sal es procesada como una entrada de una vez a la función
hash durante la inicialización, en lugar de como una entrada para cada
función de compresión.

Advertencia:

  *Salted hashing* (or just hashing) with BLAKE2 or any other general-
  purpose cryptographic hash function, such as SHA-256, is not
  suitable for hashing passwords.  See BLAKE2 FAQ for more
  information.

>>> import os
>>> from hashlib import blake2b
>>> msg = b'some message'
>>> # Calculate the first hash with a random salt.
>>> salt1 = os.urandom(blake2b.SALT_SIZE)
>>> h1 = blake2b(salt=salt1)
>>> h1.update(msg)
>>> # Calculate the second hash with a different random salt.
>>> salt2 = os.urandom(blake2b.SALT_SIZE)
>>> h2 = blake2b(salt=salt2)
>>> h2.update(msg)
>>> # The digests are different.
>>> h1.digest() != h2.digest()
True

#### Personalización

A veces es útil forzar a la función hash para producir diferentes
resúmenes para la misma entrada para diferentes propósitos. Citando a
los autores de la función hash Skein:

   Recomendamos que todos los diseñadores de aplicaciones consideren
   seriamente hacer esto; hemos visto muchos protocolos donde un hash
   que es calculado en una parte del protocolo puede ser usado en una
   parte completamente diferente porque dos cálculos hash fueron
   realizados en datos similares o relacionados, y el atacante puede
   forzar a la aplicación a hacer las entradas hash iguales.
   Personalizar cada función hash usada en el protocolo resumidamente
   detiene este tipo de ataque.

   (The Skein Hash Function Family, p. 21)

BLAKE2 puede ser personalizado pasando bytes al argumento *person*:

   >>> from hashlib import blake2b
   >>> FILES_HASH_PERSON = b'MyApp Files Hash'
   >>> BLOCK_HASH_PERSON = b'MyApp Block Hash'
   >>> h = blake2b(digest_size=32, person=FILES_HASH_PERSON)
   >>> h.update(b'the same content')
   >>> h.hexdigest()
   '20d9cd024d4fb086aae819a1432dd2466de12947831b75c5a30cf2676095d3b4'
   >>> h = blake2b(digest_size=32, person=BLOCK_HASH_PERSON)
   >>> h.update(b'the same content')
   >>> h.hexdigest()
   'cf68fb5761b9c44e7878bfb2c4c9aea52264a80b75005e65619778de59f383a3'

Se puede usar también personalización en conjunto con el modo de clave
para derivar diferentes claves desde una sola.

>>> from hashlib import blake2s
>>> from base64 import b64decode, b64encode
>>> orig_key = b64decode(b'Rm5EPJai72qcK3RGBpW3vPNfZy5OZothY+kHY6h21KM=')
>>> enc_key = blake2s(key=orig_key, person=b'kEncrypt').digest()
>>> mac_key = blake2s(key=orig_key, person=b'kMAC').digest()
>>> print(b64encode(enc_key).decode('utf-8'))
rbPb15S/Z9t+agffno5wuhB77VbRi6F9Iv2qIxU7WHw=
>>> print(b64encode(mac_key).decode('utf-8'))
G9GtHFE1YluXY1zWPlYk1e/nWfu0WSEb0KRcjhDeP/o=

#### Modo de árbol

Aquí hay un ejemplo de cifrar un árbol mínimo con dos nodos de hoja:

     10
    /  \
   00  01

Este ejemplo usa resúmenes internos de 64 bytes, y retorna el resumen
final de 32 bytes:

   >>> from hashlib import blake2b
   >>>
   >>> FANOUT = 2
   >>> DEPTH = 2
   >>> LEAF_SIZE = 4096
   >>> INNER_SIZE = 64
   >>>
   >>> buf = bytearray(6000)
   >>>
   >>> # Left leaf
   ... h00 = blake2b(buf[0:LEAF_SIZE], fanout=FANOUT, depth=DEPTH,
   ...               leaf_size=LEAF_SIZE, inner_size=INNER_SIZE,
   ...               node_offset=0, node_depth=0, last_node=False)
   >>> # Right leaf
   ... h01 = blake2b(buf[LEAF_SIZE:], fanout=FANOUT, depth=DEPTH,
   ...               leaf_size=LEAF_SIZE, inner_size=INNER_SIZE,
   ...               node_offset=1, node_depth=0, last_node=True)
   >>> # Root node
   ... h10 = blake2b(digest_size=32, fanout=FANOUT, depth=DEPTH,
   ...               leaf_size=LEAF_SIZE, inner_size=INNER_SIZE,
   ...               node_offset=0, node_depth=1, last_node=True)
   >>> h10.update(h00.digest())
   >>> h10.update(h01.digest())
   >>> h10.hexdigest()
   '3ad2a9b37c6070e374c7a8c508fe20ca86b6ed54e286e93a0318e95e881db5aa'

### Créditos

BLAKE2 fue diseñado por *Jean-Philippe Aumasson*, *Samuel Neves*,
*Zooko Wilcox-O'Hearn* y *Christian Winnerlein* basado en el SHA-3
finalista BLAKE creado por *Jean-Philippe Aumasson*, *Luca Henzen*,
*Willi Meier* y *Raphael C.-W. Phan*.

Usa el algoritmo núcleo del cifrado ChaCha diseñado por *Daniel J.
Bernstein*.

La implementación stdlib está basada en el módulo pyblake2. Fue
escrita por *Dmitry Chestnykh* basada en la implementación C escrita
por *Samuel Neves*. La documentación fue copiada desde pyblake2 y
escrita por *Dmitry Chestnykh*.

El código C fue parcialmente reescrito para Python por *Christian
Heimes*.

La siguiente dedicación de dominio público aplica tanto para la
implementación de la función hash C, el código de extensión y su
documentación:

   En la medida en que la ley lo permite, el/los autor/es han dedicado
   todos los derechos de autor y los derechos relacionados y vecinos
   de este software al dominio público mundial. Este software se
   distribuye sin ninguna garantía.

   Deberías haber recibido una copia de la Dedicación CC0 de Dominio
   Público junto a este software. Si no, consulta
   https://creativecommons.org/publicdomain/zero/1.0/.

Las siguientes personas han ayudado con el desarrollo o contribuyeron
con sus cambios al proyecto y el dominio público de acuerdo a Creative
Commons Public Domain Dedication 1.0 Universal:

* *Alexandr Sokolovskiy*

Ver también:

  Módulo "hmac"
     Un módulo para generar mensajes de códigos de autentificación
     usando hashes.

  Módulo "base64"
     Otra forma de codificar hashes binarios para entornos no
     binarios.

  https://nvlpubs.nist.gov/nistpubs/fips/nist.fips.180-4.pdf
     The FIPS 180-4 publication on Secure Hash Algorithms.

  https://csrc.nist.gov/pubs/fips/202/final
     The FIPS 202 publication on the SHA-3 Standard.

  https://www.blake2.net/
     Sitio web oficial de BLAKE2.

  https://en.wikipedia.org/wiki/Cryptographic_hash_function
     Artículo de Wikipedia con información sobre cuáles algoritmos
     tienen errores conocidos y lo que eso significa con respecto a su
     uso.

  https://www.ietf.org/rfc/rfc8018.txt
     PKCS #5: Password-Based Cryptography Specification Version 2.1

  https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication8
  00-132.pdf
     Recomendación de NIST para la derivación de claves basadas en
     contraseña.
