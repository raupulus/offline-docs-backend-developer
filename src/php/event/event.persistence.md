---
title: Acerca de la persistencia de eventos
source_url: https://www.php.net/manual/es/event.persistence.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/event.persistence.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 18990
---

## Acerca de la persistencia de eventos

Por omisión, tan pronto como un evento pendiente se vuelve activo (porque su descriptor de fichero está listo para ser leído o escrito, o porque su tiempo de espera máximo ha sido alcanzado), ya no está pendiente una vez que su función de retrollamada es ejecutada. Asimismo, para volver a poner el evento en estado pendiente, una manera es llamar al método Event::add en la función de retrollamada.

Si el flag `Event::PERSIST` está definido en el evento, entonces es *persistente*. Esto significa que el evento permanece en estado pendiente incluso cuando su función de retrollamada es activada. El método Event::del puede ser llamado para pasarlo a estado no pendiente.

El tiempo de espera máximo en un evento persistente es reinicializado tan pronto como su función de retrollamada es ejecutada. Así, si un evento tiene los flags `Event::READ` `|` `Event::PERSIST` y un tiempo de espera fijado a 5 segundos, el evento se vuelve activo:

1.  Cuando el socket o el descriptor de fichero está listo para la lectura.

2.  Cuando han pasado 5 segundos desde la última activación del evento.

Ver también [ la programación de red rápida, portable y no bloqueante con Libevent; Acerca de los eventos persistentes](http://www.wangafu.net/~nickm/libevent-book/Ref4_event.html#_about_event_persistence)
