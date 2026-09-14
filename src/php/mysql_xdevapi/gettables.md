---
title: Schema::getTables
description: Devuelve las tablas del esquema
source_url: https://www.php.net/manual/es/mysql-xdevapi-schema.gettables.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/schema/gettables.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 53960
---

Schema::getTables

Devuelve las tablas del esquema

## Descripción

```php
public mysql_xdevapi\Schema::getTables(): array
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un array de todas las tablas de este esquema, donde cada elemento del array es un objeto Table con el nombre de la tabla como clave.

## Ejemplos

Ejemplo de `mysql_xdevapi\Schema::getTables`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();

$session->sql("CREATE TABLE addressbook.names(name text, age int)")->execute();
$session->sql("INSERT INTO addressbook.names values ('John', 42), ('Sam', 33)")->execute();

$session->sql("CREATE TABLE addressbook.cities(name text, population int)")->execute();
$session->sql("INSERT INTO addressbook.names values ('Portland', 639863), ('Seattle', 704352)")->execute();

$schema = $session->getSchema("addressbook");
$tables = $schema->getTables();

var_dump($tables);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(2) {
      ["cities"]=>
      object(mysql_xdevapi\Table)#3 (1) {
        ["name"]=>
        string(6) "cities"
      }

      ["names"]=>
      object(mysql_xdevapi\Table)#4 (1) {
        ["name"]=>
        string(5) "names"
      }
    }
