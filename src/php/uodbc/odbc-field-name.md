---
title: odbc_field_name
description: Lee el nombre de la columna
source_url: https://www.php.net/manual/es/function.odbc-field-name.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-field-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 98860
---

odbc_field_name

Lee el nombre de la columna

## Descripción

```php
odbc_field_name(Odbc\Result $statement, int $field): string
```php

Obtiene el nombre del campo que ocupa el número de columna dado en el objeto resultado especificado.

## Parámetros

`statement`  
The ODBC result object.

`field`  
El número de la columna. La numeración comienza en 1.

## Valores devueltos

Devuelve el nombre de la columna, como un `string`, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `statement` ahora espera una instancia de `Odbc\Result` ; anteriormente, se esperaba un `resource`. |
