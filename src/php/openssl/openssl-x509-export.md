---
title: openssl_x509_export
description: Exporta un certificado a una cadena de caracteres
source_url: https://www.php.net/manual/es/function.openssl-x509-export.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-x509-export.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 497c40ac1
order: 59590
---

openssl_x509_export

Exporta un certificado a una cadena de caracteres

## Descripción

```php
openssl_x509_export(OpenSSLCertificate $certificate, string $output, [bool $no_text]): bool
```php

`openssl_x509_export` almacena un certificado `certificate` en el fichero `output` en formato PEM.

## Parámetros

`certificate`  
Ver los [parámetros clave/Certificados](#openssl.certparams) para una lista de valores válidos.

`output`  
En caso de éxito, contendrá el PEM.

`no_text`  
El parámetro opcional `notext` afecta al nivel de verbosidad del display; si vale `false`, se añadirán información legible por humanos en el display. Por defecto, el parámetro `notext` vale `true`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `certificate` acepta ahora una instancia de `OpenSSLCertificate`; anteriormente, se aceptaba un `resource` de tipo `OpenSSL X.509`. |
