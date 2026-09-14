---
title: sodium_crypto_secretbox_open
description: Desencriptación autenticada con una clave compartida
source_url: https://www.php.net/manual/es/function.sodium-crypto-secretbox-open.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-secretbox-open.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76710
---

sodium_crypto_secretbox_open

Desencriptación autenticada con una clave compartida

## Descripción

```php
#[\SensitiveParameter] sodium_crypto_secretbox_open(string $ciphertext, string $nonce, string $key): string
```php

Desencriptación de un mensaje cifrado con una clave simétrica (compartida).

## Parámetros

`ciphertext`  
Debe estar en el formato proporcionado por `sodium_crypto_secretbox` (concatenación del texto cifrado y del tag).

`nonce`  
Un número que debe ser utilizado una sola vez, por mensaje. 24 bytes de longitud. Este es un límite suficientemente grande para ser generado aleatoriamente (i.e. `random_bytes`).

`key`  
La clave de cifrado (256 bits).

## Valores devueltos

La cadena desencriptada en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

- Si `nonce` tiene una longitud de bytes diferente de [`SODIUM_CRYPTO_SECRETBOX_NONCEBYTES`](#constant.sodium-crypto-secretbox-noncebytes) (24 bytes), se lanzará una `SodiumException`.

- Si `key` tiene una longitud de bytes diferente de [`SODIUM_CRYPTO_SECRETBOX_KEYBYTES`](#constant.sodium-crypto-secretbox-keybytes) (32 bytes), se lanzará una `SodiumException`.

## Ejemplos

Ejemplo de `sodium_crypto_secretbox_open`

```
<?php
// La $key debe ser mantenida confidencial
$key = random_bytes(SODIUM_CRYPTO_SECRETBOX_KEYBYTES);
// No reutilizar $nonce con la misma clave
$nonce = random_bytes(SODIUM_CRYPTO_SECRETBOX_NONCEBYTES);
$ciphertext = sodium_crypto_secretbox('mensaje a ser cifrado', $nonce, $key);

// El mismo nonce y la misma clave son necesarios para desencriptar el $ciphertext
$plaintext = sodium_crypto_secretbox_open($ciphertext, $nonce, $key);
if ($plaintext !== false) {
    echo $plaintext . PHP_EOL;
}
?>

   
```php

El ejemplo anterior mostrará:

    mensaje a ser cifrado

## Véase también

sodium_crypto_secretbox

sodium_crypto_secretbox_keygen

random_bytes
