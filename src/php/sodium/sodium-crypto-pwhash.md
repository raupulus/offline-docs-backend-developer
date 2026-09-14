---
title: sodium_crypto_pwhash
description: Deriva una clave a partir de una contraseña, utilizando Argon2
source_url: https://www.php.net/manual/es/function.sodium-crypto-pwhash.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-pwhash.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76650
---

sodium_crypto_pwhash

Deriva una clave a partir de una contraseña, utilizando Argon2

## Descripción

```php
#[\SensitiveParameter] sodium_crypto_pwhash(int $length, string $password, string $salt, int $opslimit, int $memlimit, [int $algo]): string
```php

Esta función proporciona acceso de bajo nivel a la función de derivación de clave crypto_pwhash de libsodium. A menos que haya una razón específica para utilizar esta función, se deben utilizar las funciones `sodium_crypto_pwhash_str` o `password_hash` en su lugar.

Una razón común para utilizar esta función es derivar las semillas para las claves criptográficas a partir de una contraseña y un salt, y luego utilizar estas semillas para generar las claves reales necesarias para un uso específico (por ejemplo, `sodium_crypto_sign_detached`).

## Parámetros

`length`  
`int`; La longitud del hash de la contraseña a generar, en bytes.

`password`  
`string`; La contraseña para la cual generar un hash.

`salt`  
Un salt para añadir a la contraseña antes del hash. El salt debe ser impredecible, idealmente generado a partir de una buena fuente de números aleatorios como `random_bytes`, y tener una longitud de al menos `SODIUM_CRYPTO_PWHASH_SALTBYTES` bytes.

`opslimit`  
Representa una cantidad máxima de cálculos a realizar. Aumentar este número hará que la función requiera más ciclos de CPU para calcular una clave. Existen constantes disponibles para definir el límite de operaciones a valores adecuados según el uso previsto, en orden de fuerza: `SODIUM_CRYPTO_PWHASH_OPSLIMIT_INTERACTIVE`, `SODIUM_CRYPTO_PWHASH_OPSLIMIT_MODERATE` y `SODIUM_CRYPTO_PWHASH_OPSLIMIT_SENSITIVE`.

`memlimit`  
La cantidad máxima de RAM que la función utilizará, en bytes. Existen constantes para ayudar a elegir un valor adecuado, en orden de tamaño: `SODIUM_CRYPTO_PWHASH_MEMLIMIT_INTERACTIVE`, `SODIUM_CRYPTO_PWHASH_MEMLIMIT_MODERATE` y `SODIUM_CRYPTO_PWHASH_MEMLIMIT_SENSITIVE`. Típicamente, estos valores deberían asociarse con los valores opslimit correspondientes.

`algo`  
`int` Un número que indica el algoritmo de hash a utilizar. Por defecto `SODIUM_CRYPTO_PWHASH_ALG_DEFAULT` (el algoritmo actualmente recomendado, que puede cambiar de una versión de libsodium a otra), o explícitamente utilizando `SODIUM_CRYPTO_PWHASH_ALG_ARGON2ID13`, representando el algoritmo Argon2id versión 1.3.

## Valores devueltos

Devuelve la clave derivada. El valor de retorno es una cadena binaria del hash, no una representación codificada en ASCII, y no contiene información adicional sobre los parámetros utilizados para crear el hash, por lo que se deberá conservar esta información si alguna vez se necesita verificar la contraseña en el futuro. Utilice `sodium_crypto_pwhash_str` para evitar tener que hacer todo esto.

## Ejemplos

Ejemplo de `sodium_crypto_pwhash`

```
<?php
//Requerido para conservar el salt si alguna vez necesitamos verificar esta contraseña
$salt = random_bytes(SODIUM_CRYPTO_PWHASH_SALTBYTES);
//Utilizar bin2hex para mantener la salida legible
echo bin2hex(
    sodium_crypto_pwhash(
        16, // == 128 bits
        'password',
        $salt,
        SODIUM_CRYPTO_PWHASH_OPSLIMIT_INTERACTIVE,
        SODIUM_CRYPTO_PWHASH_MEMLIMIT_INTERACTIVE,
        SODIUM_CRYPTO_PWHASH_ALG_ARGON2ID13
    )
);
?>
   
```php

Resultado del ejemplo anterior es similar a:

    a18f346ba57992eb7e4ae6abf3fd30ee
