---
title: Schema::getName
description: Devuelve el nombre del esquema
source_url: https://www.php.net/manual/es/mysql-xdevapi-schema.getname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/schema/getname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 53930
---

Schema::getName

Devuelve el nombre del esquema

## Descripción

```php
public mysql_xdevapi\Schema::getName(): string
```php

Devuelve el nombre del esquema.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El nombre del esquema conectado al objeto esquema, en forma de string.

## Ejemplos

Ejemplo de `mysql_xdevapi\Schema::getName`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");
$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();

$schema  = $session->getSchema("addressbook");

// ...

var_dump($schema->getName());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(11) "addressbook"
