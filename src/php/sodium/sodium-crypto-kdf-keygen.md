---
title: sodium_crypto_kdf_keygen
description: Genera una clave raíz aleatoria para la interfaz KDF
source_url: https://www.php.net/manual/es/function.sodium-crypto-kdf-keygen.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-kdf-keygen.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76520
---

sodium_crypto_kdf_keygen

Genera una clave raíz aleatoria para la interfaz KDF

## Descripción

```php
sodium_crypto_kdf_keygen(): string
```php

Genera una clave aleatoria adecuada para servir como clave raíz para `sodium_crypto_kdf_derive_from_key`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Una clave aleatoria de 256 bits.
