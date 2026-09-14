---
title: sodium_crypto_box_open
description: Desencriptación autenticada con clave pública
source_url: https://www.php.net/manual/es/function.sodium-crypto-box-open.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-box-open.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76250
---

sodium_crypto_box_open

Desencriptación autenticada con clave pública

## Descripción

```php
#[\SensitiveParameter] sodium_crypto_box_open(string $ciphertext, string $nonce, string $key_pair): string
```php

Desencripta un mensaje utilizando criptografía asimétrica (clave pública).

## Parámetros

`ciphertext`  
El mensaje cifrado a desencriptar.

`nonce`  
Un número que debe ser utilizado una sola vez, por mensaje. 24 bytes de longitud. Es un límite suficientemente grande para ser generado aleatoriamente (i.e. `random_bytes`).

`key_pair`  
Ver `sodium_crypto_box_keypair_from_secretkey_and_publickey`. Debe incluir la clave pública del remitente y la clave secreta del destinatario.

## Valores devueltos

Devuelve el mensaje en claro en caso de éxito, o `false` si ocurre un error.
