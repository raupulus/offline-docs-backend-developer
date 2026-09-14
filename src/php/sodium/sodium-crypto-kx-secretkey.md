---
title: sodium_crypto_kx_secretkey
description: Extrae la clave secreta de un par de claves crypto_kx
source_url: https://www.php.net/manual/es/function.sodium-crypto-kx-secretkey.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-kx-secretkey.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76560
---

sodium_crypto_kx_secretkey

Extrae la clave secreta de un par de claves crypto_kx

## Descripción

```php
#[\SensitiveParameter] sodium_crypto_kx_secretkey(string $key_pair): string
```php

Extrae la clave secreta de un par de claves crypto_kx.

## Parámetros

`key_pair`  
Un par de claves X25519, tal como el generado por `sodium_crypto_kx_keypair`.

## Valores devueltos

La clave secreta X25519.
