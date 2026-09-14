---
title: odbc_columns
description: Lista las columnas de una tabla
source_url: https://www.php.net/manual/es/function.odbc-columns.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-columns.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 98680
---

odbc_columns

Lista las columnas de una tabla

## Descripción

```php
odbc_columns(Odbc\Connection $odbc, [string $catalog], [string $schema], [string $table], [string $column]): Odbc\Result
```php

Lista las columnas de una tabla.

## Parámetros

`odbc`  
El objeto de conexión ODBC, ver la documentación de la función `odbc_connect` para más detalles.

`catalog`  
El catálogo ('calificativo' en el argot ODBC 2).

`schema`  
El esquema ('propietario' en el argot ODBC 2). Este parámetro acepta los siguientes patrones de búsqueda: `%` para buscar cero o más caracteres, y `_` para buscar un solo carácter.

`table`  
El nombre de la tabla. Este parámetro acepta los siguientes patrones de búsqueda: `%` para buscar cero o más caracteres, y `_` para buscar un solo carácter.

`column`  
El nombre de la columna. Este parámetro acepta los siguientes patrones de búsqueda: `%` para buscar cero o más caracteres, y `_` para buscar un solo carácter.

## Valores devueltos

Devuelve un objeto de resultado ODBC o `false` si ocurre un error.

El conjunto de resultados contiene las siguientes columnas:

- `TABLE_CAT`

- `TABLE_SCHEM`

- `TABLE_NAME`

- `COLUMN_NAME`

- `DATA_TYPE`

- `TYPE_NAME`

- `COLUMN_SIZE`

- `BUFFER_LENGTH`

- `DECIMAL_DIGITS`

- `NUM_PREC_RADIX`

- `NULLABLE`

- `REMARKS`

- `COLUMN_DEF`

- `SQL_DATA_TYPE`

- `SQL_DATETIME_SUB`

- `CHAR_OCTET_LENGTH`

- `ORDINAL_POSITION`

- `IS_NULLABLE`

Los controladores pueden indicar columnas adicionales.

El conjunto de resultados está ordenado por `TABLE_CAT`, `TABLE_SCHEM`, `TABLE_NAME` y `ORDINAL_POSITION`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `odbc` ahora espera una instancia de `Odbc\Connection` ; anteriormente, se esperaba un `resource`. |
| 8.0.0 | `schema`, `table` y `column` ahora son anulables. |

## Ejemplos

Listar las Columnas de una Tabla

```
<?php
$conn = odbc_connect($dsn, $user, $pass);
$columns = odbc_columns($conn, 'TutorialDB', 'dbo', 'test', '%');
while (($row = odbc_fetch_array($columns))) {
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
        [COLUMN_NAME] => id
        [DATA_TYPE] => 4
        [TYPE_NAME] => int
        [COLUMN_SIZE] => 10
        [BUFFER_LENGTH] => 4
        [DECIMAL_DIGITS] => 0
        [NUM_PREC_RADIX] => 10
        [NULLABLE] => 0
        [REMARKS] =>
        [COLUMN_DEF] =>
        [SQL_DATA_TYPE] => 4
        [SQL_DATETIME_SUB] =>
        [CHAR_OCTET_LENGTH] =>
        [ORDINAL_POSITION] => 1
        [IS_NULLABLE] => NO
    )

## Véase también

`odbc_columnprivileges`, `odbc_procedurecolumns`
