---
title: odbc_fetch_object
description: Lee una línea de resultado en un objeto
source_url: https://www.php.net/manual/es/function.odbc-fetch-object.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-fetch-object.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 98830
---

odbc_fetch_object

Lee una línea de resultado en un objeto

## Descripción

```php
odbc_fetch_object(Odbc\Result $statement, [int $row]): stdClass
```php

Lee un `object` desde una consulta ODBC.

## Parámetros

`statement`  
The ODBC result object desde `odbc_exec`.

`row`  
El número de línea a recuperar, opcional.

## Valores devueltos

Devuelve un objeto que corresponde a la línea recuperada, o `false` si no hay más líneas disponibles.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `statement` ahora espera una instancia de `Odbc\Result` ; anteriormente, se esperaba un `resource`. |
| 8.4.0 | `row` es ahora nullable. |

## Notas

> [!NOTE]
> Esta función está disponible cuando PHP es compilado con soporte IBM DB2 o UnixODBC.

## Véase también

`odbc_fetch_row`, `odbc_fetch_array`, `odbc_num_rows`
