---
title: Collection::modify
description: Modifica los documentos de la colección
source_url: https://www.php.net/manual/es/mysql-xdevapi-collection.modify.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collection/modify.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: ee5228571
order: 53100
---

Collection::modify

Modifica los documentos de la colección

## Descripción

```php
public mysql_xdevapi\Collection::modify(string $search_condition): mysql_xdevapi\CollectionModify
```php

Modifica los documentos de una colección que cumplen con condiciones de búsqueda específicas. Se permiten varias operaciones y se soporta la ligadura de argumentos.

## Parámetros

`search_condition`  
Debe ser una expresión SQL válida utilizada para hacer coincidir los documentos a modificar. Esta expresión puede ser tan simple como `true`, que coincide con todos los documentos, o puede utilizar funciones y operadores tales como `'CAST(_id AS SIGNED) >= 10'`, `'age MOD 2 = 0 OR age MOD 3 = 0'`, o `'_id IN ["2","5","7","10"]'`.

## Valores devueltos

SI la operación no se ejecuta, entonces la función devolverá un objeto Modify que puede ser utilizado para añadir operaciones de modificación adicionales.

Si la operación de modificación se ejecuta, entonces el objeto devuelto contendrá el resultado de la operación.

## Ejemplos

Ejemplo de `mysql_xdevapi\Collection::modify`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();

$schema     = $session->getSchema("addressbook");
$collection = $schema->createCollection("people");

$collection->add('{"name": "Alfred", "age": 18, "job": "Butler"}')->execute();
$collection->add('{"name": "Bob",    "age": 19, "job": "Painter"}')->execute();

// Añade dos nuevos trabajos para todos los Painters: Artist y Crafter
$collection
  ->modify("job in ('Butler', 'Painter')")
  ->arrayAppend('job', 'Artist')
  ->arrayAppend('job', 'Crafter')
  ->execute();

// Elimina el campo 'beer' de todos los documentos con edad menor a 21
$collection
  ->modify('age < 21')
  ->unset(['beer'])
  ->execute();
?>

   
```php
