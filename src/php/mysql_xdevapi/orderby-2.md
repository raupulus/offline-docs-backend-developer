---
title: TableSelect::orderby
description: Define los criterios de ordenación de la selección
source_url: https://www.php.net/manual/es/mysql-xdevapi-tableselect.orderby.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/tableselect/orderby.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 79d9994b8
order: 54680
---

TableSelect::orderby

Define los criterios de ordenación de la selección

## Descripción

```php
public mysql_xdevapi\TableSelect::orderby(mixed $sort_expr, mixed ...$sort_exprs): mysql_xdevapi\TableSelect
```php

Define los criterios de ordenación.

## Parámetros

`sort_expr`  
La expresión que define los criterios de ordenación. Puede ser un array con una o más expresiones, o un string.

`sort_exprs`  
Parámetros adicionales para sort_expr.

## Valores devueltos

Un objeto TableSelect.

## Ejemplos

Ejemplo de `mysql_xdevapi\TableSelect::orderBy`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$schema = $session->getSchema("addressbook");
$table  = $schema->getTable("names");

$result = $table->select('name', 'age')
  ->orderBy('name desc')
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
        [1] => Array
            (
                [name] => John
                [age] => 42
            )
    )
