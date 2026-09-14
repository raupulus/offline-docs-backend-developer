---
title: Executable::execute
description: Ejecuta una declaración
source_url: https://www.php.net/manual/es/mysql-xdevapi-executable.execute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/executable/execute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 53690
---

Executable::execute

Ejecuta una declaración

## Descripción

```php
abstract public mysql_xdevapi\Executable::execute(): mysql_xdevapi\Result
```php

Ejecuta la declaración a partir de una operación de colección o de una consulta de tabla; esta funcionalidad permite el encadenamiento de métodos.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Uno de los objetos Result, tales como Result o SqlStatementResult.

## Ejemplos

Ejemplos de execute()

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$result_sql = $session->sql("CREATE DATABASE addressbook")->execute();

var_dump($result_sql);

$schema     = $session->getSchema("addressbook");
$collection = $schema->createCollection("humans");

$result_collection = $collection->add(
  '{"name": "Jane",
    "jobs": [{"title":"Scientist","Salary":18000}, {"title":"Mother","Salary":0}],
    "hobbies": ["Walking","Making pies"]}');

$result_collection_executed = $result_collection->execute();

var_dump($result_collection);
var_dump($result_collection_executed);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(mysql_xdevapi\SqlStatementResult)#3 (0) {
    }

    object(mysql_xdevapi\CollectionAdd)#5 (0) {
    }

    object(mysql_xdevapi\Result)#7 (0) {
    }
