---
title: Schema::getTable
description: Devuelve la tabla del esquema
source_url: https://www.php.net/manual/es/mysql-xdevapi-schema.gettable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/schema/gettable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 53950
---

Schema::getTable

Devuelve la tabla del esquema

## Descripción

```php
public mysql_xdevapi\Schema::getTable(string $name): mysql_xdevapi\Table
```php

Recupera un objeto Table para la tabla proporcionada en el esquema.

## Parámetros

`name`  
El nombre de la tabla.

## Valores devueltos

Un objeto table.

## Ejemplos

Ejemplo de `mysql_xdevapi\Schema::getTable`

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
?>

   
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
