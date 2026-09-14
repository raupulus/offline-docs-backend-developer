---
title: Collection::getName
description: Devuelve el nombre de la colección
source_url: https://www.php.net/manual/es/mysql-xdevapi-collection.getname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collection/getname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 53060
---

Collection::getName

Devuelve el nombre de la colección

## Descripción

```php
public mysql_xdevapi\Collection::getName(): string
```php

Devuelve el nombre de la colección.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El nombre de la colección, en forma de string.

## Ejemplos

Ejemplo de `mysql_xdevapi\Collection::getName`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();

$schema     = $session->getSchema("addressbook");
$collection = $schema->createCollection("people");

// ...

var_dump($collection->getName());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(6) "people"
