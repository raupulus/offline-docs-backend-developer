---
title: Session::rollback
description: Revierte la transacción
source_url: https://www.php.net/manual/es/mysql-xdevapi-session.rollback.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/session/rollback.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 54110
---

Session::rollback

Revierte la transacción

## Descripción

```php
public mysql_xdevapi\Session::rollback(): void
```php

Revierte la transacción.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un objeto SqlStatementResult.

## Ejemplos

Ejemplo de `mysql_xdevapi\Session::rollback`

```
<?php
$session    = mysql_xdevapi\getSession("mysqlx://user:password@localhost");
$collection = $session->getSchema("addressbook")->getCollection("names");

$session->startTransaction();
$collection->add( '{"test1":1, "test2":2}' )->execute();

$savepoint = $session->setSavepoint();

$collection->add( '{"test3":3, "test4":4}' )->execute();

$session->releaseSavepoint($savepoint);
$session->rollback();
?>

   
```php
