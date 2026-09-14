---
title: openssl_pkcs12_read
description: Lee un certificado PKCS#12 en un array
source_url: https://www.php.net/manual/es/function.openssl-pkcs12-read.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-pkcs12-read.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: e2f2172bf
order: 59300
---

openssl_pkcs12_read

Lee un certificado

PKCS

\#12 en un array

## Descripción

```php
#[\SensitiveParameter] openssl_pkcs12_read(string $pkcs12, array $certificates, string $passphrase): bool
```php

`openssl_pkcs12_read` lee el certificado PKCS#12 proporcionado por el argumento `pkcs12` en un array denominado `certificates`.

## Parámetros

`pkcs12`  
El contenido del almacén de certificados, no el nombre del fichero.

`certificates`  
En caso de éxito, este array contendrá los datos del certificado.

`passphrase`  
Frase de contraseña para desencriptar el archivo PKCS#12.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

`openssl_pkcs12_read` example

```
<?php
if (!$cert_store = file_get_contents("/certs/file.p12")) {
    echo "Error: No se pudo leer el fichero de certificado\n";
    exit;
}

if (openssl_pkcs12_read($cert_store, $cert_info, "my_secret_pass")) {
    echo "Información del Certificado\n";
    print_r($cert_info);
} else {
    echo "Error: No se pudo leer el almacén de certificados.\n";
    exit;
}
?>

   
```php
