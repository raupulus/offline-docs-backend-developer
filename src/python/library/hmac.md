---
title: '"hmac" --- Keyed-Hashing for Message Authentication'
source_url: https://docs.python.org/es/3
source_path: library/hmac.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2810
---

# "hmac" --- Keyed-Hashing for Message Authentication

**Código fuente:** Lib/hmac.py

======================================================================

This module implements the HMAC algorithm as described by **RFC
2104**. The interface allows to use any hash function with a *fixed*
digest size. In particular, extendable output functions such as
SHAKE-128 or SHAKE-256 cannot be used with HMAC.

hmac.new(key, msg=None, digestmod)

   Retorna un nuevo objeto hmac. *key* es un objeto *bytes* o
   *bytearray* que proporciona la clave secreta. Si *msg* está
   presente, se realiza la llamada al método "update(msg)".
   *digestmod* es el nombre del resumen, constructor o módulo del
   resumen para el objeto HMAC que se va a usar. Puede ser cualquier
   nombre adecuado para "hashlib.new()". Se requiere este argumento a
   pesar de su posición.

   Distinto en la versión 3.4: El parámetro *key* puede ser un objeto
   *bytes* o *bytearray*. El parámetro *msg* puede ser de cualquier
   tipo soportado por "hashlib". El parámetro *digestmod* puede ser el
   nombre del algoritmo de *hash*.

   Distinto en la versión 3.8: The *digestmod* argument is now
   required.  Pass it as a keyword argument to avoid awkwardness when
   you do not have an initial *msg*.

hmac.digest(key, msg, digest)

   Retorna el resumen de *msg* para una clave *key* secreta y un
   resumen *digest* dados. La función es equivalente a "HMAC(key, msg,
   digest).digest()", pero utiliza una implementación optimizada en C
   o *inline*, que es más rápida para mensajes que caben en memoria.
   Los parámetros *key*, *msg* y *digest* tienen el mismo significado
   que en "new()".

   Un detalle de la implementación de CPython: la implementación
   optimizada en C solo se usa cuando *digest* es una cadena de
   caracteres y el nombre de un algoritmo de resumen, que está
   soportado por OpenSSL.

   Added in version 3.7.

class hmac.HMAC

   Un objeto HMAC tiene los siguientes métodos:

HMAC.update(msg)

   Actualiza el objeto hmac con *msg*. Las llamadas repetidas
   equivalen a una sola llamada con la concatenación de todos los
   argumentos: "m.update(a); m.update(b)" es equivalente a "m.update(a
   + b)".

   Distinto en la versión 3.4: El parámetro *msg* puede ser de
   cualquier tipo soportado por "hashlib".

HMAC.digest()

   Retorna el resumen de los *bytes* que se pasaron al método
   "update()" hasta el momento. Este objeto *bytes* será de la misma
   longitud que el *digest_size* del resumen que se pasa al
   constructor. Puede contener *bytes* no ASCII, incluyendo *bytes*
   NUL.

   Advertencia:

     Cuando se compara la salida de "digest()" a un resumen provisto
     externamente durante una rutina de verificación, se recomienda
     utilizar la función "compare_digest()" en lugar del operador "=="
     para reducir la vulnerabilidad a ataques de temporización.

HMAC.hexdigest()

   Como "digest()" excepto que el resumen se retorna como una cadena
   de caracteres de dos veces la longitud conteniendo solo dígitos
   hexadecimales. Esto se puede utilizar para intercambiar el valor de
   forma segura en email u otros entornos no binarios.

   Advertencia:

     Cuando se compara la salida de "hexdigest()" a un resumen
     provisto externamente durante una rutina de verificación, se
     recomienda utilizar la función "compare_digest()" en lugar del
     operador "==" para reducir la vulnerabilidad a ataques de
     temporización.

HMAC.copy()

   Retorna una copia ("clon") del objeto hmac. Esto se puede utilizar
   para calcular de forma eficiente los resúmenes de las cadenas de
   caracteres que comparten una subcadena de caracteres inicial común.

Un objeto *hash* tiene los siguientes atributos:

HMAC.digest_size

   El tamaño del resumen HMAC resultante en *bytes*.

HMAC.block_size

   El tamaño de bloque interno del algoritmo de *hash* en *bytes*.

   Added in version 3.4.

HMAC.name

   El nombre canónico de este HMAC, siempre en minúsculas, por ejemplo
   "hmac-md5".

   Added in version 3.4.

Distinto en la versión 3.10: Removed the undocumented attributes
"HMAC.digest_cons", "HMAC.inner", and "HMAC.outer".

Este módulo también provee las siguiente funciones auxiliares:

hmac.compare_digest(a, b)

   Retorna "a == b". Esta función utiliza un enfoque diseñado para
   prevenir el análisis de temporización evitando el comportamiento de
   cortocircuito basado en contenido, haciéndolo adecuado para
   criptografía. *a* y *b* deben ser del mismo tipo: ya sea "str"
   (solo ASCII, como por ejemplo retornado por "HMAC.hexdigest()"), o
   un *objeto tipo binario*.

   Nota:

     Si *a* y *b* son de diferente longitud, o si ocurre un error, un
     ataque de temporización teóricamente podría revelar información
     sobre los tipos y longitudes de *a* y *b*—pero no sus valores.

   Added in version 3.3.

   Distinto en la versión 3.10: La función utiliza "CRYPTO_memcmp()"
   de OpenSSL internamente cuando está disponible.

Ver también:

  Módulo "hashlib"
     El módulo de Python que provee funciones de *hash* seguras.
