---
title: Table::getSchema
description: Devuelve el esquema de la tabla
source_url: https://www.php.net/manual/es/mysql-xdevapi-table.getschema.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/table/getschema.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 18f9cbcbc
order: 54440
---

Table::getSchema

Devuelve el esquema de la tabla

## Descripción

```php
public mysql_xdevapi\Table::getSchema(): mysql_xdevapi\Schema
```php

Recupera el esquema asociado a la tabla.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un objeto Schema.

## Ejemplos

Ejemplo de `mysql_xdevapi\Table::getSchema`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();
$session->sql("CREATE TABLE addressbook.names(name text, age int)")->execute();
$session->sql("INSERT INTO addressbook.names values ('John', 42), ('Sam', 33)")->execute();

$schema = $session->getSchema("addressbook");
$table  = $schema->getTable("names");

var_dump($table->getSchema());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(mysql_xdevapi\Schema)#9 (1) {
      ["name"]=>
      string(11) "addressbook"
    }
