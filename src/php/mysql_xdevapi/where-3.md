---
title: TableUpdate::where
description: Define el filtro de búsqueda
source_url: https://www.php.net/manual/es/mysql-xdevapi-tableupdate.where.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/tableupdate/where.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 18f9cbcbc
order: 54760
---

TableUpdate::where

Define el filtro de búsqueda

## Descripción

```php
public mysql_xdevapi\TableUpdate::where(string $where_expr): mysql_xdevapi\TableUpdate
```php

Define la condición de búsqueda para el filtro.

## Parámetros

`where_expr`  
La condición de búsqueda para filtrar los documentos o los registros.

## Valores devueltos

Un objeto TableUpdate.

## Ejemplos

Ejemplo de `mysql_xdevapi\TableUpdate::where`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$schema = $session->getSchema("addressbook");
$table  = $schema->getTable("names");

$res = $table->update()
  ->set('level', 3)
  ->where('age > 15 and age < 22')
  ->limit(4)
  ->orderby(['age asc','name desc'])
  ->execute();

?>

   
```php
