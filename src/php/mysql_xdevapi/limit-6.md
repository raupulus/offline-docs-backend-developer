---
title: TableSelect::limit
description: Limita las filas seleccionadas
source_url: https://www.php.net/manual/es/mysql-xdevapi-tableselect.limit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/tableselect/limit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 86e6094e8
order: 54640
---

TableSelect::limit

Limita las filas seleccionadas

## Descripción

```php
public mysql_xdevapi\TableSelect::limit(int $rows): mysql_xdevapi\TableSelect
```php

Define el número máximo de registros o documentos a devolver.

## Parámetros

`rows`  
El número máximo de registros o documentos.

## Valores devueltos

Un objeto TableSelect.

## Ejemplos

Ejemplo de `mysql_xdevapi\TableSelect::limit`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$schema = $session->getSchema("addressbook");
$table  = $schema->getTable("names");

$result = $table->select('name', 'age')
  ->limit(1)
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
