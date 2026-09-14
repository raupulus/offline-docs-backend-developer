---
title: Schema::getSession
description: Devuelve la sesión del esquema
source_url: https://www.php.net/manual/es/mysql-xdevapi-schema.getsession.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/schema/getsession.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 53940
---

Schema::getSession

Devuelve la sesión del esquema

## Descripción

```php
public mysql_xdevapi\Schema::getSession(): mysql_xdevapi\Session
```php

Devuelve un nuevo objeto Session a partir del objeto Schema.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un objeto Session.

## Ejemplos

Ejemplo de `mysql_xdevapi\Schema::getSession`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");
$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();

$schema  = $session->getSchema("addressbook");

// ...

$newsession = $schema->getSession();

var_dump($session);
var_dump($newsession);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(mysql_xdevapi\Session)#1 (0) {
    }

    object(mysql_xdevapi\Session)#3 (0) {
    }
