---
title: Collection::getSession
description: Devuelve el objeto session
source_url: https://www.php.net/manual/es/mysql-xdevapi-collection.getsession.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collection/getsession.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 53090
---

Collection::getSession

Devuelve el objeto session

## Descripción

```php
public mysql_xdevapi\Collection::getSession(): Session
```php

Devuelve un nuevo objeto Session a partir del objeto Collection.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un objeto Session.

## Ejemplos

Ejemplo de `mysql_xdevapi\Collection::getSession`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");
$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();

$schema     = $session->getSchema("addressbook");
$collection = $schema->createCollection("people");

// ...

$newsession = $collection->getSession();

var_dump($session);
var_dump($newsession);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(mysql_xdevapi\Session)#1 (0) {
    }
    object(mysql_xdevapi\Session)#4 (0) {
    }
