---
title: Session::close
description: Cierra la sesión
source_url: https://www.php.net/manual/es/mysql-xdevapi-session.close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/session/close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 53980
---

Session::close

Cierra la sesión

## Descripción

```php
public mysql_xdevapi\Session::close(): bool
```php

Cierra la sesión con el servidor.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`true` si la sesión ha sido cerrada.

## Ejemplos

Ejemplo de `mysql_xdevapi\Session::close`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$schema = $session->getSchema("addressbook");
$table  = $schema->getTable("names");

$session->close();

   
```php
