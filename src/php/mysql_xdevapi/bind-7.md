---
title: TableSelect::bind
description: Liga los argumentos de la petición select
source_url: https://www.php.net/manual/es/mysql-xdevapi-tableselect.bind.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/tableselect/bind.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 18f9cbcbc
order: 54590
---

TableSelect::bind

Liga los argumentos de la petición select

## Descripción

```php
public mysql_xdevapi\TableSelect::bind(array $placeholder_values): mysql_xdevapi\TableSelect
```php

Liga un valor a un espacio reservado específico.

## Parámetros

`placeholder_values`  
El nombre del espacio reservado y el valor a ligar.

## Valores devueltos

Un objeto TableSelect.

## Ejemplos

Ejemplo de `mysql_xdevapi\TableSelect::bind`

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
