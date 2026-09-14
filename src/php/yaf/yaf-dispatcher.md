---
title: La clase Yaf_Dispatcher
source_url: https://www.php.net/manual/es/class.yaf-dispatcher.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf-dispatcher.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 104590
---

## Introducción

El propósito de la clase `Yaf_Dispatcher` es inicializar el entorno de peticiones, enrutar las peticiones entrantes, y despachar cuanlquier acción encontrada; agrega cualesquiera respuestas y las devuelve cuando el proceso está completado.

`Yaf_Dispatcher` también implementa el patrón Singleton, lo que significa que solamente puede estar disponible una instancia de la misma a la vez. Esto le permite también actuar como un registro en el que se puede establecer el orden de los objetos del proceso de despachamiento.

## Sinopsis de la clase

Yaf_Dispatcher

final

Yaf_Dispatcher

Propiedades

protected

\_router

protected

\_view

protected

\_request

protected

\_plugins

protected

static

\_instance

protected

\_auto_render

protected

\_return_response

protected

\_instantly_flush

protected

\_default_module

protected

\_default_controller

protected

\_default_action

Métodos

## Propiedades

`_router`  

`_view`  

`_request`  

`_plugins`  

`_instance`  

`_auto_render`  

`_return_response`  

`_instantly_flush`  

`_default_module`  

`_default_controller`  

`_default_action`
