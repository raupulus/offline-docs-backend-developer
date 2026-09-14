---
title: mb_decode_mimeheader
description: Decodifica un encabezado MIME
source_url: https://www.php.net/manual/es/function.mb-decode-mimeheader.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-decode-mimeheader.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: 398329d3c
order: 45020
---

mb_decode_mimeheader

Decodifica un encabezado MIME

## Descripción

```php
mb_decode_mimeheader(string $string): string
```php

Decodifica la cadena codificada `string` en el encabezado MIME.

## Parámetros

`string`  
La cadena a decodificar.

## Valores devueltos

La cadena decodificada, con un codificación interna.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Los guiones bajos son convertidos en espacios como se especifica en [RFC 2047](https://datatracker.ietf.org/doc/html/rfc2047). |

## Véase también

`mb_encode_mimeheader`
