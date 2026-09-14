---
title: Event::pending
description: Detecta si el evento está pendiente o programado
source_url: https://www.php.net/manual/es/event.pending.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/event/pending.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 18900
---

Event::pending

Detecta si el evento está pendiente o programado

## Descripción

```php
public Event::pending(int $flags): bool
```php

Detecta si el evento está pendiente o programado.

## Parámetros

`flags`  
Una o más de las siguientes constantes: `Event::READ`, `Event::WRITE`, `Event::TIMEOUT`, `Event::SIGNAL`.

## Valores devueltos

Devuelve `true` si el evento está pendiente o programado, `false` en caso contrario.
