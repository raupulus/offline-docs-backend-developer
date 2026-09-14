---
title: sodium_crypto_aead_aes256gcm_keygen
description: Genera una clave AES-256-GCM aleatoria
source_url: https://www.php.net/manual/es/function.sodium-crypto-aead-aes256gcm-keygen.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-aead-aes256gcm-keygen.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76100
---

sodium_crypto_aead_aes256gcm_keygen

Genera una clave AES-256-GCM aleatoria

## Descripción

```php
sodium_crypto_aead_aes256gcm_keygen(): string
```php

Genera una clave aleatoria para su uso con `sodium_crypto_aead_aes256gcm_encrypt` y `sodium_crypto_aead_aes256gcm_decrypt`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una clave aleatoria de 256 bits.
