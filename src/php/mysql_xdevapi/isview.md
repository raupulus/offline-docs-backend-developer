---
title: Table::isView
description: Devuelve si la tabla es una vista
source_url: https://www.php.net/manual/es/mysql-xdevapi-table.isview.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/table/isview.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: ee5228571
order: 54470
---

Table::isView

Devuelve si la tabla es una vista

## Descripción

```php
public mysql_xdevapi\Table::isView(): bool
```php

Determina si el objeto subyacente es una vista o no.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`true` si el objeto subyacente es una vista, de lo contrario `false`.

## Ejemplos

Ejemplo de `mysql_xdevapi\Table::isView`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();
$session->sql("CREATE TABLE addressbook.names(name text, age int)")->execute();
$session->sql("INSERT INTO addressbook.names values ('John', 42), ('Sam', 33)")->execute();

$schema = $session->getSchema("addressbook");
$table  = $schema->getTable("names");

if ($table->isView()) {
    echo "This is a view.";
} else {
    echo "This is not a view.";
}
?>

   
```php

El ejemplo anterior mostrará:

    This is not a view.
