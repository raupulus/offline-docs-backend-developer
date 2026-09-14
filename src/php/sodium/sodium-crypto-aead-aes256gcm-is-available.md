---
title: sodium_crypto_aead_aes256gcm_is_available
description: Verifica si el hardware soporta AES256-GCM
source_url: https://www.php.net/manual/es/function.sodium-crypto-aead-aes256gcm-is-available.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-aead-aes256gcm-is-available.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76090
---

sodium_crypto_aead_aes256gcm_is_available

Verifica si el hardware soporta AES256-GCM

## Descripción

```php
sodium_crypto_aead_aes256gcm_is_available(): bool
```php

El valor de retorno de esta función depende de si el hardware soporta o no el AES acelerado por hardware.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si es seguro cifrar con AES-256-GCM, y `false` en caso contrario.
