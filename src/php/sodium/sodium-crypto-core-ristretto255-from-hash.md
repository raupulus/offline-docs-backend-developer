---
title: sodium_crypto_core_ristretto255_from_hash
description: Mapea un vector
source_url: https://www.php.net/manual/es/function.sodium-crypto-core-ristretto255-from-hash.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-core-ristretto255-from-hash.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76340
---

sodium_crypto_core_ristretto255_from_hash

Mapea un vector

## Descripción

```php
sodium_crypto_core_ristretto255_from_hash(string $s): string
```php

Mapea un vector `s` de 64 bytes a un elemento de grupo. Disponible a partir de libsodium 1.0.18.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`s`  
Un vector de 64 bytes.

## Valores devueltos

Devuelve una `string` aleatoria de 32 bytes.

## Ejemplos

Ejemplo de `sodium_crypto_core_ristretto255_from_hash`

```
<?php

$hashes = sodium_hex2bin(
    '5d1be09e3d0c82fc538112490e35701979d99e06ca3e2b5b54bffe8b4dc772c1' .
    '4d98b696a1bbfb5ca32c436cc61c16563790306c79eaca7705668b47dffe5bb6'
);
var_dump(sodium_bin2hex(sodium_crypto_core_ristretto255_from_hash($hashes)));
?>

   
```php

El ejemplo anterior mostrará:

    string(64) "3066f82a1a747d45120d1740f14358531a8f04bbffe6a819f86dfe50f44a0a46"

## Véase también

sodium_hex2bin

sodium_bin2hex

sodium_crypto_core_ristretto255_from_hash
