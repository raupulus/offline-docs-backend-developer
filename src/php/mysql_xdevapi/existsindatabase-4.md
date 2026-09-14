---
title: Table::existsInDatabase
description: Verifica si la tabla existe en la base de datos
source_url: https://www.php.net/manual/es/mysql-xdevapi-table.existsindatabase.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/table/existsindatabase.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 18f9cbcbc
order: 54420
---

Table::existsInDatabase

Verifica si la tabla existe en la base de datos

## Descripción

```php
public mysql_xdevapi\Table::existsInDatabase(): bool
```php

Verifica si esta tabla existe en la base de datos.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si la tabla existe en la base de datos, de lo contrario `false` si no existe.

## Ejemplos

Ejemplo de `mysql_xdevapi\Table::existsInDatabase`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();
$session->sql("CREATE TABLE addressbook.names(name text, age int)")->execute();
$session->sql("INSERT INTO addressbook.names values ('John', 42), ('Sam', 33)")->execute();

$schema = $session->getSchema("addressbook");
$table  = $schema->getTable("names");

if ($table->existsInDatabase()) {
  echo "Yes, this table still exists in the session's schema.";
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Yes, this table still exists in the session's schema.
