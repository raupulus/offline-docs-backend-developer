---
title: sodium_crypto_core_ristretto255_scalar_mul
description: Multiplica un valor escalar
source_url: https://www.php.net/manual/es/function.sodium-crypto-core-ristretto255-scalar-mul.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-core-ristretto255-scalar-mul.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76400
---

sodium_crypto_core_ristretto255_scalar_mul

Multiplica un valor escalar

## Descripción

```php
sodium_crypto_core_ristretto255_scalar_mul(string $x, string $y): string
```php

Multiplica un valor escalar. Disponible a partir de libsodium 1.0.18.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`x`  
Escalar que representa la coordenada X.

`y`  
Escalar que representa la coordenada Y.

## Valores devueltos

Devuelve una `string` aleatoria de 32 bytes.

## Véase también

sodium_crypto_core_ristretto255_scalar_random
