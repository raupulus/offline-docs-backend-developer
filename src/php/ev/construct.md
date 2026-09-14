---
title: EvCheck::__construct
description: Construye el objeto de observación EvCheck
source_url: https://www.php.net/manual/es/evcheck.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evcheck/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 17940
---

EvCheck::\_\_construct

Construye el objeto de observación EvCheck

## Descripción

```php
public EvCheck::__construct(callable $callback, [mixed $data], [int $priority])
```php

Construye el objeto de observación `EvCheck`.

## Parámetros

`callback`  
Ver las [retrollamadas de las observaciones](#ev.watcher-callbacks).

`data`  
Datos personalizados asociados con el observador.

`priority`  
[Prioridad del observador](#ev.constants.watcher-pri)

## Véase también

EvPrepare

EvLoop::check
