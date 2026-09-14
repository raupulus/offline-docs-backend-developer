---
title: Collection::dropIndex
description: Elimina un índice de colección
source_url: https://www.php.net/manual/es/mysql-xdevapi-collection.dropindex.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collection/dropindex.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 73fae4ee5
order: 53030
---

Collection::dropIndex

Elimina un índice de colección

## Descripción

```php
public mysql_xdevapi\Collection::dropIndex(string $index_name): bool
```php

Elimina un índice de colección.

Esta operación no lanza un error si el índice no existe, pero `false` es devuelto en este caso.

## Parámetros

`index_name`  
El nombre del índice de colección a eliminar.

## Valores devueltos

`true` si la operación DROP INDEX ha tenido éxito, de lo contrario `false`.

## Ejemplos

Ejemplo de `mysql_xdevapi\Collection::dropIndex`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();

$schema = $session->getSchema("addressbook");
$create = $schema->createCollection("people");

// ...

$collection = $schema->getCollection("people");

$collection->createIndex(
  'myindex',
  '{"fields": [{"field": "$.name", "type": "TEXT(25)", "required": true}], "unique": false}'
);

// ...

if ($collection->dropIndex('myindex')) {
    echo "Un índice llamado 'myindex' fue encontrado y eliminado.";
}
?>

   
```php

El ejemplo anterior mostrará:

    Un índice llamado 'myindex' fue encontrado y eliminado.
