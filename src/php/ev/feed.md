---
title: EvWatcher::feed
description: Alimenta los revents proporcionados en el bucle de eventos
source_url: https://www.php.net/manual/es/evwatcher.feed.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evwatcher/feed.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18670
---

EvWatcher::feed

Alimenta los revents proporcionados en el bucle de eventos

## Descripción

```php
public EvWatcher::feed(int $revents): void
```php

Alimenta los revents proporcionados en el bucle de eventos, como si el evento especificado hubiera ocurrido en el observador.

## Parámetros

`revents`  
Máscara de bits del observador [de recepción de eventos](#ev.constants.watcher-revents).

## Valores devueltos

No se retorna ningún valor.
