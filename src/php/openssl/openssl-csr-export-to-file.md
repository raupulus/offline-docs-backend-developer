---
title: openssl_csr_export_to_file
description: Exporta una CSR a un fichero
source_url: https://www.php.net/manual/es/function.openssl-csr-export-to-file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-csr-export-to-file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 497c40ac1
order: 59060
---

openssl_csr_export_to_file

Exporta una CSR a un fichero

## Descripción

```php
openssl_csr_export_to_file(OpenSSLCertificateSigningRequest $csr, string $output_filename, [bool $no_text]): bool
```php

`openssl_csr_export_to_file` toma la CSR representada por el argumento `csr` y la guarda en formato PEM en el fichero nombrado `output_filename`.

## Parámetros

`csr`  
Ver los [parámetros CSR](#openssl.certparams) para obtener una lista de los valores válidos.

`output_filename`  
Ruta hacia el fichero de salida.

`no_text`  
El parámetro opcional `notext` afecta al nivel de verbosidad del display; si vale `false`, se añadirán información legible por humanos en el display. Por defecto, el parámetro `notext` vale `true`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `csr` ahora acepta una instancia de `OpenSSLCertificateSigningRequest`; anteriormente, se aceptaba un `resource` de tipo `OpenSSL X.509 CSR`. |

## Ejemplos

Ejemplo de openssl_csr_export_to_file()

```
<?php
$subject = array(
    "commonName" => "example.com",
);
$private_key = openssl_pkey_new(array(
    "private_key_bits" => 2048,
    "private_key_type" => OPENSSL_KEYTYPE_RSA,
));
$csr = openssl_csr_new($subject, $private_key, array('digest_alg' => 'sha384') );
openssl_pkey_export_to_file($private_key, 'example-priv.key');
// Al mismo tiempo que el sujeto, la CSR contiene la clave pública correspondiente a la clave privada
openssl_csr_export_to_file($csr, 'example-csr.pem');
?>

    
```php

## Véase también

`openssl_csr_export`, `openssl_csr_new`, `openssl_csr_sign`
