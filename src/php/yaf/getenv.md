---
title: Yaf_Request_Abstract::getEnv
description: Recupera la variable ENV
source_url: https://www.php.net/manual/es/yaf-request-abstract.getenv.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_request_abstract/getenv.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: 6ab98a443
order: 106150
---

Yaf_Request_Abstract::getEnv

Recupera la variable ENV

## Descripción

```php
public Yaf_Request_Abstract::getEnv(string $name, [string $default]): void
```php

Recupera la variable ENV.

## Parámetros

`name`  
El nombre de la varaible.

`default`  
Si se proporciona este parámetro, se devolverá si la variable no puede ser encontrada.

## Valores devueltos

Devuelve un string

## Véase también

Yaf_Request_Abstract::getServer

Yaf_Request_Abstract::getParam
