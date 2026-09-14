---
title: GearmanClient::clearCallbacks
description: Elimina todas las funciones de retrollamada de las tareas
source_url: https://www.php.net/manual/es/gearmanclient.clearcallbacks.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanclient/clearcallbacks.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 24980
---

GearmanClient::clearCallbacks

Elimina todas las funciones de retrollamada de las tareas

## Descripción

```php
public GearmanClient::clearCallbacks(): bool
```php

Elimina todas las funciones de retrollamada de las tareas previamente definidas.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Siempre devuelve `true`.

## Véase también

GearmanClient::setDataCallback

GearmanClient::setCompleteCallback

GearmanClient::setCreatedCallback

GearmanClient::setExceptionCallback

GearmanClient::setFailCallback

GearmanClient::setStatusCallback

GearmanClient::setWarningCallback

GearmanClient::setWorkloadCallback
