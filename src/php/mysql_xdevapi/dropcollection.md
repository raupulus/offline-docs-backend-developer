---
title: Schema::dropCollection
description: Elimina una colección del esquema
source_url: https://www.php.net/manual/es/mysql-xdevapi-schema.dropcollection.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/schema/dropcollection.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: ee5228571
order: 53880
---

Schema::dropCollection

Elimina una colección del esquema

## Descripción

```php
public mysql_xdevapi\Schema::dropCollection(string $collection_name): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`collection_name`  

## Valores devueltos

## Ejemplos

Ejemplo de mysql_xdevapi\Schema::dropCollection

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE IF EXISTS food")->execute();
$session->sql("CREATE DATABASE food")->execute();
$session->sql("CREATE TABLE food.fruit(name text, rating text)")->execute();

$schema = $session->getSchema("food");

$schema->createCollection("trees");
$schema->dropCollection("trees");
$schema->createCollection("buildings");

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
        [buildings] => mysql_xdevapi\Collection Object
            (
                [name] => buildings
            )
    )
