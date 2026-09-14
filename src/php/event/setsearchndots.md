---
title: EventDnsBase::setSearchNdots
description: Define el parámetro 'ndots' para las búsquedas
source_url: https://www.php.net/manual/es/eventdnsbase.setsearchndots.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventdnsbase/setsearchndots.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: f80105b4f
order: 19820
---

EventDnsBase::setSearchNdots

Define el parámetro 'ndots' para las búsquedas

## Descripción

```php
public EventDnsBase::setSearchNdots(int $ndots): bool
```php

Define el parámetro `'ndots'` para las búsquedas. Define el número de puntos que, cuando se encuentran en un nombre, hace que la primera solicitud se realice sin búsqueda de dominio.

## Parámetros

`ndots`  
El número de puntos.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
