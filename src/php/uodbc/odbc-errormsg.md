---
title: odbc_errormsg
description: Lee el último mensaje de error
source_url: https://www.php.net/manual/es/function.odbc-errormsg.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-errormsg.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 98780
---

odbc_errormsg

Lee el último mensaje de error

## Descripción

```php
odbc_errormsg([Odbc\Connection $odbc]): string
```php

Devuelve un string que contiene el último mensaje de error ODBC, o un string vacío si no hubo error.

## Parámetros

`odbc`  
El objeto de conexión ODBC, ver la documentación de la función `odbc_connect` para más detalles.

## Valores devueltos

Si `odbc` está especificado, el último estado ODBC de esta conexión es devuelto.

Esta función devuelve un valor significativo únicamente si la última consulta ODBC falló (i.e. la función `odbc_exec` devolvió `false`).

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `odbc` ahora espera una instancia de `Odbc\Connection` ; anteriormente, se esperaba un `resource`. |
| 8.0.0 | `odbc` es ahora nullable. |

## Véase también

`odbc_error`, `odbc_exec`
