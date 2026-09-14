---
title: Funciones de retrollamada de eventos
source_url: https://www.php.net/manual/es/event.callbacks.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/event.callbacks.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: a47dff201
order: 18960
---

## Funciones de retrollamada de eventos

Si una función de retrollamada está registrada para un evento, será llamada cuando el evento se active. Para asociar una función de retrollamada con un evento, se debe pasar con un tipo `callable` al método Event::\_\_construct, Event::set, o cualquier otro método factorial como Event::timer.

Una función de retrollamada de evento debe corresponder al siguiente prototipo:

```php
callback([mixed $fd], [int $what], [mixed $arg]): void
```php

`fd`  
Un descriptor de fichero, un recurso de flujo, o un socket asociado con el evento. Para los eventos de tipo señal, `fd` corresponde al número de la señal.

`what`  
Máscara de bits de *todos* los eventos lanzados.

`arg`  
Datos de usuario personalizados.

El método Event::timer espera una función de retrollamada que corresponda al siguiente prototipo:

```php
callback([mixed $arg]): void
```

`arg`  
Datos de usuario personalizados.

El método Event::signal espera una función de retrollamada que corresponda al siguiente prototipo:

```php
callback([int $signum], [mixed $arg]): void
```php

`signum`  
El número de la señal lanzada (i.e. `SIGTERM`).

`arg`  
Datos de usuario personalizados.
