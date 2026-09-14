---
title: sodium_crypto_stream_xor
description: Cifra un mensaje sin autenticación
source_url: https://www.php.net/manual/es/function.sodium-crypto-stream-xor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-stream-xor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76980
---

sodium_crypto_stream_xor

Cifra un mensaje sin autenticación

## Descripción

```php
#[\SensitiveParameter] #[\SensitiveParameter] sodium_crypto_stream_xor(string $message, string $nonce, string $key): string
```php

Esta función cifra un mensaje con XSalsa20, pero no proporciona ninguna garantía sobre el texto cifrado.

## Parámetros

`message`  
El mensaje a cifrar.

`nonce`  
Un número que debe ser utilizado una sola vez, por mensaje. 24 bytes de largo. Es un límite suficientemente grande para ser generado aleatoriamente (i.e. `random_bytes`).

`key`  
La clave de cifrado (256 bits).

## Valores devueltos

El mensaje cifrado.
