---
title: Yaf_Plugin_Abstract::routerStartup
description: Enganche deEl propósito de routerStartup
source_url: https://www.php.net/manual/es/yaf-plugin-abstract.routerstartup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_plugin_abstract/routerstartup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_reviewed: false
translation_revision: '356967704'
order: 106050
---

Yaf_Plugin_Abstract::routerStartup

Enganche deEl propósito de routerStartup

## Descripción

```php
public Yaf_Plugin_Abstract::routerStartup(Yaf_Request_Abstract $request, Yaf_Response_Abstract $response): void
```php

Este es el primer enchanche del sistema de enganches de complementos de Yaf. Si un complemento personalizado implementa este método, será llamado antes de enrutar una petición.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`request`  

`response`  

## Valores devueltos

## Véase también

Yaf_Plugin_Abstract::routerShutdown

Yaf_Plugin_Abstract::dispatchLoopStartup

Yaf_Plugin_Abstract::preDispatch

Yaf_Plugin_Abstract::postDispatch

Yaf_Plugin_Abstract::dispatchLoopShutdown
