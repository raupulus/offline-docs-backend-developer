---
title: Session::getServerVersion
description: Devuelve la versión del servidor
source_url: https://www.php.net/manual/es/mysql-xdevapi-session.getserverversion.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/session/getserverversion.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 86e6094e8
order: 54070
---

Session::getServerVersion

Devuelve la versión del servidor

## Descripción

```php
public mysql_xdevapi\Session::getServerVersion(): int
```php

Devuelve la versión del servidor MySQL para la sesión.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

La versión del servidor MySQL para la sesión, en forma de entero como "80012".

## Ejemplos

Ejemplo de `mysql_xdevapi\Session::getServerVersion`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$version = $session->getServerVersion();

var_dump($version);

   
```php

Resultado del ejemplo anterior es similar a:

    int(80012)
