---
title: RowResult::getColumnNames
description: Devuelve el nombre de todas las columnas
source_url: https://www.php.net/manual/es/mysql-xdevapi-rowresult.getcolumnnames.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/rowresult/getcolumnnames.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 286ab7c12
order: 53820
---

RowResult::getColumnNames

Devuelve el nombre de todas las columnas

## Descripción

```php
public mysql_xdevapi\RowResult::getColumnNames(): array
```php

Devuelve el nombre de las columnas presentes en el conjunto de resultados.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un array numérico de nombres de columnas de tabla, o un array vacío si el conjunto de resultados está vacío.

## Ejemplos

Ejemplo de `mysql_xdevapi\RowResult::getColumnNames`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE addressbook")->execute();
$session->sql("CREATE DATABASE foo")->execute();
$session->sql("CREATE TABLE foo.test_table(x int)")->execute();
$session->sql("INSERT INTO addressbook.names values ('John', 42), ('Sam', 33)")->execute();

$sql = $session->sql("SELECT * from addressbook.names")->execute();

$colnames = $sql->getColumnNames();

print_r($colnames);

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => name
        [1] => age
    )
