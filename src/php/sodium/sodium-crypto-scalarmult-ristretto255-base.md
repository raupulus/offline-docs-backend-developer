---
title: sodium_crypto_scalarmult_ristretto255_base
description: Calcula la clave pública a partir de una clave secreta
source_url: https://www.php.net/manual/es/function.sodium-crypto-scalarmult-ristretto255-base.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-scalarmult-ristretto255-base.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76670
---

sodium_crypto_scalarmult_ristretto255_base

Calcula la clave pública a partir de una clave secreta

## Descripción

```php
sodium_crypto_scalarmult_ristretto255_base(string $n): string
```php

Dada una clave secreta, calcula la clave pública correspondiente. Disponible a partir de libsodium 1.0.18.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`n`  
Una clave secreta.

## Valores devueltos

Devuelve una `string` aleatoria de 32 bytes.

## Véase también

sodium_crypto_scalarmult_ristretto255
