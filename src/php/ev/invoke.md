---
title: EvWatcher::invoke
description: Invoca la función de retrollamada del observador con el mascara de bits
  de los eventos recibidos proporcionados
source_url: https://www.php.net/manual/es/evwatcher.invoke.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evwatcher/invoke.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18690
---

EvWatcher::invoke

Invoca la función de retrollamada del observador con el mascara de bits de los eventos recibidos proporcionados

## Descripción

```php
public EvWatcher::invoke(int $revents): void
```php

Invoca la función de retrollamada del observador con el mascara de bits de los eventos recibidos proporcionados.

## Parámetros

`revents`  
Mascara de bits del observador [que recibe los eventos](#ev.constants.watcher-revents).

## Valores devueltos

No se retorna ningún valor.
