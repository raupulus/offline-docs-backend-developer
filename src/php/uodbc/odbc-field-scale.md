---
title: odbc_field_scale
description: Lee la escala de un campo
source_url: https://www.php.net/manual/es/function.odbc-field-scale.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-field-scale.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: e2f2172bf
order: 98890
---

odbc_field_scale

Lee la escala de un campo

## Descripción

```php
odbc_field_scale(Odbc\Result $statement, int $field): int
```php

Lee la escala del campo referenciado por número en el resultado ODBC dado.

## Parámetros

`statement`  
The ODBC result object.

`field`  
El número del campo. La numeración comienza en 1.

## Valores devueltos

Devuelve la escala del campo, en forma de `int`, o `false` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `statement` ahora espera una instancia de `Odbc\Result` ; anteriormente, se esperaba un `resource`. |
