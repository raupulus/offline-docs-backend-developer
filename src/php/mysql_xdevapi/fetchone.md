---
title: DocResult::fetchOne
description: Devuelve una fila
source_url: https://www.php.net/manual/es/mysql-xdevapi-docresult.fetchone.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/docresult/fetchone.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: '475439775'
order: 53660
---

DocResult::fetchOne

Devuelve una fila

## Descripción

```php
public mysql_xdevapi\DocResult::fetchOne(): array
```php

Recupera un resultado de un conjunto de resultados.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El resultado, en forma de array asociativo o `null` si no hay resultado presente.

## Ejemplos

Ejemplo de `mysql_xdevapi\DocResult::fetchOne`

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
  ->execute();

var_dump($result->fetchOne());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(4) {
      ["_id"]=>
      string(28) "00005b6b53610000000000000125"
      ["age"]=>
      int(42)
      ["job"]=>
      string(6) "Butler"
      ["name"]=>
      string(8) "Reginald"
    }
