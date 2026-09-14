---
title: sodium_crypto_aead_aegis128l_decrypt
description: Verifica y luego descifra un mensaje con AEGIS-128L
source_url: https://www.php.net/manual/es/function.sodium-crypto-aead-aegis128l-decrypt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-aead-aegis128l-decrypt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 01cb7d495
order: 76010
---

sodium_crypto_aead_aegis128l_decrypt

Verifica y luego descifra un mensaje con AEGIS-128L

## Descripción

```php
#[\SensitiveParameter] sodium_crypto_aead_aegis128l_decrypt(string $ciphertext, string $additional_data, string $nonce, string $key): string
```php

Verifica y luego descifra un mensaje con AEGIS-128L.

## Parámetros

`ciphertext`  
Debe estar en el formato proporcionado por `sodium_crypto_aead_aegis128l_encrypt`.

`additional_data`  
Además, datos autenticados. Esto se utiliza en la verificación de la etiqueta de autenticación añadida al texto cifrado, pero no se cifra ni se almacena en el texto cifrado.

`nonce`  
Un número que debe ser utilizado una sola vez, por mensaje.

`key`  
La clave de cifrado (128 bits).

## Valores devueltos

Devuelve el texto en claro en caso de éxito, o `false` si ocurre un error.

## Véase también

sodium_crypto_aead_aegis128l_encrypt

sodium_crypto_aead_aegis128l_keygen
