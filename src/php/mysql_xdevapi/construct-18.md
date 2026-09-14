---
title: Table::__construct
description: Constructor de Table
source_url: https://www.php.net/manual/es/mysql-xdevapi-table.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/table/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 54390
---

Table::\_\_construct

Constructor de Table

## Descripción

```php
private mysql_xdevapi\Table::__construct()
```php

Construye un objeto table.

## Parámetros

Esta función no contiene ningún parámetro.

## Ejemplos

Ejemplo de `mysql_xdevapi\Table::__construct`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$schema = $session->getSchema("addressbook");
$table  = $schema->getTable("names");
?>

   
```php
