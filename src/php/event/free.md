---
title: Event::free
description: Elimina un evento de la lista de eventos vigilados y libera los recursos
  asociados
source_url: https://www.php.net/manual/es/event.free.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/event/free.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 18880
---

Event::free

Elimina un evento de la lista de eventos vigilados y libera los recursos asociados

## Descripción

```php
public Event::free(): void
```php

Elimina un evento de la lista de eventos vigilados por libevent y libera los recursos asignados a ese evento.

> [!WARNING]
> El método Event::free no destruye actualmente el objeto en sí. Para destruir el objeto completamente, llame a la función `unset` o asigne el valor `null`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Véase también

Event::\_\_construct
