---
title: '"secrets" --- Generate secure random numbers for managing secrets'
source_url: https://docs.python.org/es/3
source_path: library/secrets.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3720
---

# "secrets" --- Generate secure random numbers for managing secrets

Added in version 3.6.

**Código fuente:** Lib/secrets.py

======================================================================

The "secrets" module is used for generating cryptographically strong
random numbers suitable for managing data such as passwords, account
authentication, security tokens, and related secrets.

In particular, "secrets" should be used in preference to the default
pseudo-random number generator in the "random" module, which is
designed for modelling and simulation, not security or cryptography.

Ver también: **PEP 506**

## Números aleatorios

The "secrets" module provides access to the most secure source of
randomness that your operating system provides.

class secrets.SystemRandom

   Una clase para generar números aleatorios utilizando las fuentes de
   mayor calidad que proporciona el sistema operativo. Ver
   "random.SystemRandom" para más detalles.

secrets.choice(seq)

   Retorna un elemento elegido aleatoriamente a partir de una
   secuencia no vacía.

secrets.randbelow(exclusive_upper_bound)

   Return a random int in the range [0, *exclusive_upper_bound*).

secrets.randbits(k)

   Return a non-negative int with *k* random bits.

## Generando tokens

The "secrets" module provides functions for generating secure tokens,
suitable for applications such as password resets, hard-to-guess URLs,
and similar.

secrets.token_bytes(nbytes=None)

   Return a random byte string containing *nbytes* number of bytes.

   If *nbytes* is not specified or "None", "DEFAULT_ENTROPY" is used
   instead.

      >>> token_bytes(16)
      b'\xebr\x17D*t\xae\xd4\xe3S\xb6\xe2\xebP1\x8b'

secrets.token_hex(nbytes=None)

   Return a random text string, in hexadecimal.  The string has
   *nbytes* random bytes, each byte converted to two hex digits.

   If *nbytes* is not specified or "None", "DEFAULT_ENTROPY" is used
   instead.

      >>> token_hex(16)
      'f9bf78b9a18ce6d46a0cd2b0b86df9da'

secrets.token_urlsafe(nbytes=None)

   Return a random URL-safe text string, containing *nbytes* random
   bytes.  The text is Base64 encoded, so on average each byte results
   in approximately 1.3 characters.

   If *nbytes* is not specified or "None", "DEFAULT_ENTROPY" is used
   instead.

      >>> token_urlsafe(16)
      'Drmhze6EPcv0fN_81Bj-nA'

### ¿Cuántos bytes deben tener los tokens?

To be secure against brute-force attacks, tokens need to have
sufficient randomness.  Unfortunately, what is considered sufficient
will necessarily increase as computers get more powerful and able to
make more guesses in a shorter period.  As of 2015, it is believed
that 32 bytes (256 bits) of randomness is sufficient for the typical
use-case expected for the "secrets" module.

Para quienes quieran gestionar la longitud de sus propios tokens,
pueden especificar explícitamente cuánta aleatoriedad se utiliza para
los tokens  dando un argumento "int" a las funciones "token_*". Ese
argumento se toma como el número de bytes de aleatoriedad a utilizar.

Otherwise, if no argument is provided, or if the argument is "None",
the "token_*" functions use "DEFAULT_ENTROPY" instead.

secrets.DEFAULT_ENTROPY

   Default number of bytes of randomness used by the "token_*"
   functions.

   The exact value is subject to change at any time, including during
   maintenance releases.

## Otras funciones

secrets.compare_digest(a, b)

   Return "True" if strings or *bytes-like objects* *a* and *b* are
   equal, otherwise "False", using a "constant-time compare" to reduce
   the risk of timing attacks. See "hmac.compare_digest()" for
   additional details.

## Recetas y mejores prácticas

This section shows recipes and best practices for using "secrets" to
manage a basic level of security.

Generar una contraseña alfanumérica de ocho caracteres:

   import string
   import secrets
   alphabet = string.ascii_letters + string.digits
   password = ''.join(secrets.choice(alphabet) for i in range(8))

Nota:

  Applications should not **store passwords in a recoverable format**,
  whether plain text or encrypted.  They should be salted and hashed
  using a cryptographically strong one-way (irreversible) hash
  function.

Generar una contraseña alfanumérica de diez caracteres con al menos un
carácter en minúscula, al menos un carácter en mayúscula y al menos
tres dígitos:

   import string
   import secrets
   alphabet = string.ascii_letters + string.digits
   while True:
       password = ''.join(secrets.choice(alphabet) for i in range(10))
       if (any(c.islower() for c in password)
               and any(c.isupper() for c in password)
               and sum(c.isdigit() for c in password) >= 3):
           break

Generar una contraseña al estilo XKCD:

   import secrets
   # On standard Linux systems, use a convenient dictionary file.
   # Other platforms may need to provide their own word-list.
   with open('/usr/share/dict/words') as f:
       words = [word.strip() for word in f]
       password = ' '.join(secrets.choice(words) for i in range(4))

Generar una URL temporal difícil de adivinar que contenga un token de
seguridad adecuado para la recuperación de contraseñas:

   import secrets
   url = 'https://example.com/reset=' + secrets.token_urlsafe()
