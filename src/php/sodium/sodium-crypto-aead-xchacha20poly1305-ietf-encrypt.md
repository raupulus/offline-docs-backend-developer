---
title: sodium_crypto_aead_xchacha20poly1305_ietf_encrypt
description: (Preferido) Cifra y luego autentica con XChaCha20-Poly1305
source_url: https://www.php.net/manual/es/function.sodium-crypto-aead-xchacha20poly1305-ietf-encrypt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-aead-xchacha20poly1305-ietf-encrypt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: cc7976fa4
order: 76180
---

sodium_crypto_aead_xchacha20poly1305_ietf_encrypt

(Preferido) Cifra y luego autentica con XChaCha20-Poly1305

## Descripción

```php
#[\SensitiveParameter] #[\SensitiveParameter] sodium_crypto_aead_xchacha20poly1305_ietf_encrypt(string $message, string $additional_data, string $nonce, string $key): string
```php

Cifra y luego autentica con XChaCha20-Poly1305 (variante eXtended-nonce).

Generalmente, XChaCha20-Poly1305 es el mejor de los modos AEAD proporcionados para usar.

## Parámetros

`message`  
El mensaje en texto claro a cifrar.

`additional_data`  
Datos adicionales autenticados. Esto se utiliza en la verificación de la etiqueta de autenticación añadida al texto cifrado, pero no se cifra ni se almacena en el texto cifrado.

`nonce`  
Un número que debe ser utilizado una sola vez, por mensaje. 24 bytes de largo. Este es un límite suficientemente grande para ser generado aleatoriamente (i.e. `random_bytes`).

`key`  
La clave de cifrado (256 bits).

## Valores devueltos

Devuelve el texto cifrado y la etiqueta de autenticación como una cadena de bytes binarios sin procesar.
