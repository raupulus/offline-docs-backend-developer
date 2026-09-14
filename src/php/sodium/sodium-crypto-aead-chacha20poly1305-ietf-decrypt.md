---
title: sodium_crypto_aead_chacha20poly1305_ietf_decrypt
description: Verifica que el texto cifrado incluye una etiqueta válida
source_url: https://www.php.net/manual/es/function.sodium-crypto-aead-chacha20poly1305-ietf-decrypt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-aead-chacha20poly1305-ietf-decrypt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76130
---

sodium_crypto_aead_chacha20poly1305_ietf_decrypt

Verifica que el texto cifrado incluye una etiqueta válida

## Descripción

```php
#[\SensitiveParameter] sodium_crypto_aead_chacha20poly1305_ietf_decrypt(string $ciphertext, string $additional_data, string $nonce, string $key): string
```php

Verifica y luego descifra con ChaCha20-Poly1305 (variante IETF).

La variante IETF utiliza nonces de 96 bits y contadores internos de 32 bits, en lugar de 64 bits para ambos.

## Parámetros

`ciphertext`  
Debe estar en el formato proporcionado por `sodium_crypto_aead_chacha20poly1305_ietf_encrypt` (texto cifrado y etiqueta, concatenados).

`additional_data`  
Datos adicionales autenticados. Esto se utiliza en la verificación de la etiqueta de autenticación añadida al texto cifrado, pero no se cifra ni se almacena en el texto cifrado.

`nonce`  
Un número que debe ser utilizado una sola vez, por mensaje. 12 bytes de largo.

`key`  
La clave de cifrado (256 bits).

## Valores devueltos

Devuelve el texto en claro en caso de éxito, o `false` si ocurre un error.
