---
title: pg_num_fields
description: Devuelve el número de campos
source_url: https://www.php.net/manual/es/function.pg-num-fields.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-num-fields.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63460
---

pg_num_fields

Devuelve el número de campos

## Descripción

```php
pg_num_fields(PgSql\Result $result): int
```php

`pg_num_fields` devuelve el número de campos (o columnas) de una instancia `PgSql\Result`.

> [!NOTE]
> Anteriormente, esta función se llamaba `pg_numfields`.

## Parámetros

`result`  
Una instancia `PgSql\Result`, devuelta por `pg_query`, `pg_query_params`, o `pg_execute` (entre otros).

## Valores devueltos

El número de campos (o columnas) en el conjunto de resultados. En caso de error, se devuelve -1.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `result` ahora espera una instancia de `PgSql\Result` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_num_fields`

```
<?php
$result = pg_query($conn, "SELECT 1, 2");

$num = pg_num_fields($result);

echo $num . " campo(s) devuelto(s).\n";
?>

    
```php

El ejemplo anterior mostrará:

    2 campo(s) devuelto(s).

## Véase también

`pg_num_rows`, `pg_affected_rows`
