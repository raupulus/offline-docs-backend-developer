---
title: Yaf_Dispatcher::setErrorHandler
description: Establece el gestor de errores
source_url: https://www.php.net/manual/es/yaf-dispatcher.seterrorhandler.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_dispatcher/seterrorhandler.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_reviewed: false
translation_revision: 49d4fb555
order: 105800
---

Yaf_Dispatcher::setErrorHandler

Establece el gestor de errores

## Descripción

```php
public Yaf_Dispatcher::setErrorHandler(call $callback, int $error_types): Yaf_Dispatcher
```php

Establece el gestor de errores de Yaf. Cuando [application.dispatcher.throwException](#configuration.yaf.dispatcher.throwexception) está desactivada, Yaf provocará errores capturables mientras ocurran errores inesperados.

Por lo tanto, este gestor de errores será invocado mientras se produce el error.

## Parámetros

`callback`  
Una llamada de retorno de tipo callable.

`error_types`  

## Valores devueltos

## Véase también

Yaf_Dispatcher::throwException

Yaf_Application::getLastErrorNo

Yaf_Application::getLastErrorMsg
