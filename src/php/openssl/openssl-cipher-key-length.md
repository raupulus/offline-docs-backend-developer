---
title: openssl_cipher_key_length
description: Devuelve la longitud de la clave de cifrado
source_url: https://www.php.net/manual/es/function.openssl-cipher-key-length.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-cipher-key-length.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: true
translation_revision: a68a0b2da
order: 59000
---

openssl_cipher_key_length

Devuelve la longitud de la clave de cifrado

## Descripción

```php
openssl_cipher_key_length(string $cipher_algo): int
```php

Devuelve la longitud de la clave de cifrado.

## Parámetros

`cipher_algo`  
El método de cifrado, ver `openssl_get_cipher_methods` para una lista de valores potenciales.

## Valores devueltos

Devuelve la longitud de la clave de cifrado en caso de éxito, o `false` si ocurre un error.

## Errores/Excepciones

Emite un error de nivel `E_WARNING` cuando el algoritmo de cifrado es desconocido.

## Ejemplos

Ejemplo de `openssl_cipher_key_length`

```
<?php
$method = 'AES-128-CBC';

var_dump(openssl_cipher_key_length($method));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(16)
