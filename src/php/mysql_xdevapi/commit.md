---
title: Session::commit
description: Valida la transacción
source_url: https://www.php.net/manual/es/mysql-xdevapi-session.commit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/session/commit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 53990
---

Session::commit

Valida la transacción

## Descripción

```php
public mysql_xdevapi\Session::commit(): Object
```php

Valida la transacción.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un objeto SqlStatementResult.

## Ejemplos

Ejemplo de `mysql_xdevapi\Session::commit`

```
<?php
$session    = mysql_xdevapi\getSession("mysqlx://user:password@localhost");
$collection = $session->getSchema("addressbook")->getCollection("friends");

$session->startTransaction();

$collection->add('{"John":42, "Sam":33}')->execute();
$savepoint = $session->setSavepoint();

$session->commit();
$session->close();

   
```php
