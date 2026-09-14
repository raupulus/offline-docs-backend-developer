---
title: openssl_x509_free
description: Libera los recursos tomados por un certificado
source_url: https://www.php.net/manual/es/function.openssl-x509-free.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-x509-free.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 9b1673cf1
order: 59610
---

openssl_x509_free

Libera los recursos tomados por un certificado

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.0.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] openssl_x509_free(OpenSSLCertificate $certificate): void
```php

> [!NOTE]
> Esta función no tiene ningún efecto. Anterior a PHP 8.0.0, esta función era utilizada para cerrar un recurso.

`openssl_x509_free` libera los recursos de memoria tomados por el certificado `certificate`.

## Parámetros

`certificate`  

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función es ahora obsoleta ya que no tiene ningún efecto. |
| 8.0.0 | `certificate` ahora acepta una instancia de `OpenSSLCertificate`; anteriormente, se aceptaba un `resource` de tipo `OpenSSL X.509`. |
