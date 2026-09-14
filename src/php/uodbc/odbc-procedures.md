---
title: odbc_procedures
description: Lista los procedimientos almacenados
source_url: https://www.php.net/manual/es/function.odbc-procedures.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-procedures.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 99020
---

odbc_procedures

Lista los procedimientos almacenados

## Descripción

```php
odbc_procedures(Odbc\Connection $odbc, [string $catalog], [string $schema], [string $procedure]): Odbc\Result
```php

Lista los procedimientos almacenados.

## Parámetros

`odbc`  
El objeto de conexión ODBC, ver la documentación de la función `odbc_connect` para más detalles.

`catalog`  
El catálogo ('calificativo' en el argot ODBC 2).

`schema`  
El esquema ('propietario' en el argot ODBC 2). Este parámetro acepta los siguientes patrones de búsqueda: `%` para buscar cero o más caracteres, y `_` para buscar un solo carácter.

`procedure`  
El nombre. Este parámetro acepta los siguientes patrones de búsqueda: `%` para buscar cero o más caracteres, y `_` para buscar un solo carácter.

## Valores devueltos

Devuelve un objeto de resultado ODBC que contiene las informaciones o `false` si ocurre un error.

El conjunto de resultados contiene las columnas siguientes:

- `PROCEDURE_CAT`

- `PROCEDURE_SCHEM`

- `PROCEDURE_NAME`

- `NUM_INPUT_PARAMS`

- `NUM_OUTPUT_PARAMS`

- `NUM_RESULT_SETS`

- `REMARKS`

- `PROCEDURE_TYPE`

Los controladores pueden indicar columnas adicionales.

El conjunto de resultados está ordenado por `PROCEDURE_CAT`, `PROCEDURE_SCHEMA` y `PROCEDURE_NAME`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `odbc` ahora espera una instancia de `Odbc\Connection` ; anteriormente, se esperaba un `resource`. |
| 8.4.0 | Esta función ahora devuelve una instancia de `Odbc\Result` ; anteriormente, se devolvía un `resource`. |
| 8.0.0 | Antes de esta versión, la función solo podía ser llamada con uno o cuatro argumentos. |

## Ejemplos

Lista los procedimientos almacenados de una base de datos

```
<?php
$conn = odbc_connect($dsn, $user, $pass);
$procedures = odbc_procedures($conn, $catalog, $schema, '%');
while (($row = odbc_fetch_array($procedures))) {
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
        [NUM_INPUT_PARAMS] => -1
        [NUM_OUTPUT_PARAMS] => -1
        [NUM_RESULT_SETS] => -1
        [REMARKS] =>
        [PROCEDURE_TYPE] => 2
    )

## Véase también

`odbc_procedurecolumns`, `odbc_tables`
