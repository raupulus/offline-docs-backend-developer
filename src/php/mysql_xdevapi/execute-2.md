---
title: CollectionFind::execute
description: Ejecuta la declaración
source_url: https://www.php.net/manual/es/mysql-xdevapi-collectionfind.execute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collectionfind/execute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: ee5228571
order: 53180
---

CollectionFind::execute

Ejecuta la declaración

## Descripción

```php
public mysql_xdevapi\CollectionFind::execute(): mysql_xdevapi\DocResult
```php

Ejecuta la operación de búsqueda; esta funcionalidad permite el encadenamiento de métodos.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un objeto `mysql_xdevapi\DocResult`, que puede ser utilizado para recuperar los resultados, o para interrogar el estado de la operación.

## Ejemplos

Ejemplo de CollectionFind

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
  ->execute();

var_dump($result->fetchAll());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(1) {
      [0]=>
      array(4) {
        ["_id"]=>
        string(28) "00005b6b536100000000000000cf"
        ["age"]=>
        int(18)
        ["job"]=>
        string(6) "Butler"
        ["name"]=>
        string(6) "Alfred"
      }
    }
