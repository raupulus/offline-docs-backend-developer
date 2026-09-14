---
title: Table::update
description: Actualiza las filas de la tabla
source_url: https://www.php.net/manual/es/mysql-xdevapi-table.update.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/table/update.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 18f9cbcbc
order: 54490
---

Table::update

Actualiza las filas de la tabla

## Descripción

```php
public mysql_xdevapi\Table::update(): mysql_xdevapi\TableUpdate
```php

Actualiza las columnas de una tabla.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un objeto TableUpdate; utilice el método execute() para ejecutar la instrucción de actualización.

## Ejemplos

Ejemplo de `mysql_xdevapi\Table::update`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();
$session->sql("CREATE TABLE addressbook.names(name text, age int)")->execute();
$session->sql("INSERT INTO addressbook.names values ('John', 42), ('Sam', 33)")->execute();

$schema = $session->getSchema("addressbook");
$table  = $schema->getTable("names");

$table->update()->set('age',34)->where('name = "Sam"')->limit(1)->execute();
?>

   
```php
