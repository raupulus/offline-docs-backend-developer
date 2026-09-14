---
title: imap_rfc822_parse_headers
description: Analiza un encabezado de correo electrónico
source_url: https://www.php.net/manual/es/function.imap-rfc822-parse-headers.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-rfc822-parse-headers.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: e2f50c240
order: 38470
---

imap_rfc822_parse_headers

Analiza un encabezado de correo electrónico

## Descripción

```php
imap_rfc822_parse_headers(string $headers, [string $default_hostname]): stdClass
```php

Analiza la cadena `headers` y devuelve un objeto que contiene diferentes elementos, similares a la función `imap_header`.

## Parámetros

`headers`  
Los datos a analizar

`default_hostname`  
El nombre del host por defecto

## Valores devueltos

Devuelve un objeto similar al devuelto por la función `imap_header`, excepto por los flags y otras propiedades que provienen del servidor IMAP.

## Véase también

`imap_rfc822_parse_adrlist`
