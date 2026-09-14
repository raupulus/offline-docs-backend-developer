---
title: Result::getAffectedItemsCount
description: Devuelve el número de filas afectadas
source_url: https://www.php.net/manual/es/mysql-xdevapi-result.getaffecteditemscount.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/result/getaffecteditemscount.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 1fe6a1faa
order: 53730
---

Result::getAffectedItemsCount

Devuelve el número de filas afectadas

## Descripción

```php
public mysql_xdevapi\Result::getAffectedItemsCount(): int
```php

Devuelve el número de filas afectadas por la operación anterior.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El número (como integer) de filas afectadas.

## Ejemplos

Ejemplo de `mysql_xdevapi\Result::getAffectedItemsCount`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();

$schema = $session->getSchema("addressbook");
$create = $schema->createCollection("people");

$collection = $schema->getCollection("people");

$result = $collection->add('{"name": "Wilma", "age": 23, "job": "Teacher"}')->execute();

var_dump( $res->getAffectedItemsCount() );
?>

   
```php

El ejemplo anterior mostrará:

    int(1)
