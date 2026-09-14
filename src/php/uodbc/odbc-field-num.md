---
title: odbc_field_num
description: Número de columna
source_url: https://www.php.net/manual/es/function.odbc-field-num.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-field-num.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: e2f2172bf
order: 98870
---

odbc_field_num

Número de columna

## Descripción

```php
odbc_field_num(Odbc\Result $statement, string $field): int
```php

Obtiene el número de la columna correspondiente al campo nombrado en el objeto resultado especificado.

## Parámetros

`statement`  
The ODBC result object.

`field`  
El nombre del campo.

## Valores devueltos

Devuelve el número del campo, en forma de `int`, o `false` si ocurre un error. La numeración comienza en 1.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `statement` ahora espera una instancia de `Odbc\Result` ; anteriormente, se esperaba un `resource`. |
