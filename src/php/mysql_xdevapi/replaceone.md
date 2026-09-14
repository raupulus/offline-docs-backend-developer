---
title: Collection::replaceOne
description: Reemplaza un documento de la colección
source_url: https://www.php.net/manual/es/mysql-xdevapi-collection.replaceone.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collection/replaceone.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 53130
---

Collection::replaceOne

Reemplaza un documento de la colección

## Descripción

```php
public mysql_xdevapi\Collection::replaceOne(string $id, string $doc): mysql_xdevapi\Result
```php

Modifica (o reemplaza) el documento identificado por ID, si existe.

## Parámetros

`id`  
El identificador del documento a reemplazar o actualizar. Típicamente es el \_id generado por el servidor MySQL al añadir el registro.

`doc`  
El documento de la colección a actualizar o reemplazar correspondiente al argumento `id`.

Este documento puede ser un objeto documento o un string JSON válido que describa el nuevo documento.

## Valores devueltos

Un objeto Result que puede ser utilizado para consultar el número de elementos afectados y el número de advertencias generadas por la operación.

## Ejemplos

Ejemplo de `mysql_xdevapi\Collection::replaceOne`

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

// ...

$alfred = $collection->getOne($alfred_id);
$alfred['age'] = 81;
$alfred['job'] = 'Guru';

$collection->replaceOne($alfred_id, $alfred);

?>

   
```php
