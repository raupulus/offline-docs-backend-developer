---
title: Los flags de eventos
source_url: https://www.php.net/manual/es/event.flags.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/event.flags.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 18980
---

## Los flags de eventos

`Event::READ` Este flag indica que el evento se activa cuando el descriptor de fichero proporcionado (generalmente un recurso de flujo o un socket) está listo para ser leído.

`Event::WRITE` Este flag indica que el evento se activa cuando el descriptor de fichero proporcionado (generalmente un recurso de flujo o un socket) está listo para ser leído.

`Event::SIGNAL` Este flag se utiliza para implementar la detección de señales. Ver la creación de un evento de tipo señal a continuación.

`Event::TIMEOUT` Este flag indica que el evento se activa después de la expiración de un tiempo límite. El flag `Event::TIMEOUT` se ignora durante la construcción de un evento: un tiempo límite puede ser definido al *añadir* el evento, o no. Se define en el argumento `$what` de la función de retrollamada cuando se alcanza el tiempo límite.

Ver también [ la programación de red fácil, portable y no bloqueante con Libevent; los trabajos con los eventos y sus flags](http://www.wangafu.net/~nickm/libevent-book/Ref4_event.html#_the_event_flags)
