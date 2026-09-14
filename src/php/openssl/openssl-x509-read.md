---
title: openssl_x509_read
description: Analiza un certificado X.509 y devuelve un objeto
source_url: https://www.php.net/manual/es/function.openssl-x509-read.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-x509-read.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 47881dcf5
order: 59630
---

openssl_x509_read

Analiza un certificado X.509 y devuelve un objeto

## Descripción

```php
openssl_x509_read(OpenSSLCertificate $certificate): OpenSSLCertificate
```php

`openssl_x509_read` analiza el certificado `certificate` y devuelve un objeto `OpenSSLCertificate` para este.

## Parámetros

`certificate`  
Certificado X509. Ver [parámetros clave/certificados](#openssl.certparams) para la lista de valores válidos.

## Valores devueltos

Devuelve un `OpenSSLCertificate` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Se emite un `E_WARNING` si no se puede recuperar el certificado X.509.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | En caso de éxito, esta función devuelve ahora una instancia de `OpenSSLCertificate` ; anteriormente, se devolvía un `resource` de tipo `OpenSSL X.509`. |
| 8.0.0 | `certificate` acepta ahora una instancia de `OpenSSLCertificate` ; anteriormente, se aceptaba un `resource` de tipo `OpenSSL X.509`. |
