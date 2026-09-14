---
title: sodium_crypto_aead_aes256gcm_encrypt
description: Cifra y autentica con AES-256-GCM
source_url: https://www.php.net/manual/es/function.sodium-crypto-aead-aes256gcm-encrypt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-aead-aes256gcm-encrypt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76080
---

sodium_crypto_aead_aes256gcm_encrypt

Cifra y autentica con AES-256-GCM

## Descripción

```php
#[\SensitiveParameter] #[\SensitiveParameter] sodium_crypto_aead_aes256gcm_encrypt(string $message, string $additional_data, string $nonce, string $key): string
```php

Cifra y autentica con AES-256-GCM. Disponible únicamente si `sodium_crypto_aead_aes256gcm_is_available` devuelve `true`.

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

Devuelve el texto cifrado y la etiqueta de autenticación en forma de cadena de bytes binarios sin tratar. (Formato: texto cifrado, luego etiqueta.)
