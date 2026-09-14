---
title: Collection::__construct
description: Constructor de Collection
source_url: https://www.php.net/manual/es/mysql-xdevapi-collection.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collection/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 53000
---

Collection::\_\_construct

Constructor de Collection

## Descripción

```php
private mysql_xdevapi\Collection::__construct()
```php

Construye un objeto Collection.

## Parámetros

Esta función no contiene ningún parámetro.

## Ejemplos

Ejemplo de `mysql_xdevapi\Collection::getOne`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();

$schema     = $session->getSchema("addressbook");
$collection = $schema->createCollection("people");

$result = $collection->add('{"name": "Alfred", "age": 42, "job": "Butler"}')->execute();

// Un identificador único _id es generado por MySQL Server
// Esto recupera los _id generados; uno solo en este ejemplo, por lo tanto $ids[0]
$ids        = $result->getGeneratedIds();
$alfreds_id = $ids[0];

// ...

print_r($alfreds_id);
print_r($collection->getOne($alfreds_id));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    00005b6b536100000000000000b1

    Array
    (
        [_id] => 00005b6b536100000000000000b1
        [age] => 42
        [job] => Butler
        [name] => Alfred
    )
