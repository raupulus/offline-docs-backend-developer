---
title: Schema::getCollections
description: Devuelve todas las colecciones del esquema
source_url: https://www.php.net/manual/es/mysql-xdevapi-schema.getcollections.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/schema/getcollections.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 18f9cbcbc
order: 53920
---

Schema::getCollections

Devuelve todas las colecciones del esquema

## Descripción

```php
public mysql_xdevapi\Schema::getCollections(): array
```php

Recupera una lista de colecciones para este esquema.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un array de todas las colecciones de este esquema, donde cada elemento del array es una Collection con el nombre de la colección como clave.

## Ejemplos

Ejemplo de `mysql_xdevapi\Schema::getCollections`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");
$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();

$schema  = $session->getSchema("addressbook");
$collect = $schema->createCollection("people");
$collect->add('{"name": "Fred",  "age": 21, "job": "Construction"}')->execute();
$collect->add('{"name": "Wilma", "age": 23, "job": "Teacher"}')->execute();

$collections = $schema->getCollections();
var_dump($collections);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(1) {
      ["people"]=>
      object(mysql_xdevapi\Collection)#4 (1) {
        ["name"]=>
        string(6) "people"
      }
    }
