---
title: Schema::existsInDatabase
description: Verifica si el objeto existe en la base de datos
source_url: https://www.php.net/manual/es/mysql-xdevapi-schema.existsindatabase.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/schema/existsindatabase.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: ee5228571
order: 53890
---

Schema::existsInDatabase

Verifica si el objeto existe en la base de datos

## Descripción

```php
public mysql_xdevapi\Schema::existsInDatabase(): bool
```php

Verifica si el objeto actual (esquema, tabla, colección o vista) existe en el objeto esquema.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`true` si el esquema, la tabla, la colección o la vista aún existe en el esquema, de lo contrario `false`.

## Ejemplos

Ejemplo de mysql_xdevapi\Schema::existsInDatabase

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE IF EXISTS food")->execute();
$session->sql("CREATE DATABASE food")->execute();
$session->sql("CREATE TABLE food.fruit(name text, rating text)")->execute();

$schema = $session->getSchema("food");
$schema->createCollection("trees");

// ...

$trees = $schema->getCollection("trees");

// ...

// ¿Esta colección aún está en la base de datos (esquema)?
if ($trees->existsInDatabase()) {
    echo "Yes, the 'trees' collection is still present.";
}

   
```php

Resultado del ejemplo anterior es similar a:

    Yes, the 'trees' collection is still present.
