---
title: sodium_crypto_stream_xchacha20
description: Desarrolla la clave y el nonce en un flujo de claves de bytes pseudoaleatorios
source_url: https://www.php.net/manual/es/function.sodium-crypto-stream-xchacha20.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-stream-xchacha20.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76970
---

sodium_crypto_stream_xchacha20

Desarrolla la clave y el nonce en un flujo de claves de bytes pseudoaleatorios

## Descripción

```php
#[\SensitiveParameter] sodium_crypto_stream_xchacha20(int $length, string $nonce, string $key): string
```php

Desarrolla la `clave` y el `nonce` en un flujo de claves de bytes pseudoaleatorios.

## Parámetros

`length`  
El número de bytes deseado.

`nonce`  
Un nonce de 24 bytes.

`key`  
Clave, posiblemente generada por la función `sodium_crypto_stream_xchacha20_keygen`.

## Valores devueltos

Devuelve un flujo pseudoaleatorio que puede ser utilizado con `sodium_crypto_stream_xchacha20_xor`.
