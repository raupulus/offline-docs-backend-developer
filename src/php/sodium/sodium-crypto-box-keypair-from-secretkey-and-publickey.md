---
title: sodium_crypto_box_keypair_from_secretkey_and_publickey
description: Crear una pareja de claves unificada a partir de una clave secreta y
  una clave pública
source_url: https://www.php.net/manual/es/function.sodium-crypto-box-keypair-from-secretkey-and-publickey.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-box-keypair-from-secretkey-and-publickey.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76230
---

sodium_crypto_box_keypair_from_secretkey_and_publickey

Crear una pareja de claves unificada a partir de una clave secreta y una clave pública

## Descripción

```php
#[\SensitiveParameter] sodium_crypto_box_keypair_from_secretkey_and_publickey(string $secret_key, string $public_key): string
```php

Esta función existe para satisfacer los requisitos de la API de `crypto_box`. Pasar la clave secreta de una parte y la clave pública de la otra, y se obtendrá una "pareja de claves" para la conversación.

## Parámetros

`secret_key`  
La clave secreta.

`public_key`  
La clave pública.

## Valores devueltos

Una pareja de claves X25519.
