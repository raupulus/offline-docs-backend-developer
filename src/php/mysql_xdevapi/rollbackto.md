---
title: Session::rollbackTo
description: Anula la transacción hasta el punto de salvaguarda
source_url: https://www.php.net/manual/es/mysql-xdevapi-session.rollbackto.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/session/rollbackto.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 54120
---

Session::rollbackTo

Anula la transacción hasta el punto de salvaguarda

## Descripción

```php
public mysql_xdevapi\Session::rollbackTo(string $name): void
```php

Anula la transacción hasta el punto de salvaguarda.

## Parámetros

`name`  
El nombre del punto de salvaguarda hasta el cual anular; no sensible a mayúsculas y minúsculas.

## Valores devueltos

Un objeto SqlStatementResult.

## Ejemplos

Ejemplo de `mysql_xdevapi\Session::rollbackTo`

```
<?php
$session    = mysql_xdevapi\getSession("mysqlx://user:password@localhost");
$collection = $session->getSchema("addressbook")->getCollection("names");

$session->startTransaction();
$collection->add( '{"test1":1, "test2":2}' )->execute();

$savepoint1 = $session->setSavepoint();

$collection->add( '{"test3":3, "test4":4}' )->execute();

$savepoint2 = $session->setSavepoint();

$session->rollbackTo($savepoint1);
?>

   
```php
