---
title: SqlStatementResult::fetchOne
description: Devuelve una sola línea
source_url: https://www.php.net/manual/es/mysql-xdevapi-sqlstatementresult.fetchone.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/sqlstatementresult/fetchone.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 23c4a01e6
order: 54240
---

SqlStatementResult::fetchOne

Devuelve una sola línea

## Descripción

```php
public mysql_xdevapi\SqlStatementResult::fetchOne(): array
```php

Recupera una sola línea del conjunto de resultados.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El resultado, en forma de array asociativo. En caso de ausencia de resultado, null será devuelto.

## Ejemplos

Ejemplo de `mysql_xdevapi\SqlStatementResult::fetchOne`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");
$session->sql("DROP DATABASE IF EXISTS dbtest")->execute();
$session->sql("CREATE DATABASE dbtest")->execute();
$session->sql("CREATE TABLE dbtest.workers(name text, age int, job text)")->execute();
$session->sql("INSERT INTO dbtest.workers values ('John', 42, 'bricklayer'), ('Sam', 33, 'carpenter')")->execute();

$schema = $session->getSchema("dbtest");
$table  = $schema->getTable("workers");

$rows = $session->sql("SELECT * FROM dbtest.workers")->execute()->fetchOne();

print_r($rows);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [name] => John
        [age] => 42
        [job] => bricklayer
    )
