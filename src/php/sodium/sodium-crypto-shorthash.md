---
title: sodium_crypto_shorthash
description: Calcula un hash corto de un mensaje y una clave
source_url: https://www.php.net/manual/es/function.sodium-crypto-shorthash.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-shorthash.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76800
---

sodium_crypto_shorthash

Calcula un hash corto de un mensaje y una clave

## Descripción

```php
#[\SensitiveParameter] sodium_crypto_shorthash(string $message, string $key): string
```php

`sodium_crypto_shorthash` envuelve una función hash llamada SipHash-2-4, que es ideal para implementar tablas hash que no son susceptibles a ataques de denegación de servicio por colisión de hash (Hash-DoS).

SipHash-2-4 no es una función hash criptográfica general.

## Parámetros

`message`  
El mensaje a hachear.

`key`  
La clave de hash.

## Valores devueltos
