---
title: sodium_crypto_aead_aes256gcm_decrypt
description: Verifica y luego descifra un mensaje con AES-256-GCM
source_url: https://www.php.net/manual/es/function.sodium-crypto-aead-aes256gcm-decrypt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-aead-aes256gcm-decrypt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76070
---

sodium_crypto_aead_aes256gcm_decrypt

Verifica y luego descifra un mensaje con AES-256-GCM

## Descripción

```php
#[\SensitiveParameter] sodium_crypto_aead_aes256gcm_decrypt(string $ciphertext, string $additional_data, string $nonce, string $key): string
```php

Verifica y luego descifra con AES-256-GCM. Disponible únicamente si `sodium_crypto_aead_aes256gcm_is_available` devuelve `true`.

## Parámetros

`ciphertext`  
Debe estar en el formato proporcionado por `sodium_crypto_aead_aes256gcm_encrypt` (cifrar y etiquetar, concatenados).

`additional_data`  
Datos adicionales autenticados. Esto se utiliza en la verificación de la etiqueta de autenticación añadida al texto cifrado, pero no es cifrado ni almacenado en el texto cifrado.

`nonce`  
Un número que debe ser utilizado una sola vez, por mensaje. 12 bytes de largo.

`key`  
La clave de cifrado (256 bits).

## Valores devueltos

Devuelve el texto en claro en caso de éxito, o `false` si ocurre un error.
