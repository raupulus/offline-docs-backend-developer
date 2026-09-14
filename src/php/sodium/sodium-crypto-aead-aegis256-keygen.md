---
title: sodium_crypto_aead_aegis256_keygen
description: Genera una clave AEGIS-256 aleatoria
source_url: https://www.php.net/manual/es/function.sodium-crypto-aead-aegis256-keygen.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-aead-aegis256-keygen.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 01cb7d495
order: 76060
---

sodium_crypto_aead_aegis256_keygen

Genera una clave AEGIS-256 aleatoria

## Descripción

```php
sodium_crypto_aead_aegis256_keygen(): string
```php

Genera una clave aleatoria de 256 bits para ser utilizada con `sodium_crypto_aead_aegis256_encrypt` y `sodium_crypto_aead_aegis256_decrypt`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una clave aleatoria de 256 bits.

## Véase también

sodium_crypto_aead_aegis256_decrypt

sodium_crypto_aead_aegis256_encrypt
