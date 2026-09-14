---
title: SQLite3::exec
description: Ejecuta una consulta en una base de datos
source_url: https://www.php.net/manual/es/sqlite3.exec.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/sqlite3/exec.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: false
translation_revision: 855bfee2f
order: 85720
---

SQLite3::exec

Ejecuta una consulta en una base de datos

## Descripción

```php
public SQLite3::exec(string $query): bool
```php

Ejecuta una consulta en una base de datos.

> [!NOTE]
> SQLite3 puede necesitar crear [archivos temporales](https://sqlite.org/tempfiles.html) durante la ejecución de consultas, por lo que los directorios respectivos deben ser escribibles.

## Parámetros

`query`  
La consulta SQL a ejecutar (típicamente, una consulta de tipo INSERT, UPDATE o DELETE).

## Valores devueltos

Devuelve `true` si la consulta se ejecutó con éxito, `false` si ocurre un error.

## Ejemplos

Ejemplo con `SQLite3::exec`

```
<?php
$db = new SQLite3('mysqlitedb.db');

$db->exec('CREATE TABLE bar (bar TEXT)');
?>

    
```php
