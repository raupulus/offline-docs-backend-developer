---
title: openssl_cms_read
description: Exporta el fichero CMS a un array de certificados PEM
source_url: https://www.php.net/manual/es/function.openssl-cms-read.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-cms-read.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: true
translation_revision: 497c40ac1
order: 59030
---

openssl_cms_read

Exporta el fichero CMS a un array de certificados

PEM

## Descripción

```php
openssl_cms_read(string $input_filename, array $certificates): bool
```php

Realiza la operación inversa de `openssl_pkcs7_read`.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`input_filename`  

`certificates`  

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
