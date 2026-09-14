---
title: SQLite3::query
description: Ejecuta una consulta SQL
source_url: https://www.php.net/manual/es/sqlite3.query.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/sqlite3/query.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: false
translation_revision: 855bfee2f
order: 85800
---

SQLite3::query

Ejecuta una consulta SQL

## Descripción

```php
public SQLite3::query(string $query): SQLite3Result
```php

Ejecuta una consulta SQL y devuelve un objeto `SQLite3Result`. Si la consulta no genera resultados (como las instrucciones DML), el objeto `SQLite3Result` devuelto no es realmente utilizable. Utilice sqlite3::exec para estas consultas en su lugar.

## Parámetros

`query`  
La consulta SQL a ejecutar.

## Valores devueltos

Devuelve un objeto `SQLite3Result`, o `false` si ocurre un error

## Ejemplos

Ejemplo con `SQLite3::query`

```
<?php
$db = new SQLite3('mysqlitedb.db');

$results = $db->query('SELECT bar FROM foo');
while ($row = $results->fetchArray()) {
    var_dump($row);
}
?>

    
```php
