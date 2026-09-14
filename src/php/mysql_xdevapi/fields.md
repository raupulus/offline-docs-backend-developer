---
title: CollectionFind::fields
description: Define el filtro de campo de documento
source_url: https://www.php.net/manual/es/mysql-xdevapi-collectionfind.fields.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collectionfind/fields.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: ee5228571
order: 53190
---

CollectionFind::fields

Define el filtro de campo de documento

## Descripción

```php
public mysql_xdevapi\CollectionFind::fields(string $projection): mysql_xdevapi\CollectionFind
```php

Define las columnas para la consulta a devolver. Si no se define, se utilizan todas las columnas.

## Parámetros

`projection`  
Puede ser una cadena única o un array de cadenas identificando las columnas a devolver para cada documento que coincida con la condición de búsqueda.

## Valores devueltos

Un objeto CollectionFind que puede ser utilizado para un procesamiento posterior.

## Ejemplos

Ejemplo de `mysql_xdevapi\CollectionFind::fields`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();

$schema = $session->getSchema("addressbook");
$create = $schema->createCollection("people");

$create
  ->add('{"name": "Alfred", "age": 18, "job": "Butler"}')
  ->execute();

// ...

$collection = $schema->getCollection("people");

$result = $collection
  ->find('job like :job and age > :age')
  ->bind(['job' => 'Butler', 'age' => 16])
  ->fields('name')
  ->execute();

var_dump($result->fetchAll());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(1) {
      [0]=>
      array(1) {
        ["name"]=>
        string(6) "Alfred"
      }
    }
