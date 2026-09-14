---
title: Collection::getSchema
description: Devuelve el objeto esquema
source_url: https://www.php.net/manual/es/mysql-xdevapi-collection.getschema.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collection/getschema.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: '475439775'
order: 53080
---

Collection::getSchema

Devuelve el objeto esquema

## Descripción

```php
public mysql_xdevapi\Collection::getSchema(): Schema Object
```php

Devuelve el objeto esquema que contiene la colección.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El objeto esquema en caso de éxito, o `null` si el objeto no puede ser recuperado para la colección dada.

## Ejemplos

Ejemplo de `mysql_xdevapi\Collection::getSchema`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();

$schema     = $session->getSchema("addressbook");
$collection = $schema->createCollection("people");

var_dump($collection->getSchema());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(mysql_xdevapi\Schema)#9 (1) {
      ["name"]=>
      string(11) "addressbook"
    }
