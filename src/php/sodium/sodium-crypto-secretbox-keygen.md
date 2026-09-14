---
title: sodium_crypto_secretbox_keygen
description: Genera una clave aleatoria para sodium_crypto_secretbox
source_url: https://www.php.net/manual/es/function.sodium-crypto-secretbox-keygen.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-secretbox-keygen.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76700
---

sodium_crypto_secretbox_keygen

Genera una clave aleatoria para sodium_crypto_secretbox

## Descripción

```php
sodium_crypto_secretbox_keygen(): string
```php

Genera una clave para ser utilizada con `sodium_crypto_secretbox` y `sodium_crypto_secretbox_open`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la string generada de bytes aleatorios criptográficamente seguros.

## Ejemplos

Ejemplo de `sodium_crypto_secretbox_keygen`

```
<?php
$key = sodium_crypto_secretbox_keygen();
var_dump( sodium_bin2hex( $key ) );
?>

    
```php

Resultado del ejemplo anterior es similar a:

    string(64) "88bd1dc51ec81984f3ddc5a8f59a3d95b647e2da3e879f1b9ceb0abd89e7286c"

Comparar `sodium_crypto_secretbox_keygen` con `random_bytes`

```
<?php
$key = sodium_crypto_secretbox_keygen();
$bytes = random_bytes( SODIUM_CRYPTO_SECRETBOX_KEYBYTES );
var_dump( mb_strlen( $key, '8bit' ) === mb_strlen( $bytes, '8bit' ) );
?>

    
```php

El ejemplo anterior mostrará:

    bool(true)

## Véase también

sodium_bin2hex

random_bytes
