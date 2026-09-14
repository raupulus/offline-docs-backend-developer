---
title: ZMQDevice::setIdleTimeout
description: Establecer el tiempo de espera para la inactividad
source_url: https://www.php.net/manual/es/zmqdevice.setidletimeout.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zmq/zmqdevice/setidletimeout.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zmq
translation_status: ready
translation_reviewed: false
translation_revision: be295015d
order: 109200
---

ZMQDevice::setIdleTimeout

Establecer el tiempo de espera para la inactividad

## Descripción

```php
public ZMQDevice::setIdleTimeout(int $timeout): ZMQDevice
```php

Establece el valor del tiempo de espera de la retrollamada de inactividad. La retrollamada de inactividad se invoca periódicamente cuando el dispositivo está inactivo.

## Parámetros

`timeout`  
El valor del tiempo de espera de la retrollamada de inactividad.

## Valores devueltos

En caso de éxito, este método devuelve el objeto actual.
