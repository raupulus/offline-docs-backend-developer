---
title: TableDelete::execute
description: Ejecuta la consulta de eliminación
source_url: https://www.php.net/manual/es/mysql-xdevapi-tabledelete.execute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/tabledelete/execute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 18f9cbcbc
order: 54520
---

TableDelete::execute

Ejecuta la consulta de eliminación

## Descripción

```php
public mysql_xdevapi\TableDelete::execute(): mysql_xdevapi\Result
```php

Ejecuta la consulta de eliminación.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un objeto Result.

## Ejemplos

Ejemplo de `mysql_xdevapi\TableDelete::execute`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();
$session->sql("CREATE TABLE addressbook.names(name text, age int)")->execute();
$session->sql("INSERT INTO addressbook.names values ('John', 42), ('Sam', 33)")->execute();

$schema = $session->getSchema("addressbook");
$table  = $schema->getTable("names");

$table->delete()
  ->where("name = :name")
  ->bind(['name' => 'John'])
  ->orderby("age DESC")
  ->limit(1)
  ->execute();

?>

   
```php
