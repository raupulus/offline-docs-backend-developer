---
title: sodium_crypto_aead_xchacha20poly1305_ietf_decrypt
description: (Preferido) Verificar y luego descifrar con XChaCha20-Poly1305
source_url: https://www.php.net/manual/es/function.sodium-crypto-aead-xchacha20poly1305-ietf-decrypt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-aead-xchacha20poly1305-ietf-decrypt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76170
---

sodium_crypto_aead_xchacha20poly1305_ietf_decrypt

(Preferido) Verificar y luego descifrar con XChaCha20-Poly1305

## Descripción

```php
#[\SensitiveParameter] sodium_crypto_aead_xchacha20poly1305_ietf_decrypt(string $ciphertext, string $additional_data, string $nonce, string $key): string
```php

Verificar y luego descifrar con ChaCha20-Poly1305 (variante de nonce extendido).

Generalmente, XChaCha20-Poly1305 es el mejor de los modos AEAD proporcionados para usar.

## Parámetros

`ciphertext`  
Debe estar en el formato proporcionado por `sodium_crypto_aead_xchacha20poly1305_ietf_encrypt` (texto cifrado y etiqueta, concatenados).

`additional_data`  
Datos adicionales autenticados. Esto se usa en la verificación de la etiqueta de autenticación adjunta al texto cifrado, pero no se cifra ni se almacena en el texto cifrado.

`nonce`  
Un número que debe usarse solo una vez, por mensaje. 24 bytes de largo. Este es un límite lo suficientemente grande para generar aleatoriamente (es decir, `random_bytes`).

`key`  
Clave de cifrado (256 bits).

## Valores devueltos

Devuelve el texto plano en caso de éxito, o `false` si ocurre un error.
