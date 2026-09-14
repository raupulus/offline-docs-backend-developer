---
title: odbc_statistics
description: Cálculo de estadísticas sobre una tabla
source_url: https://www.php.net/manual/es/function.odbc-statistics.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-statistics.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 99080
---

odbc_statistics

Cálculo de estadísticas sobre una tabla

## Descripción

```php
odbc_statistics(Odbc\Connection $odbc, string $catalog, string $schema, string $table, int $unique, int $accuracy): Odbc\Result
```php

Cálculo de estadísticas sobre una tabla.

## Parámetros

`odbc`  
El objeto de conexión ODBC, ver la documentación de la función `odbc_connect` para más detalles.

`catalog`  
El catálogo ('calificativo' en el argot ODBC 2).

`schema`  
El esquema ('propietario' en el argot ODBC 2).

`table`  
El nombre de la tabla.

`unique`  
El tipo del índice. Uno de `SQL_INDEX_UNIQUE` o `SQL_INDEX_ALL`.

`accuracy`  
Uno de `SQL_ENSURE` o `SQL_QUICK`. Este último solicita al controlador que recupere `CARDINALITY` y `PAGES` solo si están inmediatamente disponibles desde el servidor.

## Valores devueltos

Devuelve un objeto de resultado ODBC o `false` si ocurre un error.

El conjunto de resultados contiene las siguientes columnas:

- `TABLE_CAT`

- `TABLE_SCHEM`

- `TABLE_NAME`

- `NON_UNIQUE`

- `INDEX_QUALIFIER`

- `INDEX_NAME`

- `TYPE`

- `ORDINAL_POSITION`

- `COLUMN_NAME`

- `ASC_OR_DESC`

- `CARDINALITY`

- `PAGES`

- `FILTER_CONDITION`

Los controladores pueden indicar columnas adicionales.

El conjunto de resultados está ordenado por `NON_UNIQUE`, `TYPE`, `INDEX_QUALIFIER`, `INDEX_NAME` y `ORDINAL_POSITION`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `odbc` ahora espera una instancia de `Odbc\Connection` ; anteriormente, se esperaba un `resource`. |
| 8.4.0 | Esta función ahora devuelve una instancia de `Odbc\Result` ; anteriormente, se devolvía un `resource`. |

## Ejemplos

Lista las estadísticas de una tabla

```
<?php
$conn = odbc_connect($dsn, $user, $pass);
$statistics = odbc_statistics($conn, 'TutorialDB', 'dbo', 'TEST', SQL_INDEX_UNIQUE, SQL_QUICK);
while (($row = odbc_fetch_array($statistics))) {
    print_r($row);
    break; // filas adicionales omitidas por brevedad
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [TABLE_CAT] => TutorialDB
        [TABLE_SCHEM] => dbo
        [TABLE_NAME] => TEST
        [NON_UNIQUE] =>
        [INDEX_QUALIFIER] =>
        [INDEX_NAME] =>
        [TYPE] => 0
        [ORDINAL_POSITION] =>
        [COLUMN_NAME] =>
        [ASC_OR_DESC] =>
        [CARDINALITY] => 15
        [PAGES] => 3
        [FILTER_CONDITION] =>
    )

## Véase también

`odbc_tables`
