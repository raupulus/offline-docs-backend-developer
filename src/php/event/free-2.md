---
title: EventBase::free
description: Libera los recursos asignados para el evento base
source_url: https://www.php.net/manual/es/eventbase.free.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbase/free.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 19040
---

EventBase::free

Libera los recursos asignados para el evento base

## Descripción

```php
public EventBase::free(): void
```php

Libera los recursos asignados por libevent para el objeto `EventBase`.

> [!WARNING]
> El método EventBase::free no destruye el objeto mismo. Para destruir el objeto completamente, llame a la función `unset` o asignele el valor `null`.
>
> Este método no libera, ni desasocia ningún evento que esté actualmente asociado con el objeto `EventBase`, ni cierra ninguno de sus sockets; tenga esto en cuenta.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Véase también

EventBase::\_\_construct
