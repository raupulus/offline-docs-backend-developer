---
title: sodium_crypto_core_ristretto255_scalar_add
description: Añade un valor escalar
source_url: https://www.php.net/manual/es/function.sodium-crypto-core-ristretto255-scalar-add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-core-ristretto255-scalar-add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76370
---

sodium_crypto_core_ristretto255_scalar_add

Añade un valor escalar

## Descripción

```php
sodium_crypto_core_ristretto255_scalar_add(string $x, string $y): string
```php

Añade un elemento `y` a `x`. Disponible a partir de libsodium 1.0.18.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`x`  
Escalar que representa la coordenada X.

`y`  
Escalar que representa la coordenada Y.

## Valores devueltos

Devuelve una `string` aleatoria de 32 bytes.

## Ejemplos

Ejemplo de `sodium_crypto_core_ristretto255_scalar_add`

```
<?php

$foo = sodium_crypto_core_ristretto255_scalar_random();
$bar = sodium_crypto_core_ristretto255_scalar_random();

$value = sodium_crypto_core_ristretto255_scalar_add($foo, $bar);
$value = sodium_crypto_core_ristretto255_scalar_sub($value, $bar);

var_dump(hash_equals($foo, $value));
?>

   
```php

El ejemplo anterior mostrará:

    bool(true)

## Véase también

sodium_crypto_core_ristretto255_scalar_random

sodium_crypto_core_ristretto255_scalar_sub
