---
title: odbc_field_type
description: Tipo de datos de un campo
source_url: https://www.php.net/manual/es/function.odbc-field-type.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-field-type.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 98900
---

odbc_field_type

Tipo de datos de un campo

## Descripción

```php
odbc_field_type(Odbc\Result $statement, int $field): string
```php

Lee el tipo de datos SQL de un campo, identificado por su número.

## Parámetros

`statement`  
The ODBC result object.

`field`  
El número del campo. La numeración comienza en 1.

## Valores devueltos

Devuelve el tipo del campo, en forma de `string`, o `false` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `statement` ahora espera una instancia de `Odbc\Result` ; anteriormente, se esperaba un `resource`. |
