---
title: TableInsert::execute
description: Ejecuta una consulta de inserción
source_url: https://www.php.net/manual/es/mysql-xdevapi-tableinsert.execute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/tableinsert/execute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 18f9cbcbc
order: 54570
---

TableInsert::execute

Ejecuta una consulta de inserción

## Descripción

```php
public mysql_xdevapi\TableInsert::execute(): mysql_xdevapi\Result
```php

Ejecuta la declaración.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un objeto Result.

## Ejemplos

Ejemplo de `mysql_xdevapi\TableInsert::execute`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();
$session->sql("CREATE TABLE addressbook.names(name text, age int)")->execute();
$session->sql("INSERT INTO addressbook.names values ('John', 42), ('Sam', 33)")->execute();

$schema = $session->getSchema("addressbook");
$table  = $schema->getTable("names");

$table
  ->insert("name", "age")
  ->values(["Suzanne", 31],["Julie", 43])
  ->execute();
?>

   
```php
