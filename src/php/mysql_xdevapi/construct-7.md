---
title: ColumnResult::__construct
description: Constructor de ColumnResult
source_url: https://www.php.net/manual/es/mysql-xdevapi-columnresult.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/columnresult/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: ee5228571
order: 53440
---

ColumnResult::\_\_construct

Constructor de ColumnResult

## Descripción

```php
private mysql_xdevapi\ColumnResult::__construct()
```php

Devuelve los metadatos de columna, tales como su conjunto de caracteres; esto es instanciado por el método mysql_xdevapi\RowResult::getColumns.

## Parámetros

Esta función no contiene ningún parámetro.

## Ejemplos

Ejemplo de `mysql_xdevapi\ColumnResult::__construct`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE IF EXISTS nonsense")->execute();
$session->sql("CREATE DATABASE nonsense")->execute();
$session->sql("CREATE TABLE nonsense.numbers (hello int, world float unsigned)")->execute();
$session->sql("INSERT INTO  nonsense.numbers values (42, 42)")->execute();

$schema = $session->getSchema("nonsense");
$table  = $schema->getTable("numbers");

$result1 = $table->select('hello','world')->execute();

// Devuelve un array de objetos ColumnResult
$columns = $result1->getColumns();

foreach ($columns as $column) {
    echo "\nColumn label " , $column->getColumnLabel();
    echo " is type "       , $column->getType();
    echo " and is ", ($column->isNumberSigned() === 0) ? "unsigned." : "signed.";
}

// O bien
$result2 = $session->sql("SELECT * FROM nonsense.numbers")->execute();

// Devuelve un array de objetos FieldMetadata
print_r($result2->getColumns());

   
```php

Resultado del ejemplo anterior es similar a:

    Column label hello is type 19 and is signed.
    Column label world is type 4  and is unsigned.

    Array
    (
        [0] => mysql_xdevapi\FieldMetadata Object
            (
                [type] => 1
                [type_name] => SINT
                [name] => hello
                [original_name] => hello
                [table] => numbers
                [original_table] => numbers
                [schema] => nonsense
                [catalog] => def
                [collation] => 0
                [fractional_digits] => 0
                [length] => 11
                [flags] => 0
                [content_type] => 0
            )
        [1] => mysql_xdevapi\FieldMetadata Object
            (
                [type] => 6
                [type_name] => FLOAT
                [name] => world
                [original_name] => world
                [table] => numbers
                [original_table] => numbers
                [schema] => nonsense
                [catalog] => def
                [collation] => 0
                [fractional_digits] => 31
                [length] => 12
                [flags] => 1
                [content_type] => 0
            )
    )
