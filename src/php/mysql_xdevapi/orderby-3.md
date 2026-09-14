---
title: TableUpdate::orderby
description: Define los criterios de ordenación
source_url: https://www.php.net/manual/es/mysql-xdevapi-tableupdate.orderby.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/tableupdate/orderby.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 9e0f03ac3
order: 54740
---

TableUpdate::orderby

Define los criterios de ordenación

## Descripción

```php
public mysql_xdevapi\TableUpdate::orderby(mixed $orderby_expr, mixed ...$orderby_exprs): mysql_xdevapi\TableUpdate
```php

Define los criterios de ordenación.

## Parámetros

`orderby_expr`  
La expresión que define los criterios de ordenación. Puede ser un array con una o más expresiones, o un string.

`orderby_exprs`  
Parámetros adicionales para las expresiones de ordenación.

## Valores devueltos

Un objeto TableUpdate.

## Ejemplos

Ejemplo de `mysql_xdevapi\TableUpdate::orderby`

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
