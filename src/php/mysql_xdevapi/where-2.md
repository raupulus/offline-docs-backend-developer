---
title: TableSelect::where
description: Define los criterios de búsqueda de la selección
source_url: https://www.php.net/manual/es/mysql-xdevapi-tableselect.where.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/tableselect/where.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 18f9cbcbc
order: 54690
---

TableSelect::where

Define los criterios de búsqueda de la selección

## Descripción

```php
public mysql_xdevapi\TableSelect::where(string $where_expr): mysql_xdevapi\TableSelect
```php

Define las condiciones de búsqueda para filtrar.

## Parámetros

`where_expr`  
Define la condición de búsqueda para filtrar los documentos o los registros.

## Valores devueltos

Un objeto TableSelect.

## Ejemplos

Ejemplo de `mysql_xdevapi\TableSelect::where`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$schema = $session->getSchema("addressbook");
$table  = $schema->getTable("names");

$result = $table->select('name','age')
  ->where('name like :name and age > :age')
  ->bind(['name' => 'John', 'age' => 42])
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
                [name] => John
                [age] => 42
            )
    )
