---
title: pg_affected_rows
description: Devuelve el número de filas afectadas
source_url: https://www.php.net/manual/es/function.pg-affected-rows.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-affected-rows.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: 5f1a92089
order: 62850
---

pg_affected_rows

Devuelve el número de filas afectadas

## Descripción

```php
pg_affected_rows(PgSql\Result $result): int
```php

`pg_affected_rows` devuelve el número de filas afectadas por las consultas de tipo `INSERT`, `UPDATE` y `DELETE`.

El servidor devuelve el número de filas seleccionadas por SELECT.

> [!NOTE]
> Anteriormente, esta función se llamaba `pg_cmdtuples`.

## Parámetros

`result`  
Una instancia `PgSql\Result`, devuelta por `pg_query`, `pg_query_params`, o `pg_execute` (entre otros).

## Valores devueltos

El número de filas afectadas por la consulta. Si no hay tuplas afectadas, la función devolverá `0`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `result` ahora espera una instancia de `PgSql\Result` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_affected_rows`

```
<?php
$result = pg_query($conn, "INSERT INTO editeur VALUES ('Auteur')");

$cmdtuples = pg_affected_rows($result);

echo $cmdtuples . " filas han sido afectadas.\n";
?>

    
```php

El ejemplo anterior mostrará:

    1 filas han sido afectadas.

## Véase también

`pg_query`, `pg_query_params`, `pg_execute`, `pg_num_rows`
