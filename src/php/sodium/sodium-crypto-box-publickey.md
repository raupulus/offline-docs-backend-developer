---
title: sodium_crypto_box_publickey
description: Extrae la clave pública de un par de claves crypto_box
source_url: https://www.php.net/manual/es/function.sodium-crypto-box-publickey.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-box-publickey.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76270
---

sodium_crypto_box_publickey

Extrae la clave pública de un par de claves crypto_box

## Descripción

```php
#[\SensitiveParameter] sodium_crypto_box_publickey(string $key_pair): string
```php

Dado un par de claves, se extrae únicamente la clave pública.

## Parámetros

`key_pair`  
Un par de claves, tal como el generado por `sodium_crypto_box_keypair` o `sodium_crypto_box_seed_keypair`

## Valores devueltos

La clave pública X25519.
