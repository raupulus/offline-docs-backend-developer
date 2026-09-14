---
title: sodium_crypto_sign_secretkey
description: Extrae la clave secreta Ed25519 de un par de claves
source_url: https://www.php.net/manual/es/function.sodium-crypto-sign-secretkey.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-sign-secretkey.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76890
---

sodium_crypto_sign_secretkey

Extrae la clave secreta Ed25519 de un par de claves

## Descripción

```php
#[\SensitiveParameter] sodium_crypto_sign_secretkey(string $key_pair): string
```php

Extrae la clave secreta Ed25519 de un par de claves

## Parámetros

`key_pair`  
El par de claves Ed25519 (ver: `sodium_crypto_sign_keypair`)

## Valores devueltos

La clave secreta Ed25519
