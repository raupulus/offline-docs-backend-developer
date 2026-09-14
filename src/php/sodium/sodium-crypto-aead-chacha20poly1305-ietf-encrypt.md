---
title: sodium_crypto_aead_chacha20poly1305_ietf_encrypt
description: Cifra un mensaje
source_url: https://www.php.net/manual/es/function.sodium-crypto-aead-chacha20poly1305-ietf-encrypt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-aead-chacha20poly1305-ietf-encrypt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: cc7976fa4
order: 76140
---

sodium_crypto_aead_chacha20poly1305_ietf_encrypt

Cifra un mensaje

## Descripción

```php
#[\SensitiveParameter] #[\SensitiveParameter] sodium_crypto_aead_chacha20poly1305_ietf_encrypt(string $message, string $additional_data, string $nonce, string $key): string
```php

Cifra y autentica con ChaCha20-Poly1305 (variante IETF).

La variante IETF utiliza nonces de 96 bits y contadores internos de 32 bits, en lugar de 64 bits para ambos.

## Parámetros

`message`  
El mensaje en texto claro a cifrar.

`additional_data`  
Datos adicionales autenticados. Esto se utiliza en la verificación de la etiqueta de autenticación añadida al texto cifrado, pero no se cifra ni se almacena en el texto cifrado.

`nonce`  
Un número que debe ser utilizado una sola vez, por mensaje. 12 bytes de largo.

`key`  
La clave de cifrado (256 bits).

## Valores devueltos

Devuelve el texto cifrado y la etiqueta de autenticación como una cadena de bytes binarios sin procesar.
