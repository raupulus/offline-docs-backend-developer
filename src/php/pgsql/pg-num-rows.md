---
title: pg_num_rows
description: Devuelve el número de filas de PostgreSQL
source_url: https://www.php.net/manual/es/function.pg-num-rows.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-num-rows.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63470
---

pg_num_rows

Devuelve el número de filas de PostgreSQL

## Descripción

```php
pg_num_rows(PgSql\Result $result): int
```php

`pg_num_rows` devuelve el número de filas de una instancia `PgSql\Result`.

> [!NOTE]
> Anteriormente, esta función se llamaba `pg_numrows`.

## Parámetros

`result`  
Una instancia `PgSql\Result`, devuelta por `pg_query`, `pg_query_params`, o `pg_execute` (entre otros).

## Valores devueltos

El número de filas en el conjunto de resultados. En caso de error, se devuelve `-1`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `result` ahora espera una instancia de `PgSql\Result` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_num_rows`

```
<?php
$result = pg_query($conn, "SELECT 1");

$rows = pg_num_rows($result);

echo $rows . " línea(s) devuelta(s).\n";
?>

    
```php

El ejemplo anterior mostrará:

    1 línea(s) devuelta(s).

## Véase también

`pg_num_fields`, `pg_affected_rows`
