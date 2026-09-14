---
title: Schema::__construct
description: Constructor de schema
source_url: https://www.php.net/manual/es/mysql-xdevapi-schema.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/schema/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: ee5228571
order: 53860
---

Schema::\_\_construct

Constructor de schema

## Descripción

```php
private mysql_xdevapi\Schema::__construct()
```php

El objeto Schema proporciona acceso completo al esquema (base de datos).

## Parámetros

Esta función no contiene ningún parámetro.

## Ejemplos

Ejemplo de mysql_xdevapi\Schema::\_\_construct

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE IF EXISTS food")->execute();
$session->sql("CREATE DATABASE food")->execute();
$session->sql("CREATE TABLE food.fruit(name text, rating text)")->execute();

$schema = $session->getSchema("food");
$schema->createCollection("trees");

print_r($schema->gettables());
print_r($schema->getcollections());

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [fruit] => mysql_xdevapi\Table Object
            (
                [name] => fruit
            )
    )
    Array
    (
        [trees] => mysql_xdevapi\Collection Object
            (
                [name] => trees
            )
    )
