---
title: Session::releaseSavepoint
description: Libera el punto de salvaguarda
source_url: https://www.php.net/manual/es/mysql-xdevapi-session.releasesavepoint.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/session/releasesavepoint.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 54100
---

Session::releaseSavepoint

Libera el punto de salvaguarda

## Descripción

```php
public mysql_xdevapi\Session::releaseSavepoint(string $name): void
```php

Libera un punto de salvaguarda previamente definido.

## Parámetros

`name`  
El nombre del punto de salvaguarda a liberar.

## Valores devueltos

Un objeto SqlStatementResult.

## Ejemplos

Ejemplo de `mysql_xdevapi\Session::releaseSavepoint`

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
