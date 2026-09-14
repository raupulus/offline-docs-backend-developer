---
title: Client::__construct
description: Constructor del cliente
source_url: https://www.php.net/manual/es/mysql-xdevapi-client.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/client/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 41eaa8885
order: 52960
---

Client::\_\_construct

Constructor del cliente

## Descripción

```php
private mysql_xdevapi\Client::__construct()
```php

Construye un objeto cliente.

## Parámetros

Esta función no contiene ningún parámetro.

## Ejemplos

Ejemplo de `mysql_xdevapi\Client::__construct`

```
<?php
$pooling_options = '{
  "enabled": true,
    "maxSize": 10,
    "maxIdleTime": 3600,
    "queueTimeOut": 1000
}';
$client = mysql_xdevapi\getClient($connection_uri, $pooling_options);
$session = $client->getSession();

   
```php
