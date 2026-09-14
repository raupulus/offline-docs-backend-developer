---
title: SQLite3::prepare
description: Prepara una consulta SQL para su ejecución
source_url: https://www.php.net/manual/es/sqlite3.prepare.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/sqlite3/prepare.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: false
translation_revision: 855bfee2f
order: 85790
---

SQLite3::prepare

Prepara una consulta SQL para su ejecución

## Descripción

```php
public SQLite3::prepare(string $query): SQLite3Stmt
```php

Prepara una consulta SQL para su ejecución y devuelve un objeto `SQLite3Stmt`.

## Parámetros

`query`  
La consulta SQL a preparar.

## Valores devueltos

Devuelve un objeto `SQLite3Stmt` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `SQLite3::prepare`

```
<?php
unlink('mysqlitedb.db');
$db = new SQLite3('mysqlitedb.db');

$db->exec('CREATE TABLE foo (id INTEGER, bar STRING)');
$db->exec("INSERT INTO foo (id, bar) VALUES (1, 'Ceci est un test')");

$stmt = $db->prepare('SELECT bar FROM foo WHERE id=:id');
$stmt->bindValue(':id', 1, SQLITE3_INTEGER);

$result = $stmt->execute();
var_dump($result->fetchArray());
?>

    
```php

## Véase también

SQLite3Stmt::paramCount

SQLite3Stmt::bindValue

SQLite3Stmt::bindParam
