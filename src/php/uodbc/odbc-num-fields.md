---
title: odbc_num_fields
description: Número de columnas en un resultado
source_url: https://www.php.net/manual/es/function.odbc-num-fields.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-num-fields.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 98960
---

odbc_num_fields

Número de columnas en un resultado

## Descripción

```php
odbc_num_fields(Odbc\Result $statement): int
```php

Obtiene el número de columnas en un resultado ODBC.

## Parámetros

`statement`  
The ODBC result object devuelto por la función `odbc_exec`.

## Valores devueltos

Devuelve el número de columnas, o -1 en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `statement` ahora espera una instancia de `Odbc\Result` ; anteriormente, se esperaba un `resource`. |
