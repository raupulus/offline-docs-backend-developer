---
title: parallel\Events::poll
description: Interroga
source_url: https://www.php.net/manual/es/parallel-events.poll.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parallel/parallel/events/poll.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parallel
translation_status: ready
translation_reviewed: false
translation_revision: 57c7669a1
order: 60050
---

parallel\Events::poll

Interroga

## Descripción

```php
public parallel\Events::poll(): parallel\Events\Event
```php

Interroga para el próximo evento.

## Valores devueltos

Si no quedan más objetivos, `null` será devuelto.

Esto es un bucle no bloqueante, y si se produce un bloqueo, `null` será devuelto.

De lo contrario, el `parallel\Events\Event` devuelto describe el evento.

## Excepciones

> [!WARNING]
> Lanza una `parallel\Events\Error\Existence` si se supera el tiempo de espera.
