---
title: TableSelect::offset
description: Define el desplazamiento del límite
source_url: https://www.php.net/manual/es/mysql-xdevapi-tableselect.offset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/tableselect/offset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 86e6094e8
order: 54670
---

TableSelect::offset

Define el desplazamiento del límite

## Descripción

```php
public mysql_xdevapi\TableSelect::offset(int $position): mysql_xdevapi\TableSelect
```php

Ignora un número dado de filas en el resultado.

## Parámetros

`position`  
El desplazamiento del límite.

## Valores devueltos

Un objeto TableSelect.

## Ejemplos

Ejemplo de `mysql_xdevapi\TableSelect::offset`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();
$session->sql("CREATE TABLE addressbook.names(name text, age int)")->execute();
$session->sql("INSERT INTO addressbook.names values ('John', 42), ('Sam', 42)")->execute();

$schema = $session->getSchema("addressbook");
$table  = $schema->getTable("names");

$result = $table->select('name', 'age')
  ->limit(1)
  ->offset(1)
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
                [name] => Sam
                [age] => 42
            )
    )
