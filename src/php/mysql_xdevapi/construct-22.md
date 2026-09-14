---
title: TableUpdate::__construct
description: Constructor de TableUpdate
source_url: https://www.php.net/manual/es/mysql-xdevapi-tableupdate.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/tableupdate/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 54710
---

TableUpdate::\_\_construct

Constructor de TableUpdate

## Descripción

```php
private mysql_xdevapi\TableUpdate::__construct()
```php

Inicializado por el método update().

## Parámetros

Esta función no contiene ningún parámetro.

## Ejemplos

Ejemplo de `mysql_xdevapi\TableUpdate::__construct`

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
