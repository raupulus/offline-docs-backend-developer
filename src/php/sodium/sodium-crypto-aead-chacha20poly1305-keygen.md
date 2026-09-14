---
title: sodium_crypto_aead_chacha20poly1305_keygen
description: Genera una clave ChaCha20-Poly1305 aleatoria
source_url: https://www.php.net/manual/es/function.sodium-crypto-aead-chacha20poly1305-keygen.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-aead-chacha20poly1305-keygen.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76160
---

sodium_crypto_aead_chacha20poly1305_keygen

Genera una clave ChaCha20-Poly1305 aleatoria

## Descripción

```php
sodium_crypto_aead_chacha20poly1305_keygen(): string
```php

Genera una clave aleatoria para su uso con `sodium_crypto_aead_chacha20poly1305_encrypt` y `sodium_crypto_aead_chacha20poly1305_decrypt`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una clave aleatoria de 256 bits.
