---
title: TableUpdate::set
description: Añade un campo a actualizar
source_url: https://www.php.net/manual/es/mysql-xdevapi-tableupdate.set.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/tableupdate/set.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 18f9cbcbc
order: 54750
---

TableUpdate::set

Añade un campo a actualizar

## Descripción

```php
public mysql_xdevapi\TableUpdate::set(string $table_field, string $expression_or_literal): mysql_xdevapi\TableUpdate
```php

Actualiza el valor de la columna en los registros de una tabla.

## Parámetros

`table_field`  
El nombre de la columna a actualizar.

`expression_or_literal`  
El valor a definir en la columna especificada.

## Valores devueltos

Un objeto TableUpdate.

## Ejemplos

Ejemplo de `mysql_xdevapi\TableUpdate::set`

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
