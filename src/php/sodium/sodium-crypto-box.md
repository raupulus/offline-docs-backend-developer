---
title: sodium_crypto_box
description: Cifrado asimétrico autenticado
source_url: https://www.php.net/manual/es/function.sodium-crypto-box.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-box.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76320
---

sodium_crypto_box

Cifrado asimétrico autenticado

## Descripción

```php
#[\SensitiveParameter] #[\SensitiveParameter] sodium_crypto_box(string $message, string $nonce, string $key_pair): string
```php

Cifra un mensaje utilizando criptografía asimétrica (clave pública).

El algoritmo utilizado por las funciones prefijadas por `sodium_crypto_box` es Diffie-Hellman sobre la curva de Montgomery, Curve25519; generalmente abreviado como X25519.

## Parámetros

`message`  
El mensaje a cifrar.

`nonce`  
Un número que debe ser utilizado una sola vez, por mensaje. 24 bytes de largo. Este es un límite suficientemente grande para ser generado aleatoriamente (i.e. `random_bytes`).

`key_pair`  
Ver `sodium_crypto_box_keypair_from_secretkey_and_publickey`. Esto incluye la clave pública del remitente y la clave secreta del destinatario.

## Valores devueltos

Devuelve el mensaje cifrado (ciphertext más etiqueta de autenticación). El texto cifrado será 16 bytes más largo que el texto en claro, y una string binaria bruta. Ver `sodium_bin2base64` para un encodaje seguro para el almacenamiento.
