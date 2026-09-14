---
title: DocResult::__construct
description: Constructor de DocResult
source_url: https://www.php.net/manual/es/mysql-xdevapi-docresult.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/docresult/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 53640
---

DocResult::\_\_construct

Constructor de DocResult

## Descripción

```php
private mysql_xdevapi\DocResult::__construct()
```php

Recupera los resultados y las advertencias del documento, y es instanciado por CollectionFind.

## Parámetros

Esta función no contiene ningún parámetro.

## Ejemplos

Un ejemplo de DocResult

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");
$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();

$schema = $session->getSchema("addressbook");
$create = $schema->createCollection("people");

$create->add('{"name": "Alfred", "age": 18, "job": "Butler"}')->execute();
$create->add('{"name": "Reginald", "age": 42, "job": "Butler"}')->execute();

// ...

$collection = $schema->getCollection("people");

// Devuelve un objeto DocResult
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
