---
title: sodium_crypto_sign_verify_detached
description: Verifica la firma de un mensaje
source_url: https://www.php.net/manual/es/function.sodium-crypto-sign-verify-detached.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-sign-verify-detached.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76910
---

sodium_crypto_sign_verify_detached

Verifica la firma de un mensaje

## Descripción

```php
sodium_crypto_sign_verify_detached(string $signature, string $message, string $public_key): bool
```php

Verifica la firma de un mensaje

## Parámetros

`signature`  
La firma criptográfica obtenida a partir de `sodium_crypto_sign_detached`

`message`  
El mensaje a verificar

`public_key`  
La clave pública Ed25519

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
