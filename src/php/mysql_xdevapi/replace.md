---
title: CollectionModify::replace
description: Reemplaza un campo de documento
source_url: https://www.php.net/manual/es/mysql-xdevapi-collectionmodify.replace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collectionmodify/replace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 18f9cbcbc
order: 53340
---

CollectionModify::replace

Reemplaza un campo de documento

## Descripción

```php
public mysql_xdevapi\CollectionModify::replace(string $collection_field, string $expression_or_literal): mysql_xdevapi\CollectionModify
```php

Reemplaza (actualiza) un valor de campo dado por uno nuevo.

## Parámetros

`collection_field`  
La ruta de acceso del documento del elemento a definir.

`expression_or_literal`  
El valor a definir en el atributo especificado.

## Valores devueltos

Un objeto CollectionModify.

## Ejemplos

Ejemplo de `mysql_xdevapi\CollectionModify::replace`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");
$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();

$schema     = $session->getSchema("addressbook");
$collection = $schema->createCollection("people");

$result = $collection
  ->add(
  '{"name":   "Bernie",
    "traits": ["Friend", "Brother", "Human"]}')
  ->execute();

$collection
  ->modify("name = :name")
  ->bind(['name' => 'Bernie'])
  ->replace("name", "Bern")
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
                [_id] => 00005b6b5361000000000000011b
                [name] => Bern
                [traits] => Array
                    (
                        [0] => Friend
                        [1] => Brother
                        [2] => Human
                    )
            )
    )
