---
title: sodium_crypto_secretstream_xchacha20poly1305_init_pull
description: Inicializa un contexto secretstream para el descifrado
source_url: https://www.php.net/manual/es/function.sodium-crypto-secretstream-xchacha20poly1305-init-pull.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-secretstream-xchacha20poly1305-init-pull.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76730
---

sodium_crypto_secretstream_xchacha20poly1305_init_pull

Inicializa un contexto secretstream para el descifrado

## Descripción

```php
#[\SensitiveParameter] sodium_crypto_secretstream_xchacha20poly1305_init_pull(string $header, string $key): string
```php

Inicializa un contexto secretstream para el descifrado.

## Parámetros

`header`  
La cabecera del secretstream. Debe ser uno de los valores producidos por `sodium_crypto_secretstream_xchacha20poly1305_init_push`.

`key`  
La clave de cifrado (256 bits).

## Valores devueltos

El estado del secretstream.

## Ejemplos

Ejemplo de `sodium_crypto_secretstream_xchacha20poly1305_init_pull`

```
<?php
function decrypt_file(string $inputFilePath, string $outputFilePath, string $key): void
{
    $inputFile = fopen($inputFilePath, 'rb');
    $outputFile = fopen($outputFilePath, 'wb');
    $header = fread($inputFile, 24);

    $state = sodium_crypto_secretstream_xchacha20poly1305_init_pull($header, $key);
    $inputFileSize = fstat($inputFile)['size'];

    // Descifra el fichero y escribe su contenido en el fichero de salida:
    for ($i = 24; $i < $inputFileSize; $i += 8192) {
        $ctxt_chunk = fread($inputFile, 8192);

        // No se utiliza $tag, pero en protocolos reales, puede ser utilizado para cifrar, por ejemplo
        // desencadenar una nueva clave o indicar el final del fichero. Luego, durante el descifrado, se puede
        // verificar este comportamiento.
        [$ptxt_chunk, $tag] = sodium_crypto_secretstream_xchacha20poly1305_pull($state, $ctxt_chunk);
        fwrite($outputFile, $ptxt_chunk);
    }

    sodium_memzero($state);
    fclose($inputFile);
    fclose($outputFile);
}

// sodium_crypto_secretstream_xchacha20poly1305_keygen()
$key = sodium_base642bin('MS0lzb7HC+thY6jY01pkTE/cwsQxnRq0/2L1eL4Hxn8=', SODIUM_BASE64_VARIANT_ORIGINAL);

$example = sodium_hex2bin('971e33b255f0990ef3931caf761c59136efa77b434832f28ec719e3ff73f5aec38b3bba1574ab5b70a8844d8da36a668e802cfea2c');
file_put_contents('hello.enc', $example);
decrypt_file('hello.enc', 'hello.txt.decrypted', $key);
var_dump(file_get_contents('hello.txt.decrypted'));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(12) "Hello world!"
