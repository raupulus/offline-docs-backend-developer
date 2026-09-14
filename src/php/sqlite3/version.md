---
title: SQLite3::version
description: Devuelve la versión de la biblioteca SQLite3
source_url: https://www.php.net/manual/es/sqlite3.version.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/sqlite3/version.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: false
translation_revision: 855bfee2f
order: 85830
---

SQLite3::version

Devuelve la versión de la biblioteca SQLite3

## Descripción

```php
public static SQLite3::version(): array
```php

Devuelve la versión de la biblioteca SQLite3.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array asociativo que contiene las claves "versionString" y "versionNumber".

## Ejemplos

Ejemplo con `SQLite3::version`

```
<?php
print_r(SQLite3::version());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [versionString] => 3.5.9
        [versionNumber] => 3005009
    )
