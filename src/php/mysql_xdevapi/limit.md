---
title: CollectionFind::limit
description: Limita el número de documentos devueltos
source_url: https://www.php.net/manual/es/mysql-xdevapi-collectionfind.limit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collectionfind/limit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 86e6094e8
order: 53220
---

CollectionFind::limit

Limita el número de documentos devueltos

## Descripción

```php
public mysql_xdevapi\CollectionFind::limit(int $rows): mysql_xdevapi\CollectionFind
```php

Define el número máximo de documentos a devolver.

## Parámetros

`rows`  
El número máximo de documentos.

## Valores devueltos

Un objeto mysql_xdevapi\CollectionFind que puede ser utilizado para un procesamiento posterior; encadene con el método execute() para devolver un objeto DocResult.

## Ejemplos

Ejemplo de `mysql_xdevapi\CollectionFind::limit`

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
  ->find('job like :job and age > :age')
  ->bind(['job' => 'Butler', 'age' => 16])
  ->sort('age desc')
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
