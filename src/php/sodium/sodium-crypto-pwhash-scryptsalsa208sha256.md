---
title: sodium_crypto_pwhash_scryptsalsa208sha256
description: Deriva una clave a partir de una contraseña, utilizando scrypt
source_url: https://www.php.net/manual/es/function.sodium-crypto-pwhash-scryptsalsa208sha256.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-pwhash-scryptsalsa208sha256.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76610
---

sodium_crypto_pwhash_scryptsalsa208sha256

Deriva una clave a partir de una contraseña, utilizando scrypt

## Descripción

```php
#[\SensitiveParameter] sodium_crypto_pwhash_scryptsalsa208sha256(int $length, string $password, string $salt, int $opslimit, int $memlimit): string
```php

Esta es la contraparte scrypt de `sodium_crypto_pwhash`.

Una razón común para utilizar esta función es derivar las semillas para las claves criptográficas a partir de una contraseña y un salt, y luego utilizar estas semillas para generar las claves reales necesarias para un uso específico (por ejemplo, `sodium_crypto_sign_detached`).

## Parámetros

`length`  
La longitud del hash de la contraseña a generar, en bytes.

`password`  
La contraseña para la cual se generará un hash.

`salt`  
Un salt que se añadirá a la contraseña antes del hash. El salt debe ser impredecible, idealmente generado a partir de una buena fuente de números aleatorios como `random_bytes`, y tener una longitud de al menos `SODIUM_CRYPTO_PWHASH_SCRYPTSALSA208SHA256_SALTBYTES` bytes.

`opslimit`  
Representa una cantidad máxima de cálculos a realizar. Aumentar este número hará que la función requiera más ciclos de CPU para calcular una clave. Existen constantes disponibles para definir el límite de operaciones a valores apropiados según el uso previsto, en orden de fuerza: `SODIUM_CRYPTO_PWHASH_SCRYPTSALSA208SHA256_OPSLIMIT_INTERACTIVE` y `SODIUM_CRYPTO_PWHASH_SCRYPTSALSA208SHA256_OPSLIMIT_SENSITIVE`.

`memlimit`  
La cantidad máxima de RAM que la función utilizará, en bytes. Existen constantes para ayudar a elegir un valor apropiado, en orden de tamaño: `SODIUM_CRYPTO_PWHASH_SCRYPTSALSA208SHA256_MEMLIMIT_INTERACTIVE` y `SODIUM_CRYPTO_PWHASH_SCRYPTSALSA208SHA256_MEMLIMIT_SENSITIVE`. Típicamente, estas deberían asociarse con los valores `opslimit` correspondientes.

## Valores devueltos

Una cadena de bytes de la longitud deseada.
