---
title: odbc_result_all
description: Muestra el resultado en forma de tabla HTML
source_url: https://www.php.net/manual/es/function.odbc-result-all.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-result-all.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 99030
---

odbc_result_all

Muestra el resultado en forma de tabla HTML

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.1.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] odbc_result_all(Odbc\Result $statement, [string $format]): int
```php

Muestra todas las filas de un resultado producido por `odbc_exec`. La visualización se realiza en formato HTML. Los datos *no están* escapados.

Esta función no está destinada a ser utilizada en un entorno de producción; está prevista para el desarrollo para mostrar rápidamente un conjunto de resultados.

## Parámetros

`statement`  
The ODBC result object.

`format`  
Permite modificar el aspecto global de la tabla.

## Valores devueltos

Devuelve el número de filas del resultado, o `false` si se produce un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `statement` ahora espera una instancia de `Odbc\Result` ; anteriormente, se esperaba un `resource`. |
| 8.1.0 | Esta función ha sido declarada obsoleta. |
