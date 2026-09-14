---
title: Event::set
description: Reconfigurar el evento
source_url: https://www.php.net/manual/es/event.set.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/event/set.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 18910
---

Event::set

Reconfigurar el evento

## Descripción

```php
public Event::set(EventBase $base, mixed $fd, [int $what], [callable $cb], [mixed $arg]): bool
```php

Reconfigurar el evento. Téngase en cuenta que esta función no llama a la función obsoleta event_set de libevent. En su lugar, llama a la función event_assign.

## Parámetros

`base`  
La base de evento a asociar.

`fd`  
Un recurso de flujo, un recurso de socket, o un descriptor numérico de fichero. Para los eventos de tipo temporizador pase `-1`. Para los eventos de tipo señal pase el número de la señal, por ejemplo `SIGHUP`.

`what`  
Ver los [flags de eventos](#event.flags).

`cb`  
La función de retrollamada del evento. Ver las [funciones de retrollamada de eventos](#event.callbacks).

`arg`  
Datos personalizados a asociar con el evento. Serán pasados a la función de retrollamada cuando el evento se active.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
