---
title: CollectionModify::arrayInsert
description: Inserta un elemento en un campo de array
source_url: https://www.php.net/manual/es/mysql-xdevapi-collectionmodify.arrayinsert.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collectionmodify/arrayinsert.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: ee5228571
order: 53280
---

CollectionModify::arrayInsert

Inserta un elemento en un campo de array

## Descripción

```php
public mysql_xdevapi\CollectionModify::arrayInsert(string $collection_field, string $expression_or_literal): mysql_xdevapi\CollectionModify
```php

Añade un elemento a un campo de un documento, ya que varios elementos de un campo están representados en forma de array. A diferencia de mysql_xdevapi\CollectionModify::arrayAppend este método permite especificar dónde se inserta el nuevo elemento definiendo después de qué elemento, mientras que mysql_xdevapi\CollectionModify::arrayAppend siempre añade el nuevo elemento al final del array.

## Parámetros

`collection_field`  
Identifica el elemento del array después del cual se insertará el nuevo elemento. El formato de este parámetro es `FIELD_NAME[ INDEX ]` donde \<FIELD_NAME\> es el nombre del campo del documento donde se añadirá el elemento, y \<INDEX\> es el INDEX del elemento en el campo.

El INDEX está basado en cero, por lo que el primer elemento del array tiene un índice de 0.

`expression_or_literal`  
El nuevo elemento a insertar después de FIELD_NAME\[ INDEX \]

## Valores devueltos

Un objeto CollectionModify que puede ser utilizado para ejecutar el comando, o para añadir operaciones adicionales.

## Ejemplos

Ejemplo de `mysql_xdevapi\CollectionModify::arrayInsert`

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
  ->arrayInsert('traits[1]', 'Happy')
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
                [_id] => 00005b6b5361000000000000010d
                [name] => Bernie
                [traits] => Array
                    (
                        [0] => Friend
                        [1] => Happy
                        [2] => Brother
                        [3] => Human
                    )
            )
    )
