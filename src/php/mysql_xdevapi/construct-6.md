---
title: CollectionRemove::__construct
description: Constructor de CollectionRemove
source_url: https://www.php.net/manual/es/mysql-xdevapi-collectionremove.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collectionremove/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: ee5228571
order: 53400
---

CollectionRemove::\_\_construct

Constructor de CollectionRemove

## Descripción

```php
private mysql_xdevapi\CollectionRemove::__construct()
```php

Elimina los documentos de la colección y es instanciado por el método mysql_xdevapi\Collection::remove.

## Parámetros

Esta función no contiene ningún parámetro.

## Ejemplos

Ejemplo de `mysql_xdevapi\Collection::remove`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();

$schema     = $session->getSchema("addressbook");
$collection = $schema->createCollection("people");

$collection->add('{"name": "Alfred", "age": 18, "job": "Butler"}')->execute();
$collection->add('{"name": "Bob",    "age": 19, "job": "Painter"}')->execute();

// Elimina todos los pintores
$collection
  ->remove("job in ('Painter')")
  ->execute();

// Elimina el mayordomo más viejo
$collection
  ->remove("job in ('Butler')")
  ->sort('age desc')
  ->limit(1)
  ->execute();

// Elimina el registro con la edad más baja
$collection
  ->remove('true')
  ->sort('age desc')
  ->limit(1)
  ->execute();
?>

   
```php
