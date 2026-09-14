---
title: Collection::count
description: Devuelve el número de documentos
source_url: https://www.php.net/manual/es/mysql-xdevapi-collection.count.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collection/count.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 86e6094e8
order: 53010
---

Collection::count

Devuelve el número de documentos

## Descripción

```php
public mysql_xdevapi\Collection::count(): int
```php

Esta funcionalidad es similar a una operación SQL `SELECT COUNT(*)` en el servidor MySQL para el esquema y la colección actuales. En otras palabras, cuenta el número de documentos en la colección.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El número de documentos en la colección.

## Ejemplos

Ejemplo de `mysql_xdevapi\Collection::count`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");
$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();

$schema = $session->getSchema("addressbook");
$create = $schema->createCollection("people");

$collection = $schema->getCollection("people");

$result = $collection
  ->add(
  '{"name": "Bernie",
    "jobs": [
      {"title":"Cat Herder","Salary":42000},
      {"title":"Father","Salary":0}
    ],
    "hobbies": ["Sports","Making cupcakes"]}',
  '{"name": "Jane",
    "jobs": [
      {"title":"Scientist","Salary":18000},
      {"title":"Mother","Salary":0}
    ],
    "hobbies": ["Walking","Making pies"]}')
  ->execute();

var_dump($collection->count());
?>

   
```php

El ejemplo anterior mostrará:

    int(2)
