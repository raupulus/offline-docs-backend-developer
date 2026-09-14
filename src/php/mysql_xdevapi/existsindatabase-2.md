---
title: DatabaseObject::existsInDatabase
description: Verifica si el objeto existe en la base de datos
source_url: https://www.php.net/manual/es/mysql-xdevapi-databaseobject.existsindatabase.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/databaseobject/existsindatabase.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 18f9cbcbc
order: 53610
---

DatabaseObject::existsInDatabase

Verifica si el objeto existe en la base de datos

## Descripción

```php
abstract public mysql_xdevapi\DatabaseObject::existsInDatabase(): bool
```php

Verifica si el objeto de base de datos hace referencia a un objeto que existe en la base de datos.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si el objeto existe en la base de datos, de lo contrario `false` si no existe.

## Ejemplos

Ejemplo de `mysql_xdevapi\DatabaseObject::existsInDatabase`

```
<?php

$existInDb = $dbObj->existsInDatabase();

?>

   
```php
