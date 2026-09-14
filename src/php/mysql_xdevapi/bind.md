---
title: CollectionFind::bind
description: Liga un valor a un argumento de consulta
source_url: https://www.php.net/manual/es/mysql-xdevapi-collectionfind.bind.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collectionfind/bind.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 53160
---

CollectionFind::bind

Liga un valor a un argumento de consulta

## Descripción

```php
public mysql_xdevapi\CollectionFind::bind(array $placeholder_values): mysql_xdevapi\CollectionFind
```php

Esto permite ligar un argumento al espacio reservado en la condición de búsqueda de la operación find. El espacio reservado tiene la forma de :NOMBRE donde ':' es un prefijo común que siempre debe existir antes de cualquier NOMBRE. NOMBRE es el nombre real del espacio reservado. La función bind acepta una lista de espacios reservados si varias entidades deben ser sustituidas en la condición de búsqueda.

## Parámetros

`placeholder_values`  
Los valores a sustituir en la condición de búsqueda; se permiten varios valores y se pasan en forma de array donde "NOMBRE_ESPACIO_RESERVADO =\> VALOR_ESPACIO_RESERVADO".

## Valores devueltos

Un objeto CollectionFind, o encadenado con execute() para devolver un objeto Result.

## Ejemplos

Ejemplo de `mysql_xdevapi\CollectionFind::bind`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");
$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();

$schema = $session->getSchema("addressbook");
$create = $schema->createCollection("people");
$result = $create
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
