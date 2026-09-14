---
title: odbc_cursor
description: Lee el nombre del puntero de resultado actual
source_url: https://www.php.net/manual/es/function.odbc-cursor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-cursor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 98740
---

odbc_cursor

Lee el nombre del puntero de resultado actual

## Descripción

```php
odbc_cursor(Odbc\Result $statement): string
```php

Lee el nombre del puntero del resultado actual.

## Parámetros

`statement`  
The ODBC result object.

## Valores devueltos

Devuelve el nombre del cursor, en forma de `string`, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `statement` ahora espera una instancia de `Odbc\Result` ; anteriormente, se esperaba un `resource`. |
