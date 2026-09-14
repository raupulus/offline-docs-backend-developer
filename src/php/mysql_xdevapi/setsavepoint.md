---
title: Session::setSavepoint
description: Crear un punto de salvaguarda
source_url: https://www.php.net/manual/es/mysql-xdevapi-session.setsavepoint.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/session/setsavepoint.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 54130
---

Session::setSavepoint

Crear un punto de salvaguarda

## Descripción

```php
public mysql_xdevapi\Session::setSavepoint([string $name]): string
```php

Crear un nuevo punto de salvaguarda para la transacción.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`name`  
El nombre del punto de salvaguarda. El nombre se genera automáticamente si el argumento opcional `name` no está definido como 'SAVEPOINT1', 'SAVEPOINT2', etc.

## Valores devueltos

El nombre del punto de salvaguarda.

## Ejemplos

Ejemplo de `mysql_xdevapi\Session::setSavepoint`

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
