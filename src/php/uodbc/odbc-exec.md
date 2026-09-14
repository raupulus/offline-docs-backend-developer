---
title: odbc_exec
description: Ejecuta directamente una consulta SQL
source_url: https://www.php.net/manual/es/function.odbc-exec.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-exec.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 98790
---

odbc_exec

Ejecuta directamente una consulta SQL

## Descripción

```php
odbc_exec(Odbc\Connection $odbc, string $query): Odbc\Result
```php

Envía una sentencia SQL al servidor de base de datos.

## Parámetros

`odbc`  
El objeto de conexión ODBC, ver la documentación de la función `odbc_connect` para más detalles.

`query`  
La consulta SQL.

## Valores devueltos

Devuelve un objeto de resultado ODBC si el comando SQL se ejecutó con éxito `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `odbc` ahora espera una instancia de `Odbc\Connection` ; anteriormente, se esperaba un `resource`. |
| 8.4.0 | Esta función ahora devuelve una instancia de `Odbc\Result` ; anteriormente, se devolvía un `resource`. |
| 8.0.0 | `flags` fue eliminado. |

## Véase también

`odbc_prepare`, `odbc_execute`
