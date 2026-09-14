---
title: TableDelete::bind
description: Liga los argumentos de la petición de eliminación
source_url: https://www.php.net/manual/es/mysql-xdevapi-tabledelete.bind.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/tabledelete/bind.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 18f9cbcbc
order: 54500
---

TableDelete::bind

Liga los argumentos de la petición de eliminación

## Descripción

```php
public mysql_xdevapi\TableDelete::bind(array $placeholder_values): mysql_xdevapi\TableDelete
```php

Liga un valor a un espacio reservado.

## Parámetros

`placeholder_values`  
El nombre del espacio reservado y el valor a ligar.

## Valores devueltos

Un objeto TableDelete

## Ejemplos

Ejemplo de `mysql_xdevapi\TableDelete::bind`

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
