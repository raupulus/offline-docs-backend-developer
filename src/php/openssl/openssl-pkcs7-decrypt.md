---
title: openssl_pkcs7_decrypt
description: Descifra un mensaje S/MIME
source_url: https://www.php.net/manual/es/function.openssl-pkcs7-decrypt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-pkcs7-decrypt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 5bc68add3
order: 59310
---

openssl_pkcs7_decrypt

Descifra un mensaje S/MIME

## Descripción

```php
#[\SensitiveParameter] #[\SensitiveParameter] openssl_pkcs7_decrypt(string $input_filename, string $output_filename, OpenSSLCertificate $certificate, [OpenSSLAsymmetricKey $private_key]): bool
```php

Descifra el mensaje S/MIME contenido en el fichero `input_filename`, utilizando el certificado y la clave privada asociados por `certificate` y `private_key`.

## Parámetros

`input_filename`  

`output_filename`  
El mensaje descifrado se escribe en el fichero especificado por este argumento.

`certificate`  

`private_key`  

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `private_key` acepta ahora una instancia de `OpenSSLAsymmetricKey` o `OpenSSLCertificate`; anteriormente, se aceptaba un `resource` de tipo `OpenSSL key` o `OpenSSL X.509 CSR`. |

## Ejemplos

Ejemplo con `openssl_pkcs7_decrypt`

```
<?php
// $cert y $key contienen sus certificados y claves privadas
// Se asume que el mensaje está dirigido a usted
$infilename = "encrypted.msg";  // este fichero contiene su mensaje cifrado
$outfilename = "decrypted.msg"; // asegúrese de poder escribir en este fichero

if (openssl_pkcs7_decrypt($infilename, $outfilename, $cert, $key)) {
    echo "descifrado !";
} else {
    echo "Error al descifrar !";
}
?>

    
```php
