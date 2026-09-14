---
title: Table::select
description: Selecciona filas en una tabla
source_url: https://www.php.net/manual/es/mysql-xdevapi-table.select.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/table/select.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 9e0f03ac3
order: 54480
---

Table::select

Selecciona filas en una tabla

## Descripción

```php
public mysql_xdevapi\Table::select(mixed $columns, mixed ...$more_columns): mysql_xdevapi\TableSelect
```php

Recupera datos de una tabla.

## Parámetros

`columns`  
Las columnas desde las cuales recuperar los datos. Puede ser un array con uno o más valores, o un string.

`more_columns`  
Definiciones de columnas adicionales.

## Valores devueltos

Un objeto TableSelect; utilice el método execute() para ejecutar la selección y devolver un objeto RowResult.

## Ejemplos

Ejemplo de `mysql_xdevapi\Table::count`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();
$session->sql("CREATE TABLE addressbook.names(name text, age int)")->execute();
$session->sql("INSERT INTO addressbook.names values ('John', 42), ('Sam', 33)")->execute();

$schema = $session->getSchema("addressbook");
$table  = $schema->getTable("names");

$row = $table->select('name', 'age')->execute()->fetchAll();

print_r($row);

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => Array
            (
                [name] => John
                [age] => 42
            )
        [1] => Array
            (
                [name] => Sam
                [age] => 33
            )
    )
