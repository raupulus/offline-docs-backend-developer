---
title: Session::getSchemas
description: Devuelve los esquemas
source_url: https://www.php.net/manual/es/mysql-xdevapi-session.getschemas.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/session/getschemas.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 54060
---

Session::getSchemas

Devuelve los esquemas

## Descripción

```php
public mysql_xdevapi\Session::getSchemas(): array
```php

Obtiene los objetos esquema para todos los esquemas disponibles para la sesión.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un array que contiene objetos que representan todos los esquemas disponibles para la sesión.

## Ejemplos

Ejemplo de `mysql_xdevapi\Session::getSchemas`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");
$schemas  = $session->getSchemas();

print_r($schemas);

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => mysql_xdevapi\Schema Object
            (
                [name] => addressbook
            )
        [1] => mysql_xdevapi\Schema Object
            (
                [name] => information_schema
            )
        ...
