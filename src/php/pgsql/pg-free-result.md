---
title: pg_free_result
description: Libera la memoria
source_url: https://www.php.net/manual/es/function.pg-free-result.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-free-result.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: b984d790e
order: 63230
---

pg_free_result

Libera la memoria

## Descripción

```php
pg_free_result(PgSql\Result $result): bool
```php

`pg_free_result` libera la memoria y los datos asociados con la instancia `PgSql\Result`.

`pg_free_result` solo es realmente útil si existe el riesgo de utilizar demasiada memoria durante el script. La memoria ocupada por los resultados se libera automáticamente al final del script.

> [!NOTE]
> Anteriormente, esta función se llamaba `pg_freeresult`.

## Parámetros

`result`  
Una instancia `PgSql\Result`, devuelta por `pg_query`, `pg_query_params`, o `pg_execute` (entre otros).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `result` ahora espera una instancia de `PgSql\Result` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_free_result`

```
<?php
$db = pg_connect("dbname=users user=me");

$res = pg_query($db, "SELECT 1 UNION ALL SELECT 2");

$val = pg_fetch_result($res, 1, 0);

echo "El primer campo de la segunda línea es: ", $val, "\n";

pg_free_result($res);
?>

    
```php

El ejemplo anterior mostrará:

    El primer campo de la segunda línea es: 2

## Véase también

`pg_query`, `pg_query_params`, `pg_execute`, `pg_result_memory_size`
