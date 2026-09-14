---
title: Yaf_Request_Http::get
description: Recupera una variable del cliente
source_url: https://www.php.net/manual/es/yaf-request-http.get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_request_http/get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: 6ab98a443
order: 106420
---

Yaf_Request_Http::get

Recupera una variable del cliente

## Descripción

```php
public Yaf_Request_Http::get(string $name, [string $default]): mixed
```php

Recupera una variable del cliente. Este método buscará el nombre dado por `name` en los parámetros de solicitud, y si no se encuetra el nombre, buscará en POST, GET, Cookie, Server

## Parámetros

`name`  
El nombre de la variable.

`default`  
Si se proporciona este parámetro, será devuelto si no se pudo encontrar la variable.

## Valores devueltos

## Véase también

Yaf_Request_Http::getQuery

Yaf_Request_Http::getPost

Yaf_Request_Http::getCookie

Yaf_Request_Http::getRaw

Yaf_Request_Abstract::getServer

Yaf_Request_Abstract::getParam
