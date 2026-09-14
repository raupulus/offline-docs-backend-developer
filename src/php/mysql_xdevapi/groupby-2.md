---
title: TableSelect::groupBy
description: Define los criterios de agrupación de la selección
source_url: https://www.php.net/manual/es/mysql-xdevapi-tableselect.groupby.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/tableselect/groupby.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 18f9cbcbc
order: 54620
---

TableSelect::groupBy

Define los criterios de agrupación de la selección

## Descripción

```php
public mysql_xdevapi\TableSelect::groupBy(mixed $sort_expr): mysql_xdevapi\TableSelect
```php

Define un criterio de agrupación para el conjunto de resultados.

## Parámetros

`sort_expr`  
El criterio de agrupación.

## Valores devueltos

Un objeto TableSelect.

## Ejemplos

Ejemplo de `mysql_xdevapi\TableSelect::groupBy`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();
$session->sql("CREATE TABLE addressbook.names(name text, age int)")->execute();
$session->sql("INSERT INTO addressbook.names values ('John', 42), ('Sam', 42)")->execute();
$session->sql("INSERT INTO addressbook.names values ('Suki', 31)")->execute();

$schema = $session->getSchema("addressbook");
$table  = $schema->getTable("names");

$result = $table->select('count(*) as count', 'age')
  ->groupBy('age')->orderBy('age asc')
  ->execute();

$row = $result->fetchAll();
print_r($row);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => Array
            (
                [count] => 1
                [age] => 31
            )
        [1] => Array
            (
                [count] => 2
                [age] => 42
            )
    )
