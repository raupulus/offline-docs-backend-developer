---
title: Session::generateUUID
description: Devuelve un nuevo UUID
source_url: https://www.php.net/manual/es/mysql-xdevapi-session.generateuuid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/session/generateuuid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 54030
---

Session::generateUUID

Devuelve un nuevo UUID

## Descripción

```php
public mysql_xdevapi\Session::generateUUID(): string
```php

Genera un identificador único universal (Universal Unique IDentifier - UUID) generado según la [RFC 4122](https://datatracker.ietf.org/doc/html/rfc4122).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El UUID; una cadena de 32 caracteres.

## Ejemplos

Ejemplo de `mysql_xdevapi\Session::generateUuid`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$uuid = $session->generateUuid();

var_dump($uuid);

   
```php

Resultado del ejemplo anterior es similar a:

    string(32) "484B18AC7980F8D4FE84613CDA5EE84B"
