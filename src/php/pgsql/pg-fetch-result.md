---
title: pg_fetch_result
description: Devuelve los valores de un resultado
source_url: https://www.php.net/manual/es/function.pg-fetch-result.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-fetch-result.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: 87c67b277
order: 63120
---

pg_fetch_result

Devuelve los valores de un resultado

## Descripción

```php
pg_fetch_result(PgSql\Result $result, string $row, mixed $field): string
```php

```php
pg_fetch_result(PgSql\Result $result, mixed $field): string
```

`pg_fetch_result` devuelve el valor de una fila y un campo (columna) en particular a partir de una instancia `PgSql\Result`.

> [!NOTE]
> Esta función puede llamarse `pg_result`.

## Parámetros

`result`  
Una instancia `PgSql\Result`, devuelta por `pg_query`, `pg_query_params`, o `pg_execute` (entre otros).

`row`  
Número de la fila a recuperar. Las filas están numeradas a partir de 0. Si el argumento es omitido, se recupera la siguiente fila.

`field`  
Una cadena de tipo `string` que representa el nombre del campo (columna) a recuperar, o un entero de tipo `int` que representa el número del campo a recuperar. Los campos están numerados a partir de 0.

## Valores devueltos

Los valores booleanos son devueltos como "t" o "f". Todos los otros tipos, incluyendo los arrays, son devueltos como cadenas formateadas, de la misma manera que PostgreSQL los mostraría en el cliente `psql`. Los valores NULL de la base de datos son devueltos como NULL.

`false` es devuelto si `row` excede el número de filas en el conjunto de resultados, no hay más filas disponibles o cualquier otro error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | `row` ahora puede ser nullable. |
| 8.1.0 | El parámetro `result` ahora espera una instancia de `PgSql\Result` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_fetch_result`

```php
<?php
$db = pg_connect("dbname=users user=me");

$res = pg_query($db, "SELECT 1 UNION ALL SELECT 2");

$val = pg_fetch_result($res, 1, 0);

echo "El primer campo en la segunda fila es: ", $val, "\n";
?>

    
```

El ejemplo anterior mostrará:

    El primer campo en la segunda fila es: 2

## Véase también

`pg_query`, `pg_fetch_array`
