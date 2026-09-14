---
title: openssl_x509_fingerprint
description: Calcula la huella digital o el resumen de un certificado X.509 dado
source_url: https://www.php.net/manual/es/function.openssl-x509-fingerprint.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-x509-fingerprint.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: d1e3ea622
order: 59600
---

openssl_x509_fingerprint

Calcula la huella digital o el resumen de un certificado X.509 dado

## Descripción

```php
openssl_x509_fingerprint(OpenSSLCertificate $certificate, [string $digest_algo], [bool $binary]): string
```php

La función `openssl_x509_fingerprint` devuelve el resumen de un certificado `certificate` en forma de `string`.

## Parámetros

`certificate`  
Ver los [parámetros clave/Certificados](#openssl.certparams) para una lista de valores válidos.

`digest_algo`  
El método de resumen o el algoritmo de hash a utilizar, por ejemplo "sha256", uno de `openssl_get_md_methods`.

`binary`  
Cuando se define como `true`, muestra los datos binarios sin tratar. `false` muestra en hexits minúsculas.

## Valores devueltos

Devuelve una `string` que contiene la huella digital calculada del certificado en forma de hexits minúsculas, a menos que `binary` esté definido como `true` en cuyo caso se devuelve la representación binaria sin tratar del resumen del mensaje.

Devuelve `false` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `certificate` ahora acepta una instancia de `OpenSSLCertificate`; anteriormente, se aceptaba un `resource` de tipo `OpenSSL X.509`. |
