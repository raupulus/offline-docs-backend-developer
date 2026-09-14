---
title: odbc_procedurecolumns
description: Lista los parámetros de los procedimientos
source_url: https://www.php.net/manual/es/function.odbc-procedurecolumns.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-procedurecolumns.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 99010
---

odbc_procedurecolumns

Lista los parámetros de los procedimientos

## Descripción

```php
odbc_procedurecolumns(Odbc\Connection $odbc, [string $catalog], [string $schema], [string $procedure], [string $column]): Odbc\Result
```php

Lista los parámetros de los procedimientos.

## Parámetros

`odbc`  
El objeto de conexión ODBC, ver la documentación de la función `odbc_connect` para más detalles.

`catalog`  
El catálogo ('calificativo' en el argot ODBC 2).

`schema`  
El esquema ('propietario' en el argot ODBC 2). Este parámetro acepta los siguientes patrones de búsqueda: `%` para buscar cero o más caracteres, y `_` para buscar un solo carácter.

`procedure`  
El procedimiento. Este parámetro acepta los siguientes patrones de búsqueda: `%` para buscar cero o más caracteres, y `_` para buscar un solo carácter.

`column`  
La columna. Este parámetro acepta los siguientes patrones de búsqueda: `%` para buscar cero o más caracteres, y `_` para buscar un solo carácter.

## Valores devueltos

Devuelve los parámetros de entrada y salida, así como las columnas utilizadas en los procedimientos designados por los argumentos. Devuelve un objeto de resultado ODBC o `false` si ocurre un error.

El conjunto de resultados contiene las siguientes columnas:

- `PROCEDURE_CAT`

- `PROCEDURE_SCHEM`

- `PROCEDURE_NAME`

- `COLUMN_NAME`

- `COLUMN_TYPE`

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

El conjunto de resultados está ordenado por `PROCEDURE_CAT`, `PROCEDURE_SCHEM`, `PROCEDURE_NAME` y `COLUMN_TYPE`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `odbc` ahora espera una instancia de `Odbc\Connection` ; anteriormente, se esperaba un `resource`. |
| 8.4.0 | Esta función ahora devuelve una instancia de `Odbc\Result` ; anteriormente, se devolvía un `resource`. |
| 8.0.0 | Antes de esta versión, la función solo podía ser llamada con uno o cinco argumentos. |

## Ejemplos

Lista las columnas de un procedimiento almacenado

```
<?php
$conn = odbc_connect($dsn, $user, $pass);
$columns = odbc_procedurecolumns($conn, 'TutorialDB', 'dbo', 'GetEmployeeSalesYTD;1', '%');
while (($row = odbc_fetch_array($columns))) {
    print_r($row);
    break; // filas adicionales omitidas por brevedad
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [PROCEDURE_CAT] => TutorialDB
        [PROCEDURE_SCHEM] => dbo
        [PROCEDURE_NAME] => GetEmployeeSalesYTD;1
        [COLUMN_NAME] => @SalesPerson
        [COLUMN_TYPE] => 1
        [DATA_TYPE] => -9
        [TYPE_NAME] => nvarchar
        [COLUMN_SIZE] => 50
        [BUFFER_LENGTH] => 100
        [DECIMAL_DIGITS] =>
        [NUM_PREC_RADIX] =>
        [NULLABLE] => 1
        [REMARKS] =>
        [COLUMN_DEF] =>
        [SQL_DATA_TYPE] => -9
        [SQL_DATETIME_SUB] =>
        [CHAR_OCTET_LENGTH] => 100
        [ORDINAL_POSITION] => 1
        [IS_NULLABLE] => YES
    )

## Véase también

`odbc_columns`
