---
title: odbc_num_rows
description: Número de filas en un resultado
source_url: https://www.php.net/manual/es/function.odbc-num-rows.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-num-rows.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 98970
---

odbc_num_rows

Número de filas en un resultado

## Descripción

```php
odbc_num_rows(Odbc\Result $statement): int
```php

Lee el número de filas en un resultado. Para los comandos INSERT, UPDATE y DELETE, `odbc_num_rows` devuelve el número de filas afectadas. Para los comandos SELECT, esto *PUEDE* ser el número de filas disponibles, pero no es seguro.

## Parámetros

`statement`  
The ODBC result object devuelto por la función `odbc_exec`.

## Valores devueltos

Devuelve el número de filas en el resultado ODBC. Esta función devolverá -1 si ocurre un error.

## Notas

> [!NOTE]
> El uso de la función `odbc_num_rows` para determinar el número de filas disponibles después de un SELECT devolverá -1 con la mayoría de los controladores.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `statement` ahora espera una instancia de `Odbc\Result` ; anteriormente, se esperaba un `resource`. |
