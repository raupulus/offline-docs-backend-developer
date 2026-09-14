---
title: sodium_crypto_box_seal_open
description: Desencriptación anónima con clave pública
source_url: https://www.php.net/manual/es/function.sodium-crypto-box-seal-open.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-box-seal-open.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76280
---

sodium_crypto_box_seal_open

Desencriptación anónima con clave pública

## Descripción

```php
#[\SensitiveParameter] sodium_crypto_box_seal_open(string $ciphertext, string $key_pair): string
```php

Desencripta un mensaje que ha sido encriptado con `sodium_crypto_box_seal`

## Parámetros

`ciphertext`  
El mensaje encriptado

`key_pair`  
La pareja de claves del destinatario. Debe incluir la clave secreta.

## Valores devueltos

El texto en claro en caso de éxito, o `false` si ocurre un error.

## Ejemplos

Ejemplo de `sodium_crypto_box_seal_open`

```
<?php
// El texto encriptado no es sensible; base64_decode es suficiente
$sealed_b64 = "oRBXXAV4iQBrxlV4A21Bord8Yo/D8ZlrIIGNyaRCcGBfpz0map52I3xq6l+CST+1NSgQkbV+HiYyFjXWiWiaCGupGf+zl4bgWj/A9Adtem7Jt3h3emrMsLw=";
$sealed = base64_decode($sealed_b64);

// La pareja de claves contiene un secreto criptográfico; utilice un decodificador seguro en tiempo
$keypair_b64 = "KZkF8wnB7bnC2aXB3lFOqCTc0Z6MllvaQb9ASVG8o2/MsewkuE4u1uaEgTzSakeiYyIW8DGj+02/L3cWIbs9bQ==";
$keypair = sodium_base642bin($keypair_b64, SODIUM_BASE64_VARIANT_ORIGINAL);

$opened = sodium_crypto_box_seal_open($sealed, $keypair);
var_dump($opened);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(41) "Writing software in PHP can be a delight!"
