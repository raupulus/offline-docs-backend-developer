---
title: sodium_crypto_box_seal
description: Cifrado anónimo con clave pública
source_url: https://www.php.net/manual/es/function.sodium-crypto-box-seal.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-box-seal.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76290
---

sodium_crypto_box_seal

Cifrado anónimo con clave pública

## Descripción

```php
#[\SensitiveParameter] sodium_crypto_box_seal(string $message, string $public_key): string
```php

Cifra un mensaje de tal manera que solo el destinatario pueda descifrarlo.

A diferencia de `sodium_crypto_box`, solo se necesita la clave pública del destinatario para utilizar `sodium_crypto_box_seal`. Una consecuencia de esta comodidad, sin embargo, es que el texto cifrado no está vinculado a una clave pública estática, y por lo tanto no está autenticado. De ahí el cifrado anónimo con clave pública.

`sodium_crypto_box_seal` siempre proporciona la integridad del texto cifrado. Solo que no la autenticación de la identidad del remitente.

Si también se necesita la autenticación del remitente, las funciones `sodium_crypto_sign` son probablemente el mejor punto de partida.

## Parámetros

`message`  
El mensaje a cifrar.

`public_key`  
La clave pública que corresponde a la única clave que puede descifrar el mensaje.

## Valores devueltos

Un texto cifrado en forma de (clave pública única, mensaje cifrado, etiqueta de autenticación).

## Ejemplos

Ejemplo de `sodium_crypto_box_seal`

```
<?php
$keypair = sodium_crypto_box_keypair();
$public_key = sodium_crypto_box_publickey($keypair);

// El texto en claro obfuscado para hacer el ejemplo más divertido
$plaintext_b64 = "V3JpdGluZyBzb2Z0d2FyZSBpbiBQSFAgY2FuIGJlIGEgZGVsaWdodCE=";
$decoded_plaintext = sodium_base642bin($plaintext_b64, SODIUM_BASE64_VARIANT_ORIGINAL);

$sealed = sodium_crypto_box_seal($decoded_plaintext, $public_key);
var_dump(base64_encode($sealed));

$opened = sodium_crypto_box_seal_open($sealed, $keypair);
var_dump($opened);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(120) "oRBXXAV4iQBrxlV4A21Bord8Yo/D8ZlrIIGNyaRCcGBfpz0map52I3xq6l+CST+1NSgQkbV+HiYyFjXWiWiaCGupGf+zl4bgWj/A9Adtem7Jt3h3emrMsLw="
    string(41) "Writing software in PHP can be a delight!"
