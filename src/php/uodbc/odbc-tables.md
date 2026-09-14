---
title: odbc_tables
description: Lista las tablas de una fuente
source_url: https://www.php.net/manual/es/function.odbc-tables.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-tables.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 99100
---

odbc_tables

Lista las tablas de una fuente

## Descripción

```php
odbc_tables(Odbc\Connection $odbc, [string $catalog], [string $schema], [string $table], [string $types]): Odbc\Result
```php

Lista las tablas de una fuente.

Para soportar las enumeraciones de calificadores propietarios y tipos de tabla, la siguiente semántica para los parámetros `catalog`, `schema`, `table` y `table_type` está disponible:

- Si `catalog` es un signo de porcentaje (%), y `schema` y `table` son strings vacíos, entonces el resultado contiene la lista de calificadores válidos para la fuente (todas las columnas excepto TABLE_QUALIFIER contienen NULL).

- Si `schema` es un signo de porcentaje (%), y `catalog` y `table` son strings vacíos, entonces el resultado contiene la lista de propietarios de la fuente (todas las columnas excepto TABLE_OWNER contienen NULL).

- Si `table_type` es un signo de porcentaje (%), y `catalog`, `schema` y `table` son strings vacíos, entonces el resultado contiene la lista de tipos de tablas de la fuente (todas las columnas excepto TABLE_TYPE contienen NULL).

## Parámetros

`odbc`  
El objeto de conexión ODBC, ver la documentación de la función `odbc_connect` para más detalles.

`catalog`  
El catálogo ('calificativo' en el argot ODBC 2).

`schema`  
El esquema ('propietario' en el argot ODBC 2). Este parámetro acepta los siguientes patrones de búsqueda: `%` para buscar cero o más caracteres, y `_` para buscar un solo carácter.

`table`  
El nombre. Este parámetro acepta los siguientes patrones de búsqueda: `%` para buscar cero o más caracteres, y `_` para buscar un solo carácter.

`types`  
Si `table_type` no es un string vacío, debe contener una lista de valores, separados por comas, que representan los tipos buscados. Cada valor puede estar entre comillas simples (`'`), o sin comillas. Por ejemplo, `'TABLE','VIEW'` o `TABLE, VIEW`. Si la fuente de datos no soporta un tipo de tabla dado, `odbc_tables` no devolverá ningún resultado para ese tipo.

## Valores devueltos

Devuelve un objeto de resultado ODBC que contiene las informaciones o `false` si ocurre un error.

El conjunto de resultados contiene las siguientes columnas:

- `TABLE_CAT`

- `TABLE_SCHEM`

- `TABLE_NAME`

- `TABLE_TYPE`

- `REMARKS`

Los controladores pueden indicar columnas adicionales.

El conjunto de resultados está ordenado por `TABLE_TYPE`, `TABLE_CAT`, `TABLE_SCHEM` y `TABLE_NAME`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `odbc` ahora espera una instancia de `Odbc\Connection` ; anteriormente, se esperaba un `resource`. |
| 8.4.0 | Esta función ahora devuelve una instancia de `Odbc\Result` ; anteriormente, se devolvía un `resource`. |
| 8.0.0 | `schema`, `table` y `types` ahora son anulables. |

## Ejemplos

Lista las Tablas en un Catálogo

```
<?php
$conn = odbc_connect($dsn, $user, $pass);
$tables = odbc_tables($conn, 'SalesOrders', 'dbo', '%', 'TABLE');
while (($row = odbc_fetch_array($tables))) {
    print_r($row);
    break; // filas adicionales omitidas por brevedad
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [TABLE_CAT] => SalesOrders
        [TABLE_SCHEM] => dbo
        [TABLE_NAME] => Orders
        [TABLE_TYPE] => TABLE
        [REMARKS] =>
    )

## Véase también

`odbc_tableprivileges`, `odbc_columns`, `odbc_specialcolumns`, `odbc_statistics`, `odbc_procedures`
