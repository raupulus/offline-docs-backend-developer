---
title: RowResult::fetchOne
description: Devuelve una fila del resultado
source_url: https://www.php.net/manual/es/mysql-xdevapi-rowresult.fetchone.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/rowresult/fetchone.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: '475439775'
order: 53800
---

RowResult::fetchOne

Devuelve una fila del resultado

## Descripción

```php
public mysql_xdevapi\RowResult::fetchOne(): array
```php

Recupera una fila del conjunto de resultados.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El resultado, en forma de array asociativo o `null` si no hay resultado presente.

## Ejemplos

Ejemplo de `mysql_xdevapi\RowResult::fetchOne`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();
$session->sql("CREATE TABLE addressbook.names(name text, age int)")->execute();
$session->sql("INSERT INTO addressbook.names values ('John', 42), ('Sam', 33)")->execute();

$schema = $session->getSchema("addressbook");
$table  = $schema->getTable("names");

$row = $table->select('name', 'age')->where('age < 40')->execute()->fetchOne();

print_r($row);

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [name] => Sam
        [age] => 33
    )
