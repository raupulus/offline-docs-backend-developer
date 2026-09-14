---
title: EventBufferEvent::free
description: Libera un evento de búfer
source_url: https://www.php.net/manual/es/eventbufferevent.free.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbufferevent/free.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 19450
---

EventBufferEvent::free

Libera un evento de búfer

## Descripción

```php
public EventBufferEvent::free(): void
```php

Libera todos los recursos asignados por un evento de búfer.

Generalmente, no es necesario llamar a este método, ya que normalmente, la liberación total de los recursos asociados se realiza en los destructores internos del objeto. Sin embargo, puede ocurrir que un script largo asigne muchas instancias, o bien que un script utilice una gran cantidad de memoria; en estos casos, puede ser necesario liberar los recursos lo más rápido posible. Asimismo, el uso del método EventBufferEvent::free puede ser útil para proteger la ejecución del script de alcanzar el valor de `memory_limit`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.
