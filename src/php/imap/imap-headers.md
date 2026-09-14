---
title: imap_headers
description: Devuelve los encabezados de todos los mensajes de un buzón de correo
source_url: https://www.php.net/manual/es/function.imap-headers.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-headers.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 38220
---

imap_headers

Devuelve los encabezados de todos los mensajes de un buzón de correo

## Descripción

```php
imap_headers(IMAP\Connection $imap): array
```php

Devuelve los encabezados de todos los mensajes de un buzón de correo.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

## Valores devueltos

Devuelve un array de strings que contienen los encabezados de los mensajes: un string por mensaje. Devuelve `false` en caso de fallo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |
