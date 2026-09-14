---
title: Session::__construct
description: Descripción del constructor
source_url: https://www.php.net/manual/es/mysql-xdevapi-session.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/session/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 54000
---

Session::\_\_construct

Descripción del constructor

## Descripción

```php
private mysql_xdevapi\Session::__construct()
```php

Un objeto Session, tal como iniciado por getSession().

## Parámetros

Esta función no contiene ningún parámetro.

## Ejemplos

Ejemplo de `mysql_xdevapi\Session::__construct`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");
$session->close();
?>

   
```php
