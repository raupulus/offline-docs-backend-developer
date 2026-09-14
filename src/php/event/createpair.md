---
title: EventBufferEvent::createPair
description: Crea dos eventos de buffer conectados entre sí
source_url: https://www.php.net/manual/es/eventbufferevent.createpair.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbufferevent/createpair.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: a47dff201
order: 19420
---

EventBufferEvent::createPair

Crea dos eventos de buffer conectados entre sí

## Descripción

```php
public static EventBufferEvent::createPair(EventBase $base, [int $options]): array
```php

Devuelve un array de dos objetos `EventBufferEvent` conectados entre sí. Todas las opciones habituales son soportadas, salvo `EventBufferEvent::OPT_CLOSE_ON_FREE` que no tiene ningún efecto, y `EventBufferEvent::OPT_DEFER_CALLBACKS` que siempre está activado.

## Parámetros

`base`  
Evento base asociado.

`options`  
Constantes [EventBufferEvent::OPT\_\*](#) combinadas con el operador `OR`.

## Valores devueltos

Devuelve un array de dos objetos `EventBufferEvent` conectados entre sí.

## Historial de cambios

| Versión          | Descripción                  |
|------------------|------------------------------|
| PECL event 1.9.0 | El método es ahora estático. |
