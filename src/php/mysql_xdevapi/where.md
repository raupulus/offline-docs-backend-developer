---
title: TableDelete::where
description: Define la condición de búsqueda para la eliminación
source_url: https://www.php.net/manual/es/mysql-xdevapi-tabledelete.where.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/tabledelete/where.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 18f9cbcbc
order: 54550
---

TableDelete::where

Define la condición de búsqueda para la eliminación

## Descripción

```php
public mysql_xdevapi\TableDelete::where(string $where_expr): mysql_xdevapi\TableDelete
```php

Define la condición de búsqueda para filtrar.

## Parámetros

`where_expr`  
Define la condición de búsqueda para filtrar los documentos o los registros.

## Valores devueltos

Un objeto TableDelete.

## Ejemplos

Ejemplo de `mysql_xdevapi\TableDelete::where`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$schema = $session->getSchema("addressbook");
$table  = $schema->getTable("names");

$table->delete()
  ->where("id = :id")
  ->bind(['id' => 42])
  ->limit(1)
  ->execute();

?>

   
```php
