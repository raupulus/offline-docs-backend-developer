---
title: CollectionFind::sort
description: Define los criterios de ordenación
source_url: https://www.php.net/manual/es/mysql-xdevapi-collectionfind.sort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collectionfind/sort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 53260
---

CollectionFind::sort

Define los criterios de ordenación

## Descripción

```php
public mysql_xdevapi\CollectionFind::sort(string $sort_expr): mysql_xdevapi\CollectionFind
```php

Ordena el conjunto de resultados por el campo seleccionado en el argumento sort_expr. Los órdenes permitidos son ASC (Ascendente) o DESC (Descendente). Esta operación es equivalente a la operación 'ORDER BY' SQL y sigue el mismo conjunto de reglas.

## Parámetros

`sort_expr`  
Una o más expresiones de ordenación pueden ser proporcionadas. La evaluación se realiza de izquierda a derecha, y cada expresión está separada por una coma.

## Valores devueltos

Un objeto CollectionFind que puede ser utilizado para ejecutar el comando, o para añadir operaciones adicionales.

## Ejemplos

Ejemplo de `mysql_xdevapi\CollectionFind::sort`

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
  ->sort('job desc', 'age asc')
  ->execute();

var_dump($result->fetchAll());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(2) {
      [0]=>
      array(4) {
        ["_id"]=>
        string(28) "00005b6b53610000000000000106"
        ["age"]=>
        int(18)
        ["job"]=>
        string(6) "Butler"
        ["name"]=>
        string(6) "Alfred"
      }
      [1]=>
      array(4) {
        ["_id"]=>
        string(28) "00005b6b53610000000000000107"
        ["age"]=>
        int(42)
        ["job"]=>
        string(6) "Butler"
        ["name"]=>
        string(8) "Reginald"
      }
    }
