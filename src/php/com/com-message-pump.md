---
title: com_message_pump
description: Procesa un mensaje COM en un tiempo dado
source_url: https://www.php.net/manual/es/function.com-message-pump.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/com/functions/com-message-pump.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: com
translation_status: ready
translation_reviewed: false
translation_revision: 20216b916
order: 7720
---

com_message_pump

Procesa un mensaje COM en un tiempo dado

## Descripción

```php
com_message_pump([int $timeout_milliseconds]): bool
```php

Procesa un mensaje COM esperando hasta `timeout_milliseconds` milisegundos, o bien esperando a que un mensaje llegue a la cola.

El propósito de esta función es enrutar las llamadas COM entre los elementos y gestionar las diferentes sincronizaciones. Esto permite que el script espere eficientemente los eventos a desencadenar, mientras gestiona otros eventos o ejecuta otros scripts en segundo plano. Debe ser utilizada en un bucle, como en el ejemplo de la función `com_event_sink`, hasta que se haya terminado de utilizar los objetos COM relacionados con eventos.

## Parámetros

`timeout_milliseconds`  
El tiempo de espera, en milisegundos.

Si no se especifica un valor para el parámetro `timeout_milliseconds`, entonces será 0. Un valor de 0 significa que los mensajes serán procesados inmediatamente; si hay mensajes en la cola, serán distribuidos de inmediato; si no hay mensajes en la cola, la función devolverá `false` inmediatamente sin esperar.

## Valores devueltos

Si uno o más mensajes llegan antes de que expire el tiempo de espera, serán distribuidos y la función devolverá `true`. Si el tiempo de espera expira y no se procesa ningún mensaje, el valor devuelto será `false`.
