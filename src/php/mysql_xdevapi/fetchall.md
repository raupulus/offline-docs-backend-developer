---
title: DocResult::fetchAll
description: Devuelve todas las filas
source_url: https://www.php.net/manual/es/mysql-xdevapi-docresult.fetchall.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/docresult/fetchall.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 23c4a01e6
order: 53650
---

DocResult::fetchAll

Devuelve todas las filas

## Descripción

```php
public mysql_xdevapi\DocResult::fetchAll(): array
```php

Devuelve todas las filas de un conjunto de resultados.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un array numérico con todos los resultados de la consulta; cada resultado es un array asociativo. Un array vacío es devuelto si no hay filas presentes.

## Ejemplos

Ejemplo de `mysql_xdevapi\DocResult::fetchAll`

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

var_dump($result->fetchAll());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(2) {

      [0]=>
      array(4) {
        ["_id"]=>
        string(28) "00005b6b53610000000000000123"
        ["age"]=>
        int(42)
        ["job"]=>
        string(6) "Butler"
        ["name"]=>
        string(8) "Reginald"
      }

      [1]=>
      array(4) {
        ["_id"]=>
        string(28) "00005b6b53610000000000000122"
        ["age"]=>
        int(18)
        ["job"]=>
        string(6) "Butler"
        ["name"]=>
        string(6) "Alfred"
      }

    }
