---
title: Table::delete
description: Elimina filas de la tabla
source_url: https://www.php.net/manual/es/mysql-xdevapi-table.delete.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/table/delete.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 18f9cbcbc
order: 54410
---

Table::delete

Elimina filas de la tabla

## Descripción

```php
public mysql_xdevapi\Table::delete(): mysql_xdevapi\TableDelete
```php

Elimina filas de una tabla.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un objeto TableDelete; utilice el método execute() para ejecutar la consulta de eliminación.

## Ejemplos

Ejemplo de `mysql_xdevapi\Table::delete`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();
$session->sql("CREATE TABLE addressbook.names(name text, age int)")->execute();
$session->sql("INSERT INTO addressbook.names values ('John', 42), ('Sam', 33)")->execute();

$schema = $session->getSchema("addressbook");
$table  = $schema->getTable("names");

$table->delete()->where("name = :name")->orderby("age DESC")->limit(1)->bind(['name' => 'John'])->execute();
?>

   
```php
