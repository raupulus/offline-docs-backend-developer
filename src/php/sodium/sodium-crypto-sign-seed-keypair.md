---
title: sodium_crypto_sign_seed_keypair
description: Deriva de manera determinista el par de claves a partir de una sola clave
source_url: https://www.php.net/manual/es/function.sodium-crypto-sign-seed-keypair.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-sign-seed-keypair.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76900
---

sodium_crypto_sign_seed_keypair

Deriva de manera determinista el par de claves a partir de una sola clave

## Descripción

```php
#[\SensitiveParameter] sodium_crypto_sign_seed_keypair(string $seed): string
```php

Adjunta la semilla para formar una clave secreta, deriva la clave pública y devuelve ambas como un par de claves.

Las funciones `*_seed_keypair` son ideales para generar un par de claves a partir de una contraseña y una sal. Utilice el resultado como `seed` para generar las claves deseadas.

## Parámetros

`seed`  
Algunos datos criptográficos. Debe ser de 32 bytes.

## Valores devueltos

Un par de claves (clave secreta y clave pública)
