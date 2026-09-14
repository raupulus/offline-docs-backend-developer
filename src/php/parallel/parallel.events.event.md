---
title: La clase parallel\Events\Event
source_url: https://www.php.net/manual/es/class.parallel-events-event.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parallel/parallel.events.event.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parallel
translation_status: ready
translation_reviewed: false
translation_revision: 57c7669a1
order: 60290
---

## Objeto de evento

Cuando un evento es devuelto, `Event::$object` debe ser retirado del bucle que lo devolvió. Si el evento es un evento de escritura, el `Input` para `Event::$source` también debe ser retirado.

## Sinopsis de la clase

parallel\Events\Event

final

parallel\Events\Event

Debe ser una de las constantes

Event\Type

public

int

type

Debe ser la fuente del evento (nombre del objetivo)

public

string

source

Debe ser un Future o un Channel

public

object

object

Debe definir los eventos de lectura/Error

public

value
