---
title: odbc_primarykeys
description: Lista las columnas utilizadas en una clave primaria
source_url: https://www.php.net/manual/es/function.odbc-primarykeys.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-primarykeys.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 99000
---

odbc_primarykeys

Lista las columnas utilizadas en una clave primaria

## Descripción

```php
odbc_primarykeys(Odbc\Connection $odbc, string $catalog, string $schema, string $table): Odbc\Result
```php

Devuelve un objeto resultado que puede ser utilizado para recuperar los nombres de las columnas que componen la clave primaria de una tabla.

## Parámetros

`odbc`  
El objeto de conexión ODBC, ver la documentación de la función `odbc_connect` para más detalles.

`catalog`  
El catálogo ('calificativo' en el argot ODBC 2).

`schema`  
El esquema ('propietario' en el argot ODBC 2).

`table`  

## Valores devueltos

Devuelve un objeto de resultado ODBC o `false` si ocurre un error.

El conjunto de resultados contiene las siguientes columnas:

- `TABLE_CAT`

- `TABLE_SCHEM`

- `TABLE_NAME`

- `COLUMN_NAME`

- `KEY_SEQ`

- `PK_NAME`

Los controladores pueden indicar columnas adicionales.

El conjunto de resultados está ordenado por `TABLE_CAT`, `TABLE_SCHEM`, `TABLE_NAME` y `KEY_SEQ`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `odbc` ahora espera una instancia de `Odbc\Connection` ; anteriormente, se esperaba un `resource`. |
| 8.4.0 | Esta función ahora devuelve una instancia de `Odbc\Result` ; anteriormente, se devolvía un `resource`. |

## Ejemplos

Listar las Claves primarias de una Columna

```
<?php
$conn = odbc_connect($dsn, $user, $pass);
$primarykeys = odbc_primarykeys($conn, 'TutorialDB', 'dbo', 'TEST');
while (($row = odbc_fetch_array($primarykeys))) {
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
        [KEY_SEQ] => 1
        [PK_NAME] => PK__TEST__3213E83FE141F843
    )

## Véase también

`odbc_tables`, `odbc_foreignkeys`
