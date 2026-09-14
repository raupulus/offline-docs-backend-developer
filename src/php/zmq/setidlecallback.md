---
title: ZMQDevice::setIdleCallback
description: Establecer la función de retrollamada de inactividad
source_url: https://www.php.net/manual/es/zmqdevice.setidlecallback.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zmq/zmqdevice/setidlecallback.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zmq
translation_status: ready
translation_reviewed: false
translation_revision: be295015d
order: 109190
---

ZMQDevice::setIdleCallback

Establecer la función de retrollamada de inactividad

## Descripción

```php
public ZMQDevice::setIdleCallback(callable $cb_func, int $timeout, [mixed $user_data]): ZMQDevice
```php

Establece la función de retrollamada de inactividad. Si el tiempo de espera está definido, la función de retrollamada de inactividad será invocada si el bucle de sondeo interno expira sin eventos. Si la función de retrollamada devuelve false o un valor que se evalúa como false, el dispositivo se detendrá. La firma de la función de retrollamada es callback (mixed \$datos_usuario).

## Parámetros

`cb_func`  
Función de retrollamada a invocar cuando el dispositivo está inactivo. La devolución de false o de un valor que se evalú como false por parte de esta función causará la detención del dispositivo.

`timeout`  
Frecuencia con la que se invoca la retrollamada de inactividad en milisegundos. La retrollamada de inactividad se invoca periódicamente cuando no hay actividad en el dispositivo. El valor del tiempo de espera garantiza que haya al menos dicha cantidad de milisegundos entre invocaciones a la función de retrollamada.

`user_data`  
Datos adcionales a pasar a la función de retrollamada.

## Valores devueltos

En caso de éxito, este método devuelve el objeto actual.
