---
title: sodium_crypto_secretbox
description: Cifrado autenticado con una clave compartida
source_url: https://www.php.net/manual/es/function.sodium-crypto-secretbox.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-secretbox.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76720
---

sodium_crypto_secretbox

Cifrado autenticado con una clave compartida

## Descripción

```php
#[\SensitiveParameter] #[\SensitiveParameter] sodium_crypto_secretbox(string $message, string $nonce, string $key): string
```php

Cifra un mensaje con una clave simétrica (compartida).

## Parámetros

`message`  
El mensaje en claro a cifrar.

`nonce`  
Un número que debe ser utilizado una sola vez, por mensaje. 24 bytes de largo. Este es un límite suficientemente grande para ser generado aleatoriamente (i.e. `random_bytes`).

`key`  
La clave de cifrado (256 bits).

## Valores devueltos

Devuelve la cadena cifrada.

## Errores/Excepciones

- Si `nonce` tiene una longitud de bytes diferente de [`SODIUM_CRYPTO_SECRETBOX_NONCEBYTES`](#constant.sodium-crypto-secretbox-noncebytes) (24 bytes), una `SodiumException` será lanzada.

- Si `key` tiene una longitud de bytes diferente de [`SODIUM_CRYPTO_SECRETBOX_KEYBYTES`](#constant.sodium-crypto-secretbox-keybytes) (32 bytes), una `SodiumException` será lanzada.

- Lanza una `SodiumException` en caso de fallo.

## Ejemplos

Ejemplo de `sodium_crypto_secretbox`

```
<?php
// La $key debe ser mantenida confidencial
$key = sodium_crypto_secretbox_keygen();
// No reutilizar $nonce con la misma clave
$nonce = random_bytes(SODIUM_CRYPTO_SECRETBOX_NONCEBYTES);
$plaintext = "mensaje a ser cifrado";
$ciphertext = sodium_crypto_secretbox($plaintext, $nonce, $key);

var_dump(bin2hex($ciphertext));
// El mismo nonce y la misma clave son necesarios para descifrar el $ciphertext
var_dump(sodium_crypto_secretbox_open($ciphertext, $nonce, $key));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(78) "3a1fa3e9f7b72ef8be51d40abf8e296c6899c185d07b18b4c93e7f26aa776d24c50852cd6b1076"
    string(23) "mensaje a ser cifrado"

## Véase también

sodium_crypto_secretbox_open

sodium_crypto_secretbox_keygen

random_bytes
