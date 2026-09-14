---
title: Yaf_Plugin_Abstract::dispatchLoopShutdown
description: El propósito de dispatchLoopShutdown
source_url: https://www.php.net/manual/es/yaf-plugin-abstract.dispatchloopshutdown.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_plugin_abstract/dispatchloopshutdown.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_reviewed: false
translation_revision: '356967704'
order: 105990
---

Yaf_Plugin_Abstract::dispatchLoopShutdown

El propósito de dispatchLoopShutdown

## Descripción

```php
public Yaf_Plugin_Abstract::dispatchLoopShutdown(Yaf_Request_Abstract $request, Yaf_Response_Abstract $response): void
```php

Este es el último enganche del sistema de enganches de complementos de Yaf. Si un complemento personalizado implementa este método, será llamado después de que finalice el bucle de despachamientos.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`request`  

`response`  

## Valores devueltos

## Véase también

Yaf_Plugin_Abstract::routerStartup

Yaf_Plugin_Abstract::routerShutdown

Yaf_Plugin_Abstract::dispatchLoopStartup

Yaf_Plugin_Abstract::preDispatch

Yaf_Plugin_Abstract::postDispatch
