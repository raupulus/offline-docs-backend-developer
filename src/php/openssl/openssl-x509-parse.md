---
title: openssl_x509_parse
description: Analiza un certificado X509
source_url: https://www.php.net/manual/es/function.openssl-x509-parse.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-x509-parse.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: af4e920c7
order: 59620
---

openssl_x509_parse

Analiza un certificado X509

## Descripción

```php
openssl_x509_parse(OpenSSLCertificate $certificate, [bool $short_names]): array
```php

`openssl_x509_parse` analiza el certificado X509 `certificate`, y devuelve las informaciones contenidas en él, incluyendo el sujeto (`subject`), nombre (`name`), emisor (`issuer name`), fechas de inicio y fin (`valid from date` y `valid to date`), etc.

## Parámetros

`certificate`  
Certificado X509. Ver [parámetro de Clave/Certificado](#openssl.certparams) para una lista de valores válidos.

`short_names`  
`short_names` controla la indexación de los datos en el array: si `short_names` vale `true` (valor por omisión), entonces los campos serán indexados con la forma corta de los nombres, de lo contrario, se utilizarán los nombres largos. (por ejemplo, `CN` es el nombre corto de `commonName`).

## Valores devueltos

*La estructura de los datos devueltos es (intencionalmente) no documentada, ya que está sujeta a cambios sin previo aviso.*

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | El análisis de un certificado sin segundos en UTCTime ya no es permitido para ninguna versión de OpenSSL. Esto ya estaba prohibido para OpenSSL versión 3.3+. |
| 8.0.0 | `certificate` ahora acepta una instancia de `OpenSSLCertificate`; anteriormente, se aceptaba un `resource` de tipo `OpenSSL X.509`. |
