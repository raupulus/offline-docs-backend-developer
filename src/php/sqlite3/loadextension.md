---
title: SQLite3::loadExtension
description: Intenta cargar una extensión de la biblioteca SQLite
source_url: https://www.php.net/manual/es/sqlite3.loadextension.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/sqlite3/loadextension.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: false
translation_revision: 855bfee2f
order: 85760
---

SQLite3::loadExtension

Intenta cargar una extensión de la biblioteca SQLite

## Descripción

```php
public SQLite3::loadExtension(string $name): bool
```php

Intenta cargar una extensión de la biblioteca SQLite.

## Parámetros

`name`  
El nombre de la extensión a cargar. La extensión debe encontrarse en el directorio especificado por la opción de configuración sqlite3.extension_dir.

## Valores devueltos

Devuelve `true` si la extensión se cargó con éxito, `false` si ocurre un error.

## Ejemplos

Ejemplo con `SQLite3::loadExtension`

```
<?php
$db = new SQLite3('mysqlitedb.db');
$db->loadExtension('libagg.so');
?>

    
```php
