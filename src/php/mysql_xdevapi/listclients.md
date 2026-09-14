---
title: Session::listClients
description: Devuelve la lista de clientes
source_url: https://www.php.net/manual/es/mysql-xdevapi-session.listclients.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/session/listclients.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 54080
---

Session::listClients

Devuelve la lista de clientes

## Descripción

```php
public mysql_xdevapi\Session::listClients(): array
```php

Devuelve la lista de conexiones de clientes al servidor MySQL de la sesión.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un array que contiene los clientes actualmente conectados. Los elementos del array son "client_id", "user", "host" y "sql_session".

## Ejemplos

Ejemplo de `mysql_xdevapi\Session::listClients`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$ids = $session->listClients();

var_dump($ids);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(1) {
      [0]=>
      array(4) {
        ["client_id"]=>
        int(61)
        ["user"]=>
        string(4) "root"
        ["host"]=>
        string(9) "localhost"
        ["sql_session"]=>
        int(72)
      }
    }
