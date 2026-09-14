---
title: RowResult::getColumnsCount
description: Devuelve el número de columnas
source_url: https://www.php.net/manual/es/mysql-xdevapi-rowresult.getcolumncount.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/rowresult/getcolumncount.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: '420684312'
order: 53810
---

RowResult::getColumnsCount

Devuelve el número de columnas

## Descripción

```php
public mysql_xdevapi\RowResult::getColumnsCount(): int
```php

Devuelve el número de columnas presentes en el conjunto de resultados.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El número de columnas; 0 si no hay ninguna.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.14 | El método ha sido renombrado de getColumnCount() a getColumnsCount(). |

## Ejemplos

Ejemplo de `mysql_xdevapi\RowResult::getColumnsCount`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE addressbook")->execute();
$session->sql("CREATE DATABASE foo")->execute();
$session->sql("CREATE TABLE foo.test_table(x int)")->execute();
$session->sql("INSERT INTO addressbook.names values ('John', 42), ('Sam', 33)")->execute();

$sql = $session->sql("SELECT * from addressbook.names")->execute();

echo $sql->getColumnsCount();

   
```php

Resultado del ejemplo anterior es similar a:

    2
