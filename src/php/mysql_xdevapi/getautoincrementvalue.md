---
title: Result::getAutoIncrementValue
description: Devuelve el valor auto-incrementado
source_url: https://www.php.net/manual/es/mysql-xdevapi-result.getautoincrementvalue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/result/getautoincrementvalue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 53740
---

Result::getAutoIncrementValue

Devuelve el valor auto-incrementado

## Descripción

```php
public mysql_xdevapi\Result::getAutoIncrementValue(): int
```php

Devuelve el último valor AUTO_INCREMENT (último identificador insertado).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El último valor AUTO_INCREMENT.

## Ejemplos

Ejemplo de `mysql_xdevapi\Result::getAutoIncrementValue`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();
$session->sql("
  CREATE TABLE addressbook.names
    (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(30), age INT, PRIMARY KEY (id))
  ")->execute();

$schema = $session->getSchema("addressbook");
$table  = $schema->getTable("names");

$result = $table->insert("name", "age")->values(["Suzanne", 31],["Julie", 43])->execute();
$result = $table->insert("name", "age")->values(["Suki", 34])->execute();

$ai = $result->getAutoIncrementValue();
var_dump($ai);
?>

   
```php

El ejemplo anterior mostrará:

    int(3)
