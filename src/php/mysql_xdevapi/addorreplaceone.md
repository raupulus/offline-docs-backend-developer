---
title: Collection::addOrReplaceOne
description: Añade o reemplaza un documento de la colección
source_url: https://www.php.net/manual/es/mysql-xdevapi-collection.addorreplaceone.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collection/addorreplaceone.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 52990
---

Collection::addOrReplaceOne

Añade o reemplaza un documento de la colección

## Descripción

```php
public mysql_xdevapi\Collection::addOrReplaceOne(string $id, string $doc): mysql_xdevapi\Result
```php

Añade un nuevo documento, o reemplaza un documento si ya existe.

Existen varios escenarios para este método:

- Ni el id ni ningún valor de clave única están en conflicto con un documento de la colección, entonces el documento es añadido.

- Si el id no corresponde a ningún documento, pero uno o más valores de clave única entran en conflicto con un documento de la colección, entonces se lanza un error.

- Si el id corresponde a un documento existente y ninguna clave única está definida para la colección, entonces el documento es reemplazado.

- Si el id corresponde a un documento existente, y todas las claves únicas del documento de reemplazo corresponden a ese mismo documento o no están en conflicto con ningún otro documento de la colección, entonces el documento es reemplazado.

- Si el id corresponde a un documento existente, y una o más claves únicas corresponden a otro documento de la colección, entonces se lanza un error.

## Parámetros

`id`  
Este es el identificador del filtro. Si este identificador o cualquier otro campo que tiene un índice único ya existe en la colección, entonces actualizará el documento correspondiente.

Por omisión, este identificador es generado automáticamente por el servidor MySQL cuando el documento ha sido añadido, y es referenciado como un campo nombrado '\_id'.

`doc`  
Este es el documento a añadir o reemplazar, que es una cadena JSON.

## Valores devueltos

Un objeto Result.

## Ejemplos

Ejemplo de `mysql_xdevapi\Collection::addOrReplaceOne`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");
$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();

$schema = $session->getSchema("addressbook");
$create = $schema->createCollection("people");

$collection = $schema->getCollection("people");

// Utilizar add()
$result = $collection->add('{"name": "Wilma", "age": 23, "job": "Teacher"}')->execute();

// Utilizar addOrReplaceOne()
// Nota: pasamos aquí un valor _id conocido
$result = $collection->addOrReplaceOne('00005b6b53610000000000000056', '{"name": "Fred",  "age": 21, "job": "Construction"}');

?>

   
```php
