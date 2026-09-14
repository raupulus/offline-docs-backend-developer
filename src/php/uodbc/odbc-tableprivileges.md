---
title: odbc_tableprivileges
description: Lista las tablas y sus privilegios
source_url: https://www.php.net/manual/es/function.odbc-tableprivileges.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-tableprivileges.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 99090
---

odbc_tableprivileges

Lista las tablas y sus privilegios

## Descripción

```php
odbc_tableprivileges(Odbc\Connection $odbc, string $catalog, string $schema, string $table): Odbc\Result
```php

Lista las tablas y sus privilegios.

## Parámetros

`odbc`  
El objeto de conexión ODBC, ver la documentación de la función `odbc_connect` para más detalles.

`catalog`  
El catálogo ('calificativo' en el argot ODBC 2).

`schema`  
El esquema ('propietario' en el argot ODBC 2). Este parámetro acepta los siguientes patrones de búsqueda: `%` para buscar cero o más caracteres, y `_` para buscar un solo carácter.

`table`  
El nombre. Este parámetro acepta los siguientes patrones de búsqueda: `%` para buscar cero o más caracteres, y `_` para buscar un solo carácter.

## Valores devueltos

Devuelve un objeto de resultado ODBC o `false` si ocurre un error.

El conjunto de resultados contiene las siguientes columnas:

- `TABLE_CAT`

- `TABLE_SCHEM`

- `TABLE_NAME`

- `GRANTOR`

- `GRANTEE`

- `PRIVILEGE`

- `IS_GRANTABLE`

Los controladores pueden indicar columnas adicionales.

El conjunto de resultados está ordenado por `TABLE_CAT`, `TABLE_SCHEM`, `TABLE_NAME`, `PRIVILEGE` y `GRANTEE`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `odbc` ahora espera una instancia de `Odbc\Connection` ; anteriormente, se esperaba un `resource`. |
| 8.4.0 | Esta función ahora devuelve una instancia de `Odbc\Result` ; anteriormente, se devolvía un `resource`. |

## Ejemplos

Lista los Privilegios de una Tabla

```
<?php
$conn = odbc_connect($dsn, $user, $pass);
$privileges = odbc_tableprivileges($conn, 'SalesOrders', 'dbo', 'Orders');
while (($row = odbc_fetch_array($privileges))) {
    print_r($row);
    break; // se omiten filas adicionales por brevedad
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [TABLE_CAT] => SalesOrders
        [TABLE_SCHEM] => dbo
        [TABLE_NAME] => Orders
        [GRANTOR] => dbo
        [GRANTEE] => dbo
        [PRIVILEGE] => DELETE
        [IS_GRANTABLE] => YES
    )

## Véase también

`odbc_tables`
