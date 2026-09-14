---
title: Session::startTransaction
description: Inicia una transacción
source_url: https://www.php.net/manual/es/mysql-xdevapi-session.starttransaction.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/session/starttransaction.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 54150
---

Session::startTransaction

Inicia una transacción

## Descripción

```php
public mysql_xdevapi\Session::startTransaction(): void
```php

Inicia una nueva transacción.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un objeto SqlStatementResult.

## Ejemplos

Ejemplo de `mysql_xdevapi\Session::startTransaction`

```
<?php
$session    = mysql_xdevapi\getSession("mysqlx://user:password@localhost");
$collection = $session->getSchema("addressbook")->getCollection("friends");

$session->startTransaction();
$collection->add( '{"test1":1, "test2":2}' )->execute();

$savepoint = $session->setSavepoint();

$collection->add( '{"test3":3, "test4":4}' )->execute();

$session->releaseSavepoint($savepoint);
$session->rollback();
?>

   
```php
