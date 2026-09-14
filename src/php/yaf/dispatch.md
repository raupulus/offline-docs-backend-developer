---
title: Yaf_Dispatcher::dispatch
description: Despachar una petición
source_url: https://www.php.net/manual/es/yaf-dispatcher.dispatch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_dispatcher/dispatch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_reviewed: false
translation_revision: 49d4fb555
order: 105640
---

Yaf_Dispatcher::dispatch

Despachar una petición

## Descripción

```php
public Yaf_Dispatcher::dispatch(Yaf_Request_Abstract $request): Yaf_Response_Abstract
```php

Este método realiza el trabajo duro de la clase `Yaf_Dispatcher`. Toma un objeto de petición.

El proceso de despachamiento posee tres eventos distintos: Enrutamiento, Despachamiento, Respuesta El enrutamiento ocurre exactamente una vez, usando los valores del objeto de petición al llamar a `Yaf_Dispatcher::dispatch`. El despachamiento tiene lugar en un bucle; una petición puede indicar o múltiples acciones a despachar, o el controlador, o un complemento puede reiniciar el objeto de petición para forzar acciones adicionales a despachar (véase la clase `Yaf_Plugin_Abstract`. Cuando todo ha sido realizado, la clase `Yaf_Dispatcher` devuelve una respuesta.

## Parámetros

`request`  

## Valores devueltos
