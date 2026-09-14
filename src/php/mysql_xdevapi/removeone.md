---
title: Collection::removeOne
description: Elimina un documento de la colección
source_url: https://www.php.net/manual/es/mysql-xdevapi-collection.removeone.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collection/removeone.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: ea05e49a9
order: 53120
---

Collection::removeOne

Elimina un documento de la colección

## Descripción

```php
public mysql_xdevapi\Collection::removeOne(string $id): mysql_xdevapi\Result
```php

Elimina un documento de la colección con el ID correspondiente. Esto es un atajo para `Collection.remove("_id = :id").bind("id", id).execute()`.

## Parámetros

`id`  
El identificador del documento de la colección a eliminar. Generalmente es el \_id generado por el servidor MySQL al añadir el registro.

## Valores devueltos

Un objeto Result que puede ser utilizado para consultar el número de elementos afectados o el número de advertencias generadas por la operación.

## Ejemplos

Ejemplo de `mysql_xdevapi\Collection::removeOne`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();

$schema     = $session->getSchema("addressbook");
$collection = $schema->createCollection("people");

$result = $collection->add('{"name": "Alfred", "age": 18, "job": "Butler"}')->execute();

// Normalmente el _id es conocido por otros medios,
// pero para este ejemplo, recuperemos el identificador generado y utilicémoslo
$ids       = $result->getGeneratedIds();
$alfred_id = $ids[0];

$result = $collection->removeOne($alfred_id);

if(!$result->getAffectedItemsCount()) {
    echo "Alfred con id $alfred_id no fue eliminado.";
} else {
    echo "Adiós, Alfred, puedes llevarte el _id $alfred_id contigo.";
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Adiós, Alfred, puedes llevarte el _id 00005b6b536100000000000000cb contigo.
