---
title: EvLoop::stop
description: Detiene el bucle de eventos
source_url: https://www.php.net/manual/es/evloop.stop.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evloop/stop.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18350
---

EvLoop::stop

Detiene el bucle de eventos

## Descripción

```php
public EvLoop::stop([int $how]): void
```php

Detiene el bucle de eventos.

## Parámetros

`how`  
Una [constante](#ev.constants.break-flags) *Ev::BREAK\_\**.

## Valores devueltos

No se retorna ningún valor.

## Véase también

EvLoop::run

Ev::stop
