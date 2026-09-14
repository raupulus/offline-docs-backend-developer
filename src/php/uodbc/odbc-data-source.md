---
title: odbc_data_source
description: Devuelve información sobre los DSNs disponibles
source_url: https://www.php.net/manual/es/function.odbc-data-source.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-data-source.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 98750
---

odbc_data_source

Devuelve información sobre los DSNs disponibles

## Descripción

```php
odbc_data_source(Odbc\Connection $odbc, int $fetch_type): array
```php

Devuelve una lista de DSN disponibles (tras haberla llamado varias veces).

## Parámetros

`odbc`  
El objeto de conexión ODBC, ver la documentación de la función `odbc_connect` para más detalles.

`fetch_type`  
El parámetro `fetch_type` puede ser una de las dos constantes siguientes: `SQL_FETCH_FIRST` o `SQL_FETCH_NEXT`. Utilice `SQL_FETCH_FIRST` la primera vez que se llama a la función, luego `SQL_FETCH_NEXT`.

## Valores devueltos

Devuelve `false` si ocurre un error, un `array` en caso de éxito, y `null` tras haber recuperado el último DSN disponible.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `odbc` ahora espera una instancia de `Odbc\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Listar los DSNs disponibles

```
<?php
$conn = odbc_connect('dsn', 'user', 'pass');
$dsn_info = odbc_data_source($conn, SQL_FETCH_FIRST);
while ($dsn_info) {
    print_r($dsn_info);
    $dsn_info = odbc_data_source($conn, SQL_FETCH_NEXT);
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [server] => dsn
        [description] => ODBC Driver 17 for SQL Server
    )
    Array
    (
        [server] => other_dsn
        [description] => Microsoft Access Driver (*.mdb, *.accdb)
    )
