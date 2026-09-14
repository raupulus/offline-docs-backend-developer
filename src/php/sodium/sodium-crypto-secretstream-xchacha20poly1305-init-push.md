---
title: sodium_crypto_secretstream_xchacha20poly1305_init_push
description: Inicializa un contexto secretstream para el cifrado
source_url: https://www.php.net/manual/es/function.sodium-crypto-secretstream-xchacha20poly1305-init-push.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-secretstream-xchacha20poly1305-init-push.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76740
---

sodium_crypto_secretstream_xchacha20poly1305_init_push

Inicializa un contexto secretstream para el cifrado

## Descripción

```php
#[\SensitiveParameter] sodium_crypto_secretstream_xchacha20poly1305_init_push(string $key): array
```php

Inicializa un contexto secretstream para el cifrado.

## Parámetros

`key`  
La clave de cifrado. Ver `sodium_crypto_secretstream_xchacha20poly1305_keygen`.

## Valores devueltos

Un array con dos valores de string:

El estado del secretstream, necesario para las próximas llamadas

El encabezado del secretstream, que debe ser proporcionado al destinatario para que pueda extraer los datos

## Ejemplos

Ejemplo de `sodium_crypto_secretstream_xchacha20poly1305_init_push`

```
<?php
function encrypt_file(string $inputFilePath, string $outputFilePath, string $key): void
{
    [$state, $header] = sodium_crypto_secretstream_xchacha20poly1305_init_push($key);

    $inputFile = fopen($inputFilePath, 'rb');
    $outputFile = fopen($outputFilePath, 'wb');
    // Escribe el encabezado:
    fwrite($outputFile, $header);
    $inputFileSize = fstat($inputFile)['size'];

    // Cifra el fichero y escribe su contenido en el fichero de salida:
    for ($i = 0; $i < $inputFileSize; $i += 8175) {
        $ptxt_chunk = fread($inputFile, 8175);
        $ctxt_chunk = sodium_crypto_secretstream_xchacha20poly1305_push($state, $ptxt_chunk);
        fwrite($outputFile, $ctxt_chunk);
    }

    sodium_memzero($state);
    fclose($inputFile);
    fclose($outputFile);
}

// sodium_crypto_secretstream_xchacha20poly1305_keygen()
$key = sodium_base642bin('MS0lzb7HC+thY6jY01pkTE/cwsQxnRq0/2L1eL4Hxn8=', SODIUM_BASE64_VARIANT_ORIGINAL);

file_put_contents('hello.txt', 'Hello world!');
encrypt_file('hello.txt', 'hello.txt.encrypted', $key);
var_dump(sodium_bin2hex(file_get_contents('hello.txt.encrypted')));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(106) "971e33b255f0990ef3931caf761c59136efa77b434832f28ec719e3ff73f5aec38b3bba1574ab5b70a8844d8da36a668e802cfea2c"
