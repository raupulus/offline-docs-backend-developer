---
title: crypt
description: Hash de un solo sentido (indescifrable)
source_url: https://www.php.net/manual/es/function.crypt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/crypt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: false
translation_revision: d76a7fe17
order: 88700
---

crypt

Hash de un solo sentido (indescifrable)

> [!WARNING]
> Esta función no es capaz de manejar strings binarios (aún)!

## Descripción

```php
#[\SensitiveParameter] crypt(string $string, string $salt): string
```php

`crypt` devolverá una cadena con hash utilizando el algoritmo estándar de Unix basado en DES, o un algoritmo alternativo. La función `password_verify` es compatible con la función `crypt`. Así, una contraseña con hash de la función `crypt` puede ser utilizada con la función `password_verify`.

Anterior a PHP 8.0.0, el parámetro `salt` era opcional. Sin embargo, `crypt` crea un hash débil sin el `salt`, y genera un error `E_NOTICE` sin este. Asegúrese de especificar un salt lo suficientemente fuerte para una mejor seguridad.

`password_hash` utiliza un hash fuerte, genera un salt fuerte, y aplica todo automáticamente. `password_hash` es solo un gestor de `crypt` y es compatible con contraseñas con hash existentes. Se recomienda encarecidamente el uso de la función `password_hash`.

El tipo de hash es activado por el argumento `salt`. Si no se proporciona ningún `salt`, PHP generará dos caracteres (DES), a menos que el sistema predeterminado sea MD5, en cuyo caso se generará un `salt` compatible con MD5. PHP define una constante llamada `CRYPT_SALT_LENGTH` que permite conocer la longitud del `salt` disponible para el sistema de hash utilizado.

`crypt`, cuando se utiliza con el cifrado estándar DES, devuelve el `salt` en los dos primeros caracteres de la cadena devuelta. Solo utiliza los primeros 8 caracteres de `string`, lo que hace que todas las cadenas más largas, que tienen los mismos primeros 8 octetos, devuelvan el mismo resultado (siempre que el `salt` sea siempre el mismo).

Los siguientes tipos de hash son soportados:

- `CRYPT_STD_DES`: cifrado DES estándar de 2 caracteres desde la clase de caracteres "./0-9A-Za-z". El uso de caracteres inválidos en el salt hará fallar la función crypt().

- `CRYPT_EXT_DES`: Hash DES extendido. El "salt" será una cadena de 9 caracteres compuesta de un guion bajo, seguido de 4 caracteres del contador de iteración y luego 4 caracteres del "salt". Cada una de estas cadenas de 4 caracteres codifica 24 bits, el carácter menos significativo primero. Los valores de `0` a `63` serán codificados como `./0-9A-Za-z`. El uso de caracteres inválidos en el salt hará fallar la función crypt().

- `CRYPT_MD5`: hash MD5 de 12 caracteres que comienza con `$1$`

- `CRYPT_BLOWFISH`: hash Blowfish cuyo salt está compuesto de la siguiente manera: "\$2a\$", "\$2x\$" o "\$2y\$", un parámetro de 2 dígitos, `$`, y 22 caracteres del alfabeto "./0-9A-Za-z". El uso de caracteres fuera de esta clase en el salt hará que la función crypt() devuelva una cadena vacía (de longitud 0). El parámetro de 2 dígitos es el logaritmo base-2 del contador de iteración para el algoritmo de hash basado en Blowfish subyacente y debe estar en el rango 04-31. De manera similar, si se utiliza un valor fuera de este rango, la función crypt() fallará. Los hashes "\$2x\$" son potencialmente débiles; los hashes "\$2a\$" son compatibles y mitigan esta debilidad. Para nuevos hashes, "\$2y\$" debería ser utilizado.

- `CRYPT_SHA256` - Hash SHA-256 cuyo salt está compuesto de 16 caracteres prefijados por `$5$`. Si el salt comienza con `'rounds=<N>$'`, el valor numérico de N será utilizado para indicar cuántas veces el bucle de hash debe ser ejecutado, algo similar al parámetro en el algoritmo Blowfish. El valor predeterminado de `rounds` es 5000, el mínimo puede ser 1000 y el máximo, 999,999,999. Cualquier otra selección de N fuera de este rango será truncada al límite más cercano de los 2.

- `CRYPT_SHA512` - Hash SHA-512 cuyo salt está compuesto de 16 caracteres prefijados por `$6$`. Si el salt comienza con `'rounds=<N>$'`, el valor numérico de N será utilizado para indicar cuántas veces el bucle de hash debe ser ejecutado, algo similar al parámetro en el algoritmo Blowfish. El valor predeterminado de `rounds` es 5000, el mínimo puede ser 1000 y el máximo, 999,999,999. Cualquier otra selección de N fuera de este rango será truncada al límite más cercano de los 2.

## Parámetros

`string`  
La cadena a hashear.

> [!CAUTION]
> Si se utiliza el algoritmo `CRYPT_BLOWFISH`, el resultado del parámetro `string` será truncado a una longitud máxima de 72 octetos.

`salt`  
Si el argumento `salt` no es proporcionado, el comportamiento está definido por la implementación del algoritmo y puede provocar resultados inesperados.

## Valores devueltos

Devuelve la cadena con hash o una cadena que será inferior a 13 caracteres y que está garantizada para diferir del salt en caso de error.

> [!WARNING]
> Al validar contraseñas, debe utilizarse una función de comparación de cadenas que no sea vulnerable a ataques temporales para comparar la salida de la función `crypt` con el hash conocido previamente. PHP proporciona `hash_equals` para esto.

## Historial de cambios

| Versión | Descripción                  |
|---------|------------------------------|
| 8.0.0   | El `salt` ya no es opcional. |

## Ejemplos

Ejemplo con `crypt`

```
<?php
$user_input = 'rasmuslerdorf';
$hashed_password = '$6$rounds=1000000$NJy4rIPjpOaU$0ACEYGg/aKCY3v8O8AfyiO7CTfZQ8/W231Qfh2tRLmfdvFD6XfHk12u6hMr9cYIA4hnpjLNSTRtUwYr9km9Ij/';

// Validar un hash crypt() existente de una manera compatible con software no-PHP
if (hash_equals($hashed_password, crypt($user_input, $hashed_password))) {
   echo "¡Contraseña correcta!";
}
?>

    
```php

## Notas

> [!NOTE]
> No existe una función de descifrado, ya que la función `crypt` utiliza un algoritmo de un solo sentido (inyección).

## Véase también

`hash_equals`, `password_hash`, La página del manual Unix de la función crypt para más información
