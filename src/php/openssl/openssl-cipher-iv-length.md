---
title: openssl_cipher_iv_length
description: Obtiene la longitud del vector de inicialización cipher
source_url: https://www.php.net/manual/es/function.openssl-cipher-iv-length.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-cipher-iv-length.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: d1e3ea622
order: 58990
---

openssl_cipher_iv_length

Obtiene la longitud del vector de inicialización cipher

## Descripción

```php
openssl_cipher_iv_length(string $cipher_algo): int
```php

Obtiene la longitud del vector de inicialización cipher.

## Parámetros

`cipher_algo`  
El método cipher. Consulte la función `openssl_get_cipher_methods` para obtener una lista de valores potenciales.

## Valores devueltos

Devuelve la longitud cipher en caso de éxito, o `false` si ocurre un error.

## Errores/Excepciones

Genera un error de nivel `E_WARNING` cuando el algoritmo cipher es desconocido.

## Ejemplos

Ejemplo con `openssl_cipher_iv_length`

```
<?php
$method = 'AES-128-CBC';
$ivlen = openssl_cipher_iv_length($method);

echo $ivlen;
?>

   
```php

Resultado del ejemplo anterior es similar a:

    16
