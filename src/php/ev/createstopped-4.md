---
title: EvFork::createStopped
description: Crea una instancia detenida de la clase observadora EvFork
source_url: https://www.php.net/manual/es/evfork.createstopped.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evfork/createstopped.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18070
---

EvFork::createStopped

Crea una instancia detenida de la clase observadora EvFork

## Descripción

```php
final public static EvFork::createStopped(string $callback, [string $data], [string $priority]): object
```php

Idéntico al método EvFork::\_\_construct pero no inicia automáticamente el observador.

## Parámetros

`callback`  
Ver las [retrollamadas de observadores](#ev.watcher-callbacks).

`data`  
Datos personalizados asociados con el observador.

`priority`  
[Prioridad de observador](#ev.constants.watcher-pri)

## Valores devueltos

Devuelve un objeto EvFork (detenido) en caso de éxito.

## Véase también

EvFork::\_\_construct
