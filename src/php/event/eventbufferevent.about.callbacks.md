---
title: Acerca de las funciones de retrollamada del buffer de eventos
source_url: https://www.php.net/manual/es/eventbufferevent.about.callbacks.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbufferevent.about.callbacks.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: a47dff201
order: 19660
---

## Acerca de las funciones de retrollamada del buffer de eventos

Un objeto de la clase `EventBufferEvent` representa un *buffer de eventos*. La naturaleza asíncrona de I/O realizada por Libevent implica que un socket (o cualquier otro tipo de descriptor de ficheros) no siempre está disponible. Event invoca las funciones de retrollamada correspondientes cuando el recurso se vuelve disponible para una lectura o una escritura, o cuando ocurren eventos (i.e. un error, un fin de línea, etc.).

Las funciones de retrollamada de lectura y escritura deben corresponder al siguiente prototipo:

```php
callback([EventBufferEvent $bev], [mixed $arg]): void
```php

`bev`  
Objeto `EventBufferEvent` asociado.

`arg`  
Variable personalizada adjunta a todas las funciones de retrollamada a través del método EventBufferEvent::\_\_construct o del método EventBufferEvent::setCallbacks.

Una función de retrollamada de evento debe corresponder al siguiente prototipo:

```php
callback([EventBufferEvent $bev], [int $events], [mixed $arg]): void
```

`bev`  
Objeto `EventBufferEvent` asociado.

`events`  
Máscara de bits de eventos: `EventBufferEvent::READING`, `EventBufferEvent::WRITING`, `EventBufferEvent::EOL`, `EventBufferEvent::ERROR` y `EventBufferEvent::TIMEOUT`. Ver las [constantes EventBufferEvent](#eventbufferevent.constants).

`arg`  
Variable personalizada adjunta a todas las funciones de retrollamada a través del método EventBufferEvent::\_\_construct o del método EventBufferEvent::setCallbacks.
