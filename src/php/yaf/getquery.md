---
title: Yaf_Request_Http::getQuery
description: Obtiene un parámetro de una consulta
source_url: https://www.php.net/manual/es/yaf-request-http.getquery.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_request_http/getquery.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: 6ab98a443
order: 106460
---

Yaf_Request_Http::getQuery

Obtiene un parámetro de una consulta

## Descripción

```php
public Yaf_Request_Http::getQuery(string $name, [string $default]): mixed
```php

Recupera una variable de GET.

## Parámetros

`name`  
El nombre de la variable.

`default`  
Si se proporciona este parámetro, será devuelto si no se pudo encontrar la variable.

## Valores devueltos

## Véase también

Yaf_Request_Http::get

Yaf_Request_Http::getPost

Yaf_Request_Http::getCookie

Yaf_Request_Http::getRaw

Yaf_Request_Abstract::getServer

Yaf_Request_Abstract::getParam
