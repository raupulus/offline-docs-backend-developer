---
title: CollectionModify::bind
description: Liga un valor a un parámetro de consulta
source_url: https://www.php.net/manual/es/mysql-xdevapi-collectionmodify.bind.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collectionmodify/bind.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 53290
---

CollectionModify::bind

Liga un valor a un parámetro de consulta

## Descripción

```php
public mysql_xdevapi\CollectionModify::bind(array $placeholder_values): mysql_xdevapi\CollectionModify
```php

Liga un parámetro a un espacio reservado en la condición de búsqueda de la operación de modificación.

El espacio reservado tiene la forma de :NOMBRE donde ':' es un prefijo común que siempre debe existir antes de cualquier NOMBRE donde NOMBRE es el nombre del espacio reservado. El método bind acepta una lista de espacios reservados si varias entidades deben ser sustituidas en la condición de búsqueda de la operación de modificación.

## Parámetros

`placeholder_values`  
Los valores de espacio reservado a sustituir en la condición de búsqueda. Se permiten varios valores y deben ser pasados en forma de array de mapeos NOMBRE_ESPACIO_RESERVADO-\>VALOR_ESPACIO_RESERVADO.

## Valores devueltos

Un objeto CollectionModify que puede ser utilizado para ejecutar el comando, o para añadir operaciones adicionales.

## Ejemplos

Ejemplo de `mysql_xdevapi\CollectionModify::bind`

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
                [_id] => 00005b6b53610000000000000110
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
