---
title: CollectionFind::offset
description: Ignorar un número dado de elementos a devolver
source_url: https://www.php.net/manual/es/mysql-xdevapi-collectionfind.offset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collectionfind/offset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 86e6094e8
order: 53250
---

CollectionFind::offset

Ignorar un número dado de elementos a devolver

## Descripción

```php
public mysql_xdevapi\CollectionFind::offset(int $position): mysql_xdevapi\CollectionFind
```php

Ignora (desplaza) un número dado de elementos que de otro modo serían devueltos por la operación find. Utilícese con el método limit().

Definir un desplazamiento mayor que el tamaño del conjunto de resultados da un conjunto vacío.

## Parámetros

`position`  
El número de elementos a ignorar para la operación limit().

## Valores devueltos

Un objeto CollectionFind que puede ser utilizado para un tratamiento ulterior.

## Ejemplos

Ejemplo de `mysql_xdevapi\CollectionFind::offset`

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
$create
  ->add('{"name": "Reginald", "age": 42, "job": "Butler"}')
  ->execute();

// ...

$collection = $schema->getCollection("people");

$result = $collection
  ->find()
  ->sort('age asc')
  ->offset(1)
  ->limit(1)
  ->execute();

var_dump($result->fetchAll());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(1) {
      [0]=>
      array(4) {
        ["_id"]=>
        string(28) "00005b6b536100000000000000f3"
        ["age"]=>
        int(42)
        ["job"]=>
        string(6) "Butler"
        ["name"]=>
        string(8) "Reginald"
      }
    }
