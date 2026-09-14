---
title: odbc_field_len
description: Lee la longitud de un campo
source_url: https://www.php.net/manual/es/function.odbc-field-len.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-field-len.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 98850
---

odbc_field_len

Lee la longitud de un campo

## Descripción

```php
odbc_field_len(Odbc\Result $statement, int $field): int
```php

Lee la longitud del campo identificado por su número.

## Parámetros

`statement`  
The ODBC result object.

`field`  
El número del campo. La numeración comienza en 1.

## Valores devueltos

Devuelve la longitud del campo o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `statement` ahora espera una instancia de `Odbc\Result` ; anteriormente, se esperaba un `resource`. |

## Véase también

`odbc_field_scale`para conocer la escala de un número de coma flotante
