---
title: sodium_crypto_core_ristretto255_scalar_invert
description: Invierte un valor escalar
source_url: https://www.php.net/manual/es/function.sodium-crypto-core-ristretto255-scalar-invert.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-core-ristretto255-scalar-invert.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76390
---

sodium_crypto_core_ristretto255_scalar_invert

Invierte un valor escalar

## Descripción

```php
sodium_crypto_core_ristretto255_scalar_invert(string $s): string
```php

Invierte un valor escalar. Disponible a partir de libsodium 1.0.18.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`s`  
Valor escalar.

## Valores devueltos

Devuelve una `string` aleatoria de 32 bytes.

## Ejemplos

Ejemplo de `sodium_crypto_core_ristretto255_scalar_invert`

```
<?php

$foo = sodium_crypto_core_ristretto255_scalar_random();

$inverted = sodium_crypto_core_ristretto255_scalar_invert($foo);
$reInverted = sodium_crypto_core_ristretto255_scalar_invert($inverted);

var_dump(hash_equals($foo, $reInverted));
?>

   
```php

El ejemplo anterior mostrará:

    bool(true)

## Véase también

sodium_crypto_core_ristretto255_scalar_random
