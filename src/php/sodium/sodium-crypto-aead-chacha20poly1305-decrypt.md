---
title: sodium_crypto_aead_chacha20poly1305_decrypt
description: Verifica y luego descifra con ChaCha20-Poly1305
source_url: https://www.php.net/manual/es/function.sodium-crypto-aead-chacha20poly1305-decrypt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-aead-chacha20poly1305-decrypt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76110
---

sodium_crypto_aead_chacha20poly1305_decrypt

Verifica y luego descifra con ChaCha20-Poly1305

## Descripción

```php
#[\SensitiveParameter] sodium_crypto_aead_chacha20poly1305_decrypt(string $ciphertext, string $additional_data, string $nonce, string $key): string
```php

Verifica y luego descifra con ChaCha20-Poly1305.

## Parámetros

`ciphertext`  
Debe estar en el formato proporcionado por `sodium_crypto_aead_chacha20poly1305_encrypt` (cifrar y etiquetar, concatenados).

`additional_data`  
Datos adicionales autenticados. Esto se utiliza en la verificación de la etiqueta de autenticación añadida al texto cifrado, pero no se cifra ni se almacena en el texto cifrado.

`nonce`  
Un número que debe ser utilizado una sola vez, por mensaje. 8 bytes de longitud.

`key`  
La clave de cifrado. 256 bits.

## Valores devueltos

Devuelve el texto en claro en caso de éxito, o `false` si ocurre un error.
