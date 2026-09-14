---
title: imap_base64
description: Decodifica un texto codificado en BASE64
source_url: https://www.php.net/manual/es/function.imap-base64.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-base64.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: e2f50c240
order: 37950
---

imap_base64

Decodifica un texto codificado en BASE64

## Descripción

```php
imap_base64(string $string): string
```php

Decodifica el texto `string` codificado en BASE64.

## Parámetros

`string`  
El texto codificado.

## Valores devueltos

Devuelve el texto decodificado, en forma de `string`, o `false` si ocurre un error.

## Véase también

`imap_binary`, `base64_encode`, `base64_decode`, [RFC2045](https://datatracker.ietf.org/doc/html/rfc2045), Sección 6.8
