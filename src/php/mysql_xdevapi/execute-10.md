---
title: TableUpdate::execute
description: Ejecuta la consulta de actualización
source_url: https://www.php.net/manual/es/mysql-xdevapi-tableupdate.execute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/tableupdate/execute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 18f9cbcbc
order: 54720
---

TableUpdate::execute

Ejecuta la consulta de actualización

## Descripción

```php
public mysql_xdevapi\TableUpdate::execute(): mysql_xdevapi\TableUpdate
```php

Ejecuta la declaración de actualización.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un objeto TableUpdate.

## Ejemplos

Ejemplo de `mysql_xdevapi\TableUpdate::execute`

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
