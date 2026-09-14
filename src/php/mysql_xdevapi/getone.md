---
title: Collection::getOne
description: Devuelve un documento
source_url: https://www.php.net/manual/es/mysql-xdevapi-collection.getone.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collection/getone.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: '475439775'
order: 53070
---

Collection::getOne

Devuelve un documento

## Descripción

```php
public mysql_xdevapi\Collection::getOne(string $id): Document
```php

Recupera un documento de la colección.

Esto es un atajo para: `Collection.find("_id = :id").bind("id", id).execute().fetchOne();`

## Parámetros

`id`  
El \_id del documento en la colección.

## Valores devueltos

El objeto colección, o `null` si el \_id no corresponde a un documento.

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

// Un identificador único _id (por omisión, y recomendado) es generado por MySQL Server
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
