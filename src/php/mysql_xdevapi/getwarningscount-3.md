---
title: Result::getWarningsCount
description: Devuelve el número de advertencias de la última operación
source_url: https://www.php.net/manual/es/mysql-xdevapi-result.getwarningscount.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/result/getwarningscount.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 86e6094e8
order: 53770
---

Result::getWarningsCount

Devuelve el número de advertencias de la última operación

## Descripción

```php
public mysql_xdevapi\Result::getWarningsCount(): int
```php

Devuelve el número de advertencias generadas por la última operación.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El número de advertencias generadas por la última operación.

## Ejemplos

Ejemplo de `mysql_xdevapi\RowResult::getWarningsCount`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE IF EXISTS foo")->execute();
$session->sql("CREATE DATABASE foo")->execute();
$session->sql("CREATE TABLE foo.test_table(x int)")->execute();

$schema = $session->getSchema("foo");
$table  = $schema->getTable("test_table");

$table->insert(['x'])->values([1])->values([2])->execute();

$res = $table->select(['x/0 as bad_x'])->execute();

echo $res->getWarningsCount();
?>

   
```php

Resultado del ejemplo anterior es similar a:

    2
