---
title: ZMQDevice::setTimerTimeout
description: Establecer el tiempo de espera del temporizador
source_url: https://www.php.net/manual/es/zmqdevice.settimertimeout.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zmq/zmqdevice/settimertimeout.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zmq
translation_status: ready
translation_reviewed: false
translation_revision: be295015d
order: 109220
---

ZMQDevice::setTimerTimeout

Establecer el tiempo de espera del temporizador

## Descripción

```php
public ZMQDevice::setTimerTimeout(int $timeout): ZMQDevice
```php

Establece el valor de tiempo de espera de la retrollamada del temporizador. La retrollamada del temporizador se invoca periódicamente si está establecida. Se añadion en la versión 1.1.0 de la extensión ZMQ.

## Parámetros

`timeout`  
El valor del tiempo de espera de la retrollamada del temporizador.

## Valores devueltos

En caso de éxito, este método devuelve el objeto actual.
