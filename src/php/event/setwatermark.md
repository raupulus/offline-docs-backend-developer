---
title: EventBufferEvent::setWatermark
description: Activa la lectura, y/o la escritura de las marcas de agua
source_url: https://www.php.net/manual/es/eventbufferevent.setwatermark.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbufferevent/setwatermark.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 940ea8c1b
order: 19550
---

EventBufferEvent::setWatermark

Activa la lectura, y/o la escritura de las marcas de agua

## Descripción

```php
public EventBufferEvent::setWatermark(int $events, int $lowmark, int $highmark): void
```php

Activa la lectura, la escritura o ambas para las *marcas de agua* de un búfer de eventos.

Una marca de agua de búfer de eventos es una porción, un valor que especifica el número de bytes a leer o escribir antes de llamar a la función de retrollamada. Por omisión, cada evento de lectura/escritura lanza una función de retrollamada. Vea también la siguiente página (en inglés): [Fast portable non-blocking network programming with Libevent: Callbacks and watermarks](http://www.wangafu.net/~nickm/libevent-book/Ref6_bufferevent.html#_callbacks_and_watermarks)

## Parámetros

`events`  
Máscara de constantes `Event::READ`, `Event::WRITE`, o ambas.

`lowmark`  
Valor mínimo de la marca de agua.

`highmark`  
Valor máximo de la marca de agua. El valor `0` significa "sin límite".

## Valores devueltos

No se retorna ningún valor.
