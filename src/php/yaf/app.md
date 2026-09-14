---
title: Yaf_Application::app
description: Recuperar una instancia de la clase Application
source_url: https://www.php.net/manual/es/yaf-application.app.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_application/app.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: cf91547d7
order: 104930
---

Yaf_Application::app

Recuperar una instancia de la clase Application

## Descripción

```php
public static Yaf_Application::app(): mixed
```php

Recuperar la instancia de la clase `Yaf_Application`. De forma alternativa se podría utilizar el método Yaf_Dispatcher::getApplication.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Una instancia de la clase Yaf_Application, o `null` si no se inicializó antes ninguna instancia de Yaf_Application.

## Véase también

Yaf_Dispatcher::getApplication
