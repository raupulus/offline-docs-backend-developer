---
title: sodium_crypto_sign
description: Firma un mensaje
source_url: https://www.php.net/manual/es/function.sodium-crypto-sign.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-sign.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76920
---

sodium_crypto_sign

Firma un mensaje

## Descripción

```php
#[\SensitiveParameter] sodium_crypto_sign(string $message, string $secret_key): string
```php

Firma un mensaje con una clave secreta, que puede ser verificada por la clave pública correspondiente. Esta función adjunta la firma al mensaje. Ver `sodium_crypto_sign_detached` para las firmas desvinculadas.

## Parámetros

`message`  
El mensaje a firmar.

`secret_key`  
La clave secreta. Ver `sodium_crypto_sign_secretkey`

## Valores devueltos

El mensaje firmado (no cifrado).
