---
title: openssl_x509_export_to_file
description: Exporta un certificado a un archivo
source_url: https://www.php.net/manual/es/function.openssl-x509-export-to-file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-x509-export-to-file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 497c40ac1
order: 59580
---

openssl_x509_export_to_file

Exporta un certificado a un archivo

## Descripción

```php
openssl_x509_export_to_file(OpenSSLCertificate $certificate, string $output_filename, [bool $no_text]): bool
```php

`openssl_x509_export_to_file` almacena un certificado `certificate` en el archivo `output_filename` en formato PEM.

## Parámetros

`certificate`  
Ver los [parámetros clave/Certificados](#openssl.certparams) para una lista de valores válidos.

`output_filename`  
Ruta del archivo de salida.

`no_text`  
El parámetro opcional `notext` afecta al nivel de verbosidad del display; si vale `false`, se añadirán información legible por humanos en el display. Por defecto, el parámetro `notext` vale `true`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `certificate` acepta ahora una instancia de `OpenSSLCertificate`; anteriormente, se aceptaba un `resource` de tipo `OpenSSL X.509`. |
