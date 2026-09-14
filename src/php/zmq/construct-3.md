---
title: ZMQDevice::__construct
description: Construir un nuevo dispositivo
source_url: https://www.php.net/manual/es/zmqdevice.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zmq/zmqdevice/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zmq
translation_status: ready
translation_reviewed: false
translation_revision: 45fb9e53a
order: 109150
---

ZMQDevice::\_\_construct

Construir un nuevo dispositivo

## Descripción

```php
public ZMQDevice::__construct(ZMQSocket $frontend, ZMQSocket $backend, [ZMQSocket $listener])
```php

"Los dispositivos de ØMQ pueden hacer de intermediarios de direcciones, servicios, colas o cualquier abstracción que se defina sobre las capas de mensaje y socket." -- zguide

## Parámetros

`frontend`  
Parámetro "frontend" para los dispositivos. Normalmente donde llegan los mensajes.

`backend`  
Parámetro "backend" para los dispositivos. Normalmente donde van los mensajes.

`listener`  
Socket escuchador, el cual recibe una copia de todos los mensajes en ambas direcciones. El tipo de este socket debería ser SUB, PULL o DEALER.

## Valores devueltos

Una llamada a este método preparará el dispositivo. Normalmente, los dispositivos son procesos de larga ejecución, por lo que no se recomienda la ejecución de este método desde un script interactivo. Este método lanza una ZMQDeviceException si el dispositivo no puede iniciarse.
