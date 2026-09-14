---
title: RowResult::fetchAll
description: Devuelve todas las filas del resultado
source_url: https://www.php.net/manual/es/mysql-xdevapi-rowresult.fetchall.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/rowresult/fetchall.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 23c4a01e6
order: 53790
---

RowResult::fetchAll

Devuelve todas las filas del resultado

## Descripción

```php
public mysql_xdevapi\RowResult::fetchAll(): array
```php

Recupera todas las filas del conjunto de resultados.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un array numérico con todos los resultados de la consulta; cada resultado es un array asociativo. Se devuelve un array vacío si no hay filas presentes.

## Ejemplos

`mysql_xdevapi\RowResult::fetchAll` example

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE addressbook")->execute();
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
