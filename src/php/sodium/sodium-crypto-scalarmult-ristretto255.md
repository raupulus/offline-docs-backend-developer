---
title: sodium_crypto_scalarmult_ristretto255
description: Calcula un secreto compartido
source_url: https://www.php.net/manual/es/function.sodium-crypto-scalarmult-ristretto255.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-scalarmult-ristretto255.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76680
---

sodium_crypto_scalarmult_ristretto255

Calcula un secreto compartido

## Descripción

```php
sodium_crypto_scalarmult_ristretto255(string $n, string $p): string
```php

Calcula el escalar `n` veces el punto `p`. Disponible a partir de libsodium 1.0.18.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`n`  
Un escalar, que típicamente es una clave secreta.

`p`  
Un punto (coordenada x), que típicamente es una clave pública.

## Valores devueltos

Devuelve una `string` aleatoria de 32 bytes.

## Véase también

sodium_crypto_scalarmult_ristretto255_base
