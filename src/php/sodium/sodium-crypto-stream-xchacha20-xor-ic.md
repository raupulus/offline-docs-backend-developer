---
title: sodium_crypto_stream_xchacha20_xor_ic
description: Cifra un mensaje utilizando un nonce y una clave secreta (sin autenticación)
source_url: https://www.php.net/manual/es/function.sodium-crypto-stream-xchacha20-xor-ic.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-stream-xchacha20-xor-ic.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: cc7976fa4
order: 76950
---

sodium_crypto_stream_xchacha20_xor_ic

Cifra un mensaje utilizando un nonce y una clave secreta (sin autenticación)

## Descripción

```php
#[\SensitiveParameter] #[\SensitiveParameter] sodium_crypto_stream_xchacha20_xor_ic(string $message, string $nonce, int $counter, string $key): string
```php

Esta función es similar a `sodium_crypto_stream_xchacha20_xor` pero añade la posibilidad de establecer el valor inicial del contador de bloques a un valor distinto de cero. Esto permite acceder directamente a cualquier bloque sin tener que calcular los anteriores.

> [!CAUTION]
> Este cifrado no está autenticado y no previene los ataques de texto cifrado elegido. Asegúrese de combinar el texto cifrado con un código de autenticación de mensaje, por ejemplo, con la función `sodium_crypto_aead_xchacha20poly1305_ietf_encrypt`, o `sodium_crypto_auth`.

## Parámetros

`message`  
El mensaje a cifrar.

`nonce`  
Un nonce de 24 bytes.

`counter`  
El valor inicial del contador de bloques.

`key`  
Clave, posiblemente generada por la función `sodium_crypto_stream_xchacha20_keygen`.

## Valores devueltos

El texto cifrado.

## Ejemplos

Ejemplo de `sodium_crypto_stream_xchacha20_xor_ic`

```
<?php
$n2 = random_bytes(SODIUM_CRYPTO_STREAM_XCHACHA20_NONCEBYTES);
$left  = str_repeat("\x01", 64);
$right = str_repeat("\xfe", 64);

// Todo en una vez:
$stream7_unified = sodium_crypto_stream_xchacha20_xor($left . $right, $n2, $key);

// Por partes, con un contador inicial:
$stream7_left  = sodium_crypto_stream_xchacha20_xor_ic($left, $n2, 0, $key);
$stream7_right = sodium_crypto_stream_xchacha20_xor_ic($right, $n2, 1, $key);
$stream7_concat = $stream7_left . $stream7_right;

var_dump(strlen($stream7_concat));
var_dump($stream7_unified === $stream7_concat);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(128)
    bool(true)

## Véase también

sodium_crypto_stream_xchacha20_xor
