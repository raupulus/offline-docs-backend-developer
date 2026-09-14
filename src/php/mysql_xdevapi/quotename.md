---
title: Session::quoteName
description: Añade comillas
source_url: https://www.php.net/manual/es/mysql-xdevapi-session.quotename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/session/quotename.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 54090
---

Session::quoteName

Añade comillas

## Descripción

```php
public mysql_xdevapi\Session::quoteName(string $name): string
```php

Una función que pone entre comillas para escapar los nombres e identificadores SQL. Es capaz de escapar el identificador dado conforme a los parámetros de la conexión actual. Esta función de escape no debe ser utilizada para escapar valores.

## Parámetros

`name`  
La cadena a poner entre comillas.

## Valores devueltos

La cadena puesta entre comillas.

## Ejemplos

Ejemplo de `mysql_xdevapi\Session::quoteName`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$first = "MySQL's test";
var_dump($first);
var_dump($session->quoteName($first));

$second = 'Another `test` "like" `this`';
var_dump($second);
var_dump($session->quoteName($second));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(12) "MySQL's test"
    string(14) "`MySQL's test`"

    string(28) "Another `test` "like" `this`"
    string(34) "`Another ``test`` "like" ``this```"
