---
title: Collection::remove
description: Elimina documentos de la colección
source_url: https://www.php.net/manual/es/mysql-xdevapi-collection.remove.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collection/remove.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 6cfb4b27b
order: 53110
---

Collection::remove

Elimina documentos de la colección

## Descripción

```php
public mysql_xdevapi\Collection::remove(string $search_condition): mysql_xdevapi\CollectionRemove
```php

Elimina documentos de una colección que cumplen con condiciones de búsqueda específicas. Se permiten varias operaciones, y la ligadura de argumentos.

## Parámetros

`search_condition`  
Debe ser una expresión SQL válida utilizada para hacer coincidir los documentos a modificar. Esta expresión puede ser tan simple como `true`, que coincide con todos los documentos, o puede utilizar funciones y operadores tales como `'CAST(_id AS SIGNED) >= 10'`, `'age MOD 2 = 0 OR age MOD 3 = 0'`, o `'_id IN ["2","5","7","10"]'`.

## Valores devueltos

Si la operación no se ejecuta, entonces la función devolverá un objeto Remove que puede ser utilizado para añadir operaciones de eliminación adicionales.

SI la operación de eliminación se ejecuta, entonces el objeto devuelto contendrá el resultado de la operación.

## Ejemplos

Ejemplo de `mysql_xdevapi\Collection::remove`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();

$schema     = $session->getSchema("addressbook");
$collection = $schema->createCollection("people");

$collection->add('{"name": "Alfred", "age": 18, "job": "Butler"}')->execute();
$collection->add('{"name": "Bob",    "age": 19, "job": "Painter"}')->execute();

// Elimina todos los painters
$collection
  ->remove("job in ('Painter')")
  ->execute();

// Elimina el butler más viejo
$collection
  ->remove("job in ('Butler')")
  ->sort('age desc')
  ->limit(1)
  ->execute();

// Elimina el registro con la edad más alta
$collection
  ->remove('true')
  ->sort('age desc')
  ->limit(1)
  ->execute();
?>

   
```php
