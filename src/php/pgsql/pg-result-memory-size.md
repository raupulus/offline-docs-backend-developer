---
title: pg_result_memory_size
description: Devuelve la cantidad de memoria asignada para un resultado de consulta
source_url: https://www.php.net/manual/es/function.pg-result-memory-size.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-result-memory-size.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: true
translation_revision: 0e3624a28
order: 63610
---

pg_result_memory_size

Devuelve la cantidad de memoria asignada para un resultado de consulta

## Descripción

```php
pg_result_memory_size(PgSql\Result $result): int
```php

Devuelve la cantidad de memoria, en bytes, asignada para la instancia de `PgSql\Result` especificada. Este valor es el mismo que el que sería liberado por `pg_free_result`.

## Parámetros

`result`  
Una instancia `PgSql\Result`, devuelta por `pg_query`, `pg_query_params`, o `pg_execute` (entre otros).

## Valores devueltos

Devuelve la cantidad de memoria en bytes.

## Ejemplos

Ejemplo de `pg_result_memory_size`

```
<?php
$db = pg_connect("dbname=users user=me");

$res = pg_query($db, 'SELECT 1');

$size = pg_result_memory_size($res);

var_dump($size);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(3288)

## Véase también

pg_free_result
