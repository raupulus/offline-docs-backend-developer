---
title: sodium_crypto_core_ristretto255_scalar_negate
description: Invierte el signo de un valor escalar
source_url: https://www.php.net/manual/es/function.sodium-crypto-core-ristretto255-scalar-negate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-core-ristretto255-scalar-negate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76410
---

sodium_crypto_core_ristretto255_scalar_negate

Invierte el signo de un valor escalar

## Descripción

```php
sodium_crypto_core_ristretto255_scalar_negate(string $s): string
```php

Invierte el signo de un valor escalar. Disponible a partir de libsodium 1.0.18.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`s`  
Valor escalar.

## Valores devueltos

Devuelve una `string` aleatoria de 32 bytes.

## Ejemplos

Ejemplo de `sodium_crypto_core_ristretto255_scalar_negate`

```
<?php

$foo = sodium_crypto_core_ristretto255_scalar_random();

$negate = sodium_crypto_core_ristretto255_scalar_negate($foo);
$reNegate = sodium_crypto_core_ristretto255_scalar_negate($negate);

var_dump(hash_equals($foo, $reNegate));
?>

   
```php

El ejemplo anterior mostrará:

    bool(true)

## Véase también

sodium_crypto_core_ristretto255_scalar_random
