---
title: Session::sql
description: Crear una consulta SQL
source_url: https://www.php.net/manual/es/mysql-xdevapi-session.sql.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/session/sql.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: ee5228571
order: 54140
---

Session::sql

Crear una consulta SQL

## Descripción

```php
public mysql_xdevapi\Session::sql(string $query): mysql_xdevapi\SqlStatement
```php

Crear una declaración SQL nativa. Los espacios reservados son compatibles utilizando la sintaxis nativa "?". Utilizar el método `execute` para ejecutar la declaración SQL.

## Parámetros

`query`  
La declaración SQL a ejecutar.

## Valores devueltos

Un objeto SqlStatement.

## Ejemplos

Ejemplo de `mysql_xdevapi\Session::sql`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("CREATE DATABASE addressbook")->execute();
?>

   
```php
