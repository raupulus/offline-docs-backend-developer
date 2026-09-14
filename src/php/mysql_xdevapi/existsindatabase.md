---
title: Collection::existsInDatabase
description: Verifica si la colección existe en la base de datos
source_url: https://www.php.net/manual/es/mysql-xdevapi-collection.existsindatabase.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collection/existsindatabase.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 22c3c1120
order: 53040
---

Collection::existsInDatabase

Verifica si la colección existe en la base de datos

## Descripción

```php
public mysql_xdevapi\Collection::existsInDatabase(): bool
```php

Verifica si el objeto Collection hace referencia a una colección en la base de datos (esquema).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si la colección existe en la base de datos, de lo contrario `false` si no existe.

Una tabla definida con dos columnas (doc y \_id) se considera una colección, y una tercera columna \_json_schema a partir de MySQL 8.0.21. Añadir una columna adicional significa que existsInDatabase() ya no la verá como una colección.

## Ejemplos

Ejemplo de `mysql_xdevapi\Collection::existsInDatabase`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");
$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();

$schema = $session->getSchema("addressbook");
$create = $schema->createCollection("people");

// ...

$collection = $schema->getCollection("people");

// ...

if (!$collection->existsInDatabase()) {
    echo "La colección ya no existe en la base de datos llamada addressbook. ¿Qué pasó?";
}
?>

   
```php
