---
title: Schema::getCollectionAsTable
description: Devuelve una colección como objeto Table
source_url: https://www.php.net/manual/es/mysql-xdevapi-schema.getcollectionastable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/schema/getcollectionastable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: ee5228571
order: 53910
---

Schema::getCollectionAsTable

Devuelve una colección como objeto Table

## Descripción

```php
public mysql_xdevapi\Schema::getCollectionAsTable(string $name): mysql_xdevapi\Table
```php

Devuelve una colección, pero como objeto Table en lugar de un objeto Collection.

## Parámetros

`name`  
El nombre de la colección a partir de la cual instanciar un objeto Table.

## Valores devueltos

Un objeto `mysql_xdevapi\Table` para la colección.

## Ejemplos

Ejemplo de mysql_xdevapi\Schema::getCollectionAsTable

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");
$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();

$schema  = $session->getSchema("addressbook");
$collect = $schema->createCollection("people");
$collect->add('{"name": "Fred",  "age": 21, "job": "Construction"}')->execute();
$collect->add('{"name": "Wilma", "age": 23, "job": "Teacher"}')->execute();

$table      = $schema->getCollectionAsTable("people");
$collection = $schema->getCollection("people");

var_dump($table);
var_dump($collection);

   
```php

Resultado del ejemplo anterior es similar a:

    object(mysql_xdevapi\Table)#4 (1) {
      ["name"]=>
      string(6) "people"
    }

    object(mysql_xdevapi\Collection)#5 (1) {
      ["name"]=>
      string(6) "people"
    }
