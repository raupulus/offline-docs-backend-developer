---
title: sodium_crypto_sign_keypair_from_secretkey_and_publickey
description: Reúne una clave secreta y una clave pública
source_url: https://www.php.net/manual/es/function.sodium-crypto-sign-keypair-from-secretkey-and-publickey.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-sign-keypair-from-secretkey-and-publickey.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76840
---

sodium_crypto_sign_keypair_from_secretkey_and_publickey

Reúne una clave secreta y una clave pública

## Descripción

```php
#[\SensitiveParameter] sodium_crypto_sign_keypair_from_secretkey_and_publickey(string $secret_key, string $public_key): string
```php

Reúne una clave secreta y una clave pública.

## Parámetros

`secret_key`  
La clave secreta Ed25519

`public_key`  
La clave pública

## Valores devueltos

Un par de claves
