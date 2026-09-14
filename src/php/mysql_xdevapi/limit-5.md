---
title: TableDelete::limit
description: Limita las filas eliminadas
source_url: https://www.php.net/manual/es/mysql-xdevapi-tabledelete.limit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/tabledelete/limit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 86e6094e8
order: 54530
---

TableDelete::limit

Limita las filas eliminadas

## Descripción

```php
public mysql_xdevapi\TableDelete::limit(int $rows): mysql_xdevapi\TableDelete
```php

Define el número máximo de registros o documentos a eliminar.

## Parámetros

`rows`  
El máximo de registros o documentos a eliminar.

## Valores devueltos

Un objeto TableDelete.

## Ejemplos

Ejemplo de `mysql_xdevapi\TableDelete::limit`

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
