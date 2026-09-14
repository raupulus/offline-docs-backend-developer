---
title: SQLite3::close
description: Cierra la conexión con la base de datos
source_url: https://www.php.net/manual/es/sqlite3.close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/sqlite3/close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: false
translation_revision: 855bfee2f
order: 85650
---

SQLite3::close

Cierra la conexión con la base de datos

## Descripción

```php
public SQLite3::close(): bool
```php

Cierra la conexión con la base de datos.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `SQLite3::close`

```
<?php
$db = new SQLite3('mysqlitedb.db');
$db->close();
?>

    
```php
