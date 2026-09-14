---
title: EvLoop::loopFork
description: Debe ser llamado después de un fork
source_url: https://www.php.net/manual/es/evloop.loopfork.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evloop/loopfork.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18260
---

EvLoop::loopFork

Debe ser llamado después de un fork

## Descripción

```php
public EvLoop::loopFork(): void
```php

Debe ser llamado después de un *fork* en el hijo, y antes de entrar o continuar el bucle de eventos. Una alternativa es utilizar la constante `Ev::FLAG_FORKCHECK` que llama a esta función automáticamente, con una pérdida de rendimiento (consulte la [documentación libev](http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#FUNCTIONS_CONTROLLING_EVENT_LOOPS)).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.
