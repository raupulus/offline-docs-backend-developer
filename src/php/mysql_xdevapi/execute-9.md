---
title: TableSelect::execute
description: Ejecuta una declaración select
source_url: https://www.php.net/manual/es/mysql-xdevapi-tableselect.execute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/tableselect/execute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 18f9cbcbc
order: 54610
---

TableSelect::execute

Ejecuta una declaración select

## Descripción

```php
public mysql_xdevapi\TableSelect::execute(): mysql_xdevapi\RowResult
```php

Ejecuta la declaración select encadenándola con el método execute().

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un objeto RowResult.

## Ejemplos

Ejemplo de `mysql_xdevapi\TableSelect::execute`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$schema = $session->getSchema("addressbook");
$table  = $schema->getTable("names");

$result = $table->select('name','age')
  ->where('name like :name and age > :age')
  ->bind(['name' => 'John', 'age' => 42])
  ->orderBy('age desc')
  ->execute();

$row = $result->fetchAll();
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
    )
