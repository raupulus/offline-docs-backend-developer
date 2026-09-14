---
title: openssl_csr_get_subject
description: Retorna el sujeto de una CSR
source_url: https://www.php.net/manual/es/function.openssl-csr-get-subject.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-csr-get-subject.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 4cbf70602
order: 59090
---

openssl_csr_get_subject

Retorna el sujeto de una

CSR

## Descripción

```php
openssl_csr_get_subject(OpenSSLCertificateSigningRequest $csr, [bool $short_names]): array
```php

`openssl_csr_get_subject` retorna las informaciones sobre el nombre distintivo del sujeto codificado en el `csr`, incluyendo los campos commonName (CN), organizationName (O), countryName (C) etc.

## Parámetros

`csr`  
Ver los [parámetros CSR](#openssl.certparams) para obtener una lista de los valores válidos.

`short_names`  
`short_names` controla cómo los datos son indexados en el array - si `short_names` es `true` (por omisión) entonces los campos serán indexados con la forma corta del nombre, de lo contrario el nombre completo será utilizado - por ejemplo: CN es la forma corta de commonName.

## Valores devueltos

Retorna un `array` asociativo con las descripciones de los sujetos, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `csr` ahora acepta una instancia de `OpenSSLCertificateSigningRequest` ; anteriormente, se aceptaba un `resource` de tipo `OpenSSL X.509 CSR`. |

## Ejemplos

Ejemplo con openssl_csr_get_subject()

```
<?php
$subject = array(
    "countryName" => "CA",
    "stateOrProvinceName" => "Alberta",
    "localityName" => "Calgary",
    "organizationName" => "XYZ Widgets Inc",
    "organizationalUnitName" => "PHP Documentation Team",
    "commonName" => "Wez Furlong",
    "emailAddress" => "wez@example.com",
);
$private_key = openssl_pkey_new(array(
    "private_key_bits" => 2048,
    "private_key_type" => OPENSSL_KEYTYPE_RSA,
));
$configargs = array(
    'digest_alg' => 'sha512WithRSAEncryption'
);
$csr = openssl_csr_new($subject, $privkey, $configargs);
print_r(openssl_csr_get_subject($csr));
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [C] => CA
        [ST] => Alberta
        [L] => Calgary
        [O] => XYZ Widgets Inc
        [OU] => PHP Documentation Team
        [CN] => Wez Furlong
        [emailAddress] => wez@example.com
    )

## Véase también

`openssl_csr_new`, `openssl_csr_get_public_key`, `openssl_x509_parse`
