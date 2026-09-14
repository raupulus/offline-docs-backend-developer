---
title: DatabaseObject::getSession
description: Devuelve el nombre de la sesión
source_url: https://www.php.net/manual/es/mysql-xdevapi-databaseobject.getsession.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/databaseobject/getsession.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 18f9cbcbc
order: 53630
---

DatabaseObject::getSession

Devuelve el nombre de la sesión

## Descripción

```php
abstract public mysql_xdevapi\DatabaseObject::getSession(): mysql_xdevapi\Session
```php

Recupera la sesión asociada al objeto de base de datos.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El objeto Session.

## Ejemplos

Ejemplo de `mysql_xdevapi\DatabaseObject::getSession`

```
<?php

$session = $dbObj->getSession();

?>

   
```php
