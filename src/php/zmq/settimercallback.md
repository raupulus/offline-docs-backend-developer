---
title: ZMQDevice::setTimerCallback
description: Establecer la función de retrollamada del temporizador
source_url: https://www.php.net/manual/es/zmqdevice.settimercallback.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zmq/zmqdevice/settimercallback.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zmq
translation_status: ready
translation_reviewed: false
translation_revision: 184764a63
order: 109210
---

ZMQDevice::setTimerCallback

Establecer la función de retrollamada del temporizador

## Descripción

```php
public ZMQDevice::setTimerCallback(callable $cb_func, int $timeout, [mixed $user_data]): ZMQDevice
```php

Establece la función de retrollamada del temporizador. La retrollamada del temporizador será invocada después de haber pasado el tiempo de espera. La diferencia entre las retrollamadas de inactividad y del temporizador es que la de inactividad es invocada solamente cuando el dispositivo está inactivo. La firma de la función de retrollamada es callback (mixed \$datos_usuario). Se añadió en la verisón 1.1.0 de la extensión ZMQ.

## Parámetros

`cb_func`  
Función de retrollamada a invocar cuando se dispara el temporizador. La devolución de false o de un valor que se evalú como false por parte de esta función causará la detención del dispositivo.

`timeout`  
Frecuencia con la que se invoca la retrollamada del temporizador en milisegundos. La retrollamada del temporizador se invoca periódicamente. El valor del tiempo de espera garantiza que haya al menos dicha cantidad de milisegundos entre invocaciones a la función de retrollamada.

`user_data`  
Datos adcionales a pasar a la función de retrollamada.

## Valores devueltos

En caso de éxito, este método devuelve el objeto actual.
