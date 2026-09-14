---
title: sodium_crypto_sign_ed25519_sk_to_curve25519
description: Convierte una clave secreta Ed25519 en una clave secreta Curve25519
source_url: https://www.php.net/manual/es/function.sodium-crypto-sign-ed25519-sk-to-curve25519.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-sign-ed25519-sk-to-curve25519.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76830
---

sodium_crypto_sign_ed25519_sk_to_curve25519

Convierte una clave secreta Ed25519 en una clave secreta Curve25519

## Descripción

```php
#[\SensitiveParameter] sodium_crypto_sign_ed25519_sk_to_curve25519(string $secret_key): string
```php

Dada una clave secreta Ed25519, se calcula la clave secreta X25519 birationnelmente equivalente.

## Parámetros

`secret_key`  
La clave secreta apropiada para las funciones crypto_sign.

## Valores devueltos

La clave secreta apropiada para las funciones crypto_box.
