---
title: sodium_crypto_stream_xchacha20_xor
description: Cifra un dato utilizando un nonce y una clave secreta (sin autenticación)
source_url: https://www.php.net/manual/es/function.sodium-crypto-stream-xchacha20-xor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-stream-xchacha20-xor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76960
---

sodium_crypto_stream_xchacha20_xor

Cifra un dato utilizando un nonce y una clave secreta (sin autenticación)

## Descripción

```php
#[\SensitiveParameter] #[\SensitiveParameter] sodium_crypto_stream_xchacha20_xor(string $message, string $nonce, string $key): string
```php

Cifra un `message` utilizando un `nonce` y una clave secreta `key` (sin autenticación).

> [!CAUTION]
> Este cifrado no es autenticado y no previene ataques de texto cifrado elegido. Asegúrese de combinar el texto cifrado con un código de autenticación de mensaje, por ejemplo con la función `sodium_crypto_aead_xchacha20poly1305_ietf_encrypt`, o `sodium_crypto_auth`.

## Parámetros

`message`  
El mensaje a cifrar.

`nonce`  
Un nonce de 24 bytes.

`key`  
Clave, posiblemente generada por la función `sodium_crypto_stream_xchacha20_keygen`.

## Valores devueltos

El texto cifrado.

## Véase también

sodium_crypto_stream_xchacha20_xor_ic
