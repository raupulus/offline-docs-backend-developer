---
title: CollectionModify::__construct
description: Constructor de CollectionModify
source_url: https://www.php.net/manual/es/mysql-xdevapi-collectionmodify.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collectionmodify/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: ee5228571
order: 53300
---

CollectionModify::\_\_construct

Constructor de CollectionModify

## Descripción

```php
private mysql_xdevapi\CollectionModify::__construct()
```php

Modifica (actualiza) una colección y es instanciado por el método mysql_xdevapi\Collection::modify.

## Parámetros

Esta función no contiene ningún parámetro.

## Ejemplos

Ejemplo de `mysql_xdevapi\CollectionModify::__construct`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");
$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();

$schema     = $session->getSchema("addressbook");
$collection = $schema->createCollection("people");

$result = $collection
  ->add(
  '{"name":   "Bernie",
    "traits": ["Friend", "Brother", "Human"]}')
  ->execute();

$collection
  ->modify("name in ('Bernie', 'Jane')")
  ->arrayAppend('traits', 'Happy')
  ->execute();

$result = $collection
  ->find()
  ->execute();

print_r($result->fetchAll());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => Array
            (
                [_id] => 00005b6b5361000000000000010c
                [name] => Bernie
                [traits] => Array
                    (
                        [0] => Friend
                        [1] => Brother
                        [2] => Human
                        [3] => Happy
                    )
            )
    )
