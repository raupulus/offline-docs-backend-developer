---
title: TableDelete::orderby
description: Define los criterios de ordenación de la eliminación
source_url: https://www.php.net/manual/es/mysql-xdevapi-tabledelete.orderby.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/tabledelete/orderby.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 18f9cbcbc
order: 54540
---

TableDelete::orderby

Define los criterios de ordenación de la eliminación

## Descripción

```php
public mysql_xdevapi\TableDelete::orderby(string $orderby_expr): mysql_xdevapi\TableDelete
```php

Define las opciones de ordenación para un conjunto de resultados.

## Parámetros

`orderby_expr`  
La definición de la ordenación.

## Valores devueltos

Un objeto TableDelete.

## Ejemplos

Ejemplo de `mysql_xdevapi\TableDelete::orderBy`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$schema = $session->getSchema("addressbook");
$table  = $schema->getTable("names");

$table->delete()
  ->where("age = :age")
  ->bind(['age' => 42])
  ->orderby("name DESC")
  ->limit(1)
  ->execute();

?>

   
```php
