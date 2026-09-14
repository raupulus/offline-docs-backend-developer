---
title: EventBase::exit
description: Detiene el envío de los eventos
source_url: https://www.php.net/manual/es/eventbase.exit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbase/exit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_revision: da9d81816
order: 19030
---

EventBase::exit

Detiene el envío de los eventos

## Descripción

```php
public EventBase::exit([float $timeout]): bool
```php

Le indica al evento base que pare el envío de los eventos, opcionamente después de un número de segundos dado.

## Parámetros

`timeout`  
Número opcional de segundos después de los cuales el evento base deberá parar el envío de eventos.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

EventBase::stop
