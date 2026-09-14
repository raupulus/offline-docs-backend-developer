---
title: odbc_error
description: Lee el último código de error
source_url: https://www.php.net/manual/es/function.odbc-error.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-error.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 98770
---

odbc_error

Lee el último código de error

## Descripción

```php
odbc_error([Odbc\Connection $odbc]): string
```php

Devuelve un estado ODBC de 6 dígitos, o una cadena vacía si no había más errores.

## Parámetros

`odbc`  
El objeto de conexión ODBC, ver la documentación de la función `odbc_connect` para más detalles.

## Valores devueltos

Si `odbc` está especificado, se devuelve el último estado de esa conexión, de lo contrario se devuelve el último estado de cualquier conexión.

Esta función devuelve un valor significativo únicamente si la última consulta ODBC ha fallado (es decir, la función `odbc_exec` ha devuelto `false`).

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `odbc` ahora espera una instancia de `Odbc\Connection` ; anteriormente, se esperaba un `resource`. |
| 8.0.0 | `odbc` es ahora nullable. |

## Véase también

`odbc_errormsg`, `odbc_exec`
