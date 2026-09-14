---
title: sodium_crypto_aead_aegis256_encrypt
description: Cifra y autentica un mensaje con AEGIS-256
source_url: https://www.php.net/manual/es/function.sodium-crypto-aead-aegis256-encrypt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-aead-aegis256-encrypt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 01cb7d495
order: 76050
---

sodium_crypto_aead_aegis256_encrypt

Cifra y autentica un mensaje con AEGIS-256

## Descripción

```php
#[\SensitiveParameter] #[\SensitiveParameter] sodium_crypto_aead_aegis256_encrypt(string $message, string $additional_data, string $nonce, string $key): string
```php

Cifra y autentica un mensaje con AEGIS-256.

## Parámetros

`message`  
El mensaje en claro a cifrar.

`additional_data`  
Datos adicionales autenticados. Esto se utiliza en la verificación de la etiqueta de autenticación añadida al texto cifrado, pero no se cifra ni se almacena en el texto cifrado.

`nonce`  
Un número que debe ser utilizado una sola vez, por mensaje.

`key`  
La clave de cifrado (256 bits).

## Valores devueltos

Devuelve el texto cifrado y la etiqueta de autenticación en forma de cadena de octetos sin tratar.

## Véase también

sodium_crypto_aead_aegis256_decrypt

sodium_crypto_aead_aegis256_keygen
