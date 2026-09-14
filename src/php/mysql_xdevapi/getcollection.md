---
title: Schema::getCollection
description: Devuelve una colección del esquema
source_url: https://www.php.net/manual/es/mysql-xdevapi-schema.getcollection.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/schema/getcollection.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: ee5228571
order: 53900
---

Schema::getCollection

Devuelve una colección del esquema

## Descripción

```php
public mysql_xdevapi\Schema::getCollection(string $name): mysql_xdevapi\Collection
```php

Devuelve una colección del esquema.

## Parámetros

`name`  
El nombre de la colección a recuperar.

## Valores devueltos

El objeto Collection para la colección seleccionada.

## Ejemplos

Ejemplo de mysql_xdevapi\Schema::getCollection

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE IF EXISTS food")->execute();
$session->sql("CREATE DATABASE food")->execute();

$schema = $session->getSchema("food");
$schema->createCollection("trees");

// ...

$trees = $schema->getCollection("trees");

var_dump($trees);

   
```php

Resultado del ejemplo anterior es similar a:

    object(mysql_xdevapi\Collection)#3 (1) {
      ["name"]=>
      string(5) "trees"
    }
