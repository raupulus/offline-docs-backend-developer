---
title: openssl_free_key
description: Libera los recursos
source_url: https://www.php.net/manual/es/function.openssl-free-key.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-free-key.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 9b1673cf1
order: 59170
---

openssl_free_key

Libera los recursos

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.0.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] openssl_free_key(OpenSSLAsymmetricKey $key): void
```php

`openssl_free_key` libera las claves asociadas a `key` de la memoria.

## Parámetros

`key`  

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función es ahora obsoleta ya que no tiene ningún efecto. |
| 8.0.0 | `key` acepta ahora una instancia de `OpenSSLAsymmetricKey`; anteriormente, se aceptaba un `resource` de tipo `OpenSSL key`. |
