---
title: SQLite3::changes
description: Devuelve el número de líneas modificadas (o insertadas, borradas) por
  la última consulta SQL
source_url: https://www.php.net/manual/es/sqlite3.changes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/sqlite3/changes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: false
translation_revision: 855bfee2f
order: 85640
---

SQLite3::changes

Devuelve el número de líneas modificadas (o insertadas, borradas) por la última consulta SQL

## Descripción

```php
public SQLite3::changes(): int
```php

Devuelve el número de líneas modificadas (o insertadas, borradas) por la última consulta SQL.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `int` correspondiente al número de líneas modificadas (o insertadas, borradas) por la última consulta SQL.

## Ejemplos

Ejemplo con `SQLite3::changes`

```
<?php
$db = new SQLite3('mysqlitedb.db');

$query = $db->exec('UPDATE counter SET views=0 WHERE page="test"');
if ($query) {
    echo 'Número de líneas modificadas : ', $db->changes();
}
?>

    
```php
