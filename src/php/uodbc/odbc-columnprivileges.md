---
title: odbc_columnprivileges
description: Lista las columnas y sus derechos asociados
source_url: https://www.php.net/manual/es/function.odbc-columnprivileges.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-columnprivileges.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 98670
---

odbc_columnprivileges

Lista las columnas y sus derechos asociados

## Descripción

```php
odbc_columnprivileges(Odbc\Connection $odbc, string $catalog, string $schema, string $table, string $column): Odbc\Result
```php

Lista las columnas y sus derechos asociados.

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

Devuelve un objeto de resultado ODBC o `false` si ocurre un error. Este objeto resultado puede ser utilizado para recuperar una lista de columnas y los derechos asociados.

El conjunto de resultados contiene las siguientes columnas:

- `TABLE_CAT`

- `TABLE_SCHEM`

- `TABLE_NAME`

- `COLUMN_NAME`

- `GRANTOR`

- `GRANTEE`

- `PRIVILEGE`

- `IS_GRANTABLE`

Los controladores pueden indicar columnas adicionales.

El conjunto de resultados está ordenado por `TABLE_CAT`, `TABLE_SCHEM`, `TABLE_NAME`, `COLUMN_NAME` y `PRIVILEGE`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `odbc` ahora espera una instancia de `Odbc\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Listar los Privilegios para una Columna

```
<?php
$conn = odbc_connect($dsn, $user, $pass);
$privileges = odbc_columnprivileges($conn, 'TutorialDB', 'dbo', 'test', 'id');
while (($row = odbc_fetch_array($privileges))) {
    print_r($row);
    break; // further rows omitted for brevity
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [TABLE_CAT] => TutorialDB
        [TABLE_SCHEM] => dbo
        [TABLE_NAME] => test
        [COLUMN_NAME] => id
        [GRANTOR] => dbo
        [GRANTEE] => dbo
        [PRIVILEGE] => INSERT
        [IS_GRANTABLE] => YES
    )
