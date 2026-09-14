---
title: Result::getGeneratedIds
description: Devuelve los ID generados
source_url: https://www.php.net/manual/es/mysql-xdevapi-result.getgeneratedids.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/result/getgeneratedids.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 286ab7c12
order: 53750
---

Result::getGeneratedIds

Devuelve los ID generados

## Descripción

```php
public mysql_xdevapi\Result::getGeneratedIds(): array
```php

Recupera los valores \_id generados por la última operación. El campo \_id único es generado por el servidor MySQL.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un array de \_id generados por la última operación, o un array vacío si no hay ninguno.

## Ejemplos

Ejemplo de `mysql_xdevapi\Result::getGeneratedIds`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");
$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();

$schema = $session->getSchema("addressbook");
$create = $schema->createCollection("people");

$collection = $schema->getCollection("people");

$result = $collection->add(
  '{"name": "Bernie",
    "jobs": [{"title":"Cat Herder","Salary":42000}, {"title":"Father","Salary":0}],
    "hobbies": ["Sports","Making cupcakes"]}',
  '{"name": "Jane",
    "jobs": [{"title":"Scientist","Salary":18000}, {"title":"Mother","Salary":0}],
    "hobbies": ["Walking","Making pies"]}')->execute();

$ids = $result->getGeneratedIds();
var_dump($ids);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(2) {
      [0]=>
      string(28) "00005b6b53610000000000000064"
      [1]=>
      string(28) "00005b6b53610000000000000065"
    }
