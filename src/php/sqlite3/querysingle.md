---
title: SQLite3::querySingle
description: Ejecuta una consulta y devuelve un único resultado
source_url: https://www.php.net/manual/es/sqlite3.querysingle.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/sqlite3/querysingle.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: true
translation_revision: 855bfee2f
order: 85810
---

SQLite3::querySingle

Ejecuta una consulta y devuelve un único resultado

## Descripción

```php
public SQLite3::querySingle(string $query, [bool $entireRow]): mixed
```php

Ejecuta una consulta y devuelve un único resultado.

## Parámetros

`query`  
La consulta SQL a ejecutar.

`entireRow`  
Por omisión, esta función devuelve el valor de la primera columna devuelta por la consulta. Si `entireRow` es `true`, entonces la función devolverá un array que contiene toda la primera fila.

## Valores devueltos

Devuelve el valor de la primera columna del resultado, o un array que contiene toda la primera fila (si el argumento `entireRow` es `true`).

Si la consulta es válida pero no devuelve ningún resultado, `null` será devuelto si `entireRow` es `false`, de lo contrario se devuelve un array vacío.

Las consultas inválidas devolverán `false`.

## Ejemplos

Ejemplo con `SQLite3::querySingle`

```
<?php
$db = new SQLite3('mysqlitedb.db');

var_dump($db->querySingle('SELECT username FROM user WHERE userid=1'));
print_r($db->querySingle('SELECT username, email FROM user WHERE userid=1', true));
?>

    
```php

Resultado del ejemplo anterior es similar a:

    string(5) "Scott"
    Array
    (
        [username] => Scott
        [email] => scott@example.com
    )
