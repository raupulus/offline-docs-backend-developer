---
title: sodium_crypto_box_keypair
description: Genera aleatoriamente una clave secreta y una clave pública correspondiente
source_url: https://www.php.net/manual/es/function.sodium-crypto-box-keypair.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-box-keypair.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76240
---

sodium_crypto_box_keypair

Genera aleatoriamente una clave secreta y una clave pública correspondiente

## Descripción

```php
sodium_crypto_box_keypair(): string
```php

Genera una clave secreta y una clave pública en una sola cadena.

Para extraer la clave secreta de esta cadena de clave unificada, ver `sodium_crypto_box_secretkey`. Para extraer la clave pública de esta cadena de clave unificada, ver `sodium_crypto_box_publickey`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Una cadena que contiene tanto la clave secreta X25519 como la clave pública X25519 correspondiente.
