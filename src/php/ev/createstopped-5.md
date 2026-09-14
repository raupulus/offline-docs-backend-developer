---
title: EvIdle::createStopped
description: Crea una instancia de un objeto observador EvIdle
source_url: https://www.php.net/manual/es/evidle.createstopped.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evidle/createstopped.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18100
---

EvIdle::createStopped

Crea una instancia de un objeto observador EvIdle

## Descripción

```php
final public static EvIdle::createStopped(string $callback, [mixed $data], [int $priority]): object
```php

Idéntico al método EvIdle::\_\_construct pero no inicia automáticamente el observador.

## Parámetros

`callback`  
Ver las [retrollamadas de los observadores](#ev.watcher-callbacks).

`data`  
Datos personalizados con el observador.

`priority`  
[Prioridad del observador](#ev.constants.watcher-pri)

## Valores devueltos

Devuelve un objeto EvIdle en caso de éxito.

## Véase también

EvIdle::\_\_construct

EvLoop::idle
