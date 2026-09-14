---
title: sodium_crypto_sign_open
description: Verifica que el mensaje firmado posee una firma válida
source_url: https://www.php.net/manual/es/function.sodium-crypto-sign-open.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-sign-open.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76860
---

sodium_crypto_sign_open

Verifica que el mensaje firmado posee una firma válida

## Descripción

```php
sodium_crypto_sign_open(string $signed_message, string $public_key): string
```php

Verifica la firma adjunta a un mensaje y devuelve el mensaje

## Parámetros

`signed_message`  
Un mensaje firmado con `sodium_crypto_sign`

`public_key`  
Una clave pública Ed25519

## Valores devueltos

Devuelve el mensaje firmado original en caso de éxito, o `false` si ocurre un error.
