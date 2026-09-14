---
title: openssl_x509_check_private_key
description: Verifica si una clave privada corresponde a un certificado
source_url: https://www.php.net/manual/es/function.openssl-x509-check-private-key.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-x509-check-private-key.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 5bc68add3
order: 59560
---

openssl_x509_check_private_key

Verifica si una clave privada corresponde a un certificado

## Descripción

```php
#[\SensitiveParameter] openssl_x509_check_private_key(OpenSSLCertificate $certificate, OpenSSLAsymmetricKey $private_key): bool
```php

Verifica si el argumento `private_key` proporcionado es la clave privada que corresponde a `certificate`.

> [!WARNING]
> Esta función no verifica si KEY es efectivamente una clave privada o no. Simplemente compara el material público (por ejemplo exponent y modulo de una clave RSA) y/o los parámetros de clave (por ejemplo los parámetros EC de una clave EC) de un par de claves.
>
> Esto significa, por ejemplo, que una clave pública podría ser proporcionada para `private_key` y la función puede devolver `true`.

## Parámetros

`certificate`  
El certificado.

`private_key`  
La clave privada.

## Valores devueltos

Devuelve `true` si `private_key` es la clave privada que corresponde a `certificate`, o `false` en caso contrario.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `certificate` ahora acepta una instancia de `OpenSSLCertificate` ; anteriormente, se aceptaba un `resource` de tipo `OpenSSL X.509`. |
| 8.0.0 | `private_key` ahora acepta una instancia de `OpenSSLAsymmetricKey` o `OpenSSLCertificate` ; anteriormente, se aceptaba un `resource` de tipo `OpenSSL key` o `OpenSSL X.509`. |
