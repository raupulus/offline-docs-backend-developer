---
title: odbc_fetch_array
description: Lee una línea de resultado en un array asociativo
source_url: https://www.php.net/manual/es/function.odbc-fetch-array.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-fetch-array.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 98810
---

odbc_fetch_array

Lee una línea de resultado en un array asociativo

## Descripción

```php
odbc_fetch_array(Odbc\Result $statement, [int $row]): array
```php

Lee un `array` asociativo desde una consulta ODBC.

## Parámetros

`statement`  
The ODBC result object desde `odbc_exec`.

`row`  
El número de la línea que debe ser leída, opcional.

## Valores devueltos

Devuelve un array correspondiente a la línea recuperada, o `false` si no hay más líneas disponibles.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `statement` ahora espera una instancia de `Odbc\Result` ; anteriormente, se esperaba un `resource`. |
| 8.4.0 | `row` es ahora nullable. |

## Notas

> [!NOTE]
> Esta función está disponible cuando PHP es compilado con el soporte IBM DB2 o UnixODBC.

## Véase también

`odbc_fetch_row`, `odbc_fetch_object`, `odbc_num_rows`
