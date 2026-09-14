---
title: RowResult::getWarnings
description: Devuelve las advertencias de la última operación
source_url: https://www.php.net/manual/es/mysql-xdevapi-rowresult.getwarnings.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/rowresult/getwarnings.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 286ab7c12
order: 53840
---

RowResult::getWarnings

Devuelve las advertencias de la última operación

## Descripción

```php
public mysql_xdevapi\RowResult::getWarnings(): array
```php

Devuelve las advertencias de la última operación RowResult.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un array de objetos Warning de la última operación. Cada objeto define un mensaje de error 'message', un nivel de error 'level', y un código de error 'code'. Un array vacío es devuelto si no hay errores presentes.

## Ejemplos

Ejemplo de `mysql_xdevapi\RowResult::getWarnings`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("CREATE DATABASE foo")->execute();
$session->sql("CREATE TABLE foo.test_table(x int)")->execute();

$schema = $session->getSchema("foo");
$table  = $schema->getTable("test_table");

$table->insert(['x'])->values([1])->values([2])->execute();

$res = $table->select(['x/0 as bad_x'])->execute();
$warnings = $res->getWarnings();

print_r($warnings);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => mysql_xdevapi\Warning Object
            (
                [message] => Division by 0
                [level] => 2
                [code] => 1365
            )
        [1] => mysql_xdevapi\Warning Object
            (
                [message] => Division by 0
                [level] => 2
                [code] => 1365
            )
    )
