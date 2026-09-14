---
title: CollectionModify::limit
description: Limita el número de documentos modificados
source_url: https://www.php.net/manual/es/mysql-xdevapi-collectionmodify.limit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collectionmodify/limit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 86e6094e8
order: 53320
---

CollectionModify::limit

Limita el número de documentos modificados

## Descripción

```php
public mysql_xdevapi\CollectionModify::limit(int $rows): mysql_xdevapi\CollectionModify
```php

Limita el número de documentos modificados por esta operación. Combina eventualmente con skip() para definir un valor de desplazamiento.

## Parámetros

`rows`  
El número máximo de documentos a modificar.

## Valores devueltos

Un objeto CollectionModify.

## Ejemplos

Ejemplo de `mysql_xdevapi\CollectionModify::limit`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");
$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();

$schema     = $session->getSchema("addressbook");
$collection = $schema->createCollection("people");

$collection->add('{"name": "Fred",  "age": 21, "job": "Construction"}')->execute();
$collection->add('{"name": "Wilma", "age": 23, "job": "Teacher"}')->execute();
$collection->add('{"name": "Betty", "age": 24, "job": "Teacher"}')->execute();

$collection
  ->modify("job = :job")
  ->bind(['job' => 'Teacher'])
  ->set('job', 'Principal')
  ->limit(1)
  ->execute();

$result = $collection
  ->find()
  ->execute();

print_r($result->fetchAll());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => Array
            (
                [_id] => 00005b6b53610000000000000118
                [age] => 21
                [job] => Construction
                [name] => Fred
            )
        [1] => Array
            (
                [_id] => 00005b6b53610000000000000119
                [age] => 23
                [job] => Principal
                [name] => Wilma
            )
        [2] => Array
            (
                [_id] => 00005b6b5361000000000000011a
                [age] => 24
                [job] => Teacher
                [name] => Betty
            )
    )
