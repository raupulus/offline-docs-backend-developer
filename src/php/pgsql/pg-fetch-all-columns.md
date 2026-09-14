---
title: pg_fetch_all_columns
description: Recupera todas las filas de una columna particular de resultados como
  un array
source_url: https://www.php.net/manual/es/function.pg-fetch-all-columns.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-fetch-all-columns.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63070
---

pg_fetch_all_columns

Recupera todas las filas de una columna particular de resultados como un array

## Descripción

```php
pg_fetch_all_columns(PgSql\Result $result, [int $field]): array
```php

`pg_fetch_all_columns` devuelve un array que contiene todas las filas (registros) de una columna particular de una instancia de `PgSql\Result`.

> [!NOTE]
> Esta función define los campos NULL al valor PHP `null`.

## Parámetros

`result`  
Una instancia `PgSql\Result`, devuelta por `pg_query`, `pg_query_params`, o `pg_execute` (entre otros).

`field`  
Número de la columna. Por omisión, la primera columna si no se especifica.

## Valores devueltos

Un `array` que contiene todos los valores de una columna del resultado.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `result` ahora espera una instancia de `PgSql\Result` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_fetch_all_columns`

```
<?php
$conn = pg_pconnect("dbname=publisher");
if (!$conn) {
  echo "Se ha producido un error.\n";
  exit;
}

$result = pg_query($conn, "SELECT title, name, address FROM authors");
if (!$result) {
  echo "Se ha producido un error.\n";
  exit;
}

// Recupera un array que contiene todos los nombres de autores
$arr = pg_fetch_all_columns($result, 1);

var_dump($arr);

?>

    
```php

## Véase también

`pg_fetch_all`
