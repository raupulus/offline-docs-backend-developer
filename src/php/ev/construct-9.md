---
title: EvPrepare::__construct
description: Construye un objeto watcher EvPrepare
source_url: https://www.php.net/manual/es/evprepare.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evprepare/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: dfd68fd22
order: 18460
---

EvPrepare::\_\_construct

Construye un objeto watcher EvPrepare

## Descripción

```php
public EvPrepare::__construct(string $callback, [string $data], [string $priority])
```php

Construye un objeto watcher EvPrepare. Inicia el watcher automáticamente. Si se necesita un watcher detenido, se debe utilizar el método EvPrepare::createStopped.

## Parámetros

`callback`  
Ver las [retrollamadas de los Watchers](#ev.watcher-callbacks).

`data`  
Datos personalizados para asociar con el watcher.

`priority`  
[Prioridad del Watcher](#ev.constants.watcher-pri)

## Véase también

EvCheck
