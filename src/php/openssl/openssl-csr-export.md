---
title: openssl_csr_export
description: Exporta un CSR a un fichero o una variable
source_url: https://www.php.net/manual/es/function.openssl-csr-export.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-csr-export.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 497c40ac1
order: 59070
---

openssl_csr_export

Exporta un

CSR

a un fichero o una variable

## Descripción

```php
openssl_csr_export(OpenSSLCertificateSigningRequest $csr, string $output, [bool $no_text]): bool
```php

`openssl_csr_export` toma la solicitud de firma de certificado representada por `CSR` y la almacena en formato PEM en `output`, que es pasado por referencia.

## Parámetros

`csr`  
Ver los [parámetros CSR](#openssl.certparams) para obtener una lista de los valores válidos.

`output`  
En caso de éxito, esta cadena contendrá el CSR codificado en PEM

`no_text`  
El parámetro opcional `notext` afecta al nivel de verbosidad del display; si vale `false`, se añadirán información legible por humanos en el display. Por defecto, el parámetro `notext` vale `true`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `csr` ahora acepta una instancia de `OpenSSLCertificateSigningRequest`; anteriormente, se aceptaba un `resource` de tipo `OpenSSL X.509 CSR`. |

## Ejemplos

Ejemplo de openssl_csr_export()

```
<?php
$subject = array(
    "commonName" => "example.com",
);
$private_key = openssl_pkey_new(array(
    "private_key_bits" => 2048,
    "private_key_type" => OPENSSL_KEYTYPE_RSA,
));
$configargs = array(
    'digest_alg' => 'sha256WithRSAEncryption'
);
$csr = openssl_csr_new($subject, $private_key, $configargs);
openssl_csr_export($csr, $csr_string);
echo $csr_string;
?>

    
```php

## Véase también

`openssl_csr_export_to_file`, `openssl_csr_new`, `openssl_csr_sign`
