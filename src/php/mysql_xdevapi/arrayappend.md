---
title: CollectionModify::arrayAppend
description: Añade un elemento a un campo de array
source_url: https://www.php.net/manual/es/mysql-xdevapi-collectionmodify.arrayappend.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collectionmodify/arrayappend.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 53270
---

CollectionModify::arrayAppend

Añade un elemento a un campo de array

## Descripción

```php
public mysql_xdevapi\CollectionModify::arrayAppend(string $collection_field, string $expression_or_literal): mysql_xdevapi\CollectionModify
```php

Añade un elemento a un campo de un documento, ya que varios elementos de un campo se representan como un array. A diferencia de arrayInsert(), arrayAppend() siempre añade el nuevo elemento al final del array, mientras que arrayInsert() puede definir la ubicación.

## Parámetros

`collection_field`  
El identificador del campo donde se inserta el nuevo elemento.

`expression_or_literal`  
El nuevo elemento a insertar al final del array del campo del documento.

## Valores devueltos

Un objeto CollectionModify que puede ser utilizado para ejecutar el comando, o para añadir operaciones adicionales.

## Ejemplos

Ejemplo de `mysql_xdevapi\CollectionModify::arrayAppend`

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
  ->modify("name in ('Bernie', 'Jane')")
  ->arrayAppend('traits', 'Happy')
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
                [_id] => 00005b6b5361000000000000010c
                [name] => Bernie
                [traits] => Array
                    (
                        [0] => Friend
                        [1] => Brother
                        [2] => Human
                        [3] => Happy
                    )
            )
    )
