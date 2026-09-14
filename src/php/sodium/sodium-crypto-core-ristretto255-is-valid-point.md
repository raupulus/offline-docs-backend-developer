---
title: sodium_crypto_core_ristretto255_is_valid_point
description: Determina si un punto está en la curva ristretto255
source_url: https://www.php.net/manual/es/function.sodium-crypto-core-ristretto255-is-valid-point.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-core-ristretto255-is-valid-point.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76350
---

sodium_crypto_core_ristretto255_is_valid_point

Determina si un punto está en la curva ristretto255

## Descripción

```php
sodium_crypto_core_ristretto255_is_valid_point(string $s): bool
```php

Determina si un punto está en la curva ristretto255, en forma canónica, en el subgrupo principal, y que el punto no tiene un orden pequeño. Disponible a partir de libsodium 1.0.18.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`s`  
Un punto en la curva elíptica.

## Valores devueltos

Devuelve `true` si `s` está en la curva ristretto255, `false` en caso contrario.

## Ejemplos

Ejemplo de `sodium_crypto_core_ristretto255_is_valid_point`

```
<?php

$foo = sodium_crypto_core_ristretto255_scalar_random();
$bar = sodium_crypto_scalarmult_ristretto255_base($foo);

var_dump(sodium_crypto_core_ristretto255_is_valid_point($bar));
?>

   
```php

El ejemplo anterior mostrará:

    bool(true)

## Véase también

sodium_crypto_core_ristretto255_scalar_random

sodium_crypto_scalarmult_ristretto255_base
