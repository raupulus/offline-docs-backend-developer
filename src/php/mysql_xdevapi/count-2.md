---
title: Table::count
description: Devuelve el número de filas
source_url: https://www.php.net/manual/es/mysql-xdevapi-table.count.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/table/count.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 86e6094e8
order: 54400
---

Table::count

Devuelve el número de filas

## Descripción

```php
public mysql_xdevapi\Table::count(): int
```php

Recupera el número de filas en la tabla.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El número total de filas en la tabla.

## Ejemplos

Ejemplo de `mysql_xdevapi\Table::count`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();
$session->sql("CREATE TABLE addressbook.names(name text, age int)")->execute();
$session->sql("INSERT INTO addressbook.names values ('John', 42), ('Sam', 33)")->execute();

$schema = $session->getSchema("addressbook");
$table  = $schema->getTable("names");

var_dump($table->count());
?>

   
```php

El ejemplo anterior mostrará:

    int(2)
