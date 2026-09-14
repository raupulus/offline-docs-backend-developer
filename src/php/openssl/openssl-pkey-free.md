---
title: openssl_pkey_free
description: Libera una clave privada
source_url: https://www.php.net/manual/es/function.openssl-pkey-free.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-pkey-free.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 9b1673cf1
order: 59390
---

openssl_pkey_free

Libera una clave privada

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.0.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] openssl_pkey_free(OpenSSLAsymmetricKey $key): void
```php

> [!NOTE]
> Esta función no tiene ningún efecto. Anterior a PHP 8.0.0, esta función era utilizada para cerrar un recurso.

Libera una clave privada creada por la función `openssl_pkey_new`.

## Parámetros

`key`  
Recurso que representa la clave.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función es ahora obsoleta ya que no tiene ningún efecto. |
| 8.0.0 | `key` acepta ahora una instancia de `OpenSSLAsymmetricKey`; anteriormente, se aceptaba un `resource` de tipo `OpenSSL key`. |
