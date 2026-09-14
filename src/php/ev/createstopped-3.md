---
title: EvEmbed::createStopped
description: Crea un objeto EvEmbed watcher detenido
source_url: https://www.php.net/manual/es/evembed.createstopped.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evembed/createstopped.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18020
---

EvEmbed::createStopped

Crea un objeto EvEmbed watcher detenido

## Descripción

```php
final public static EvEmbed::createStopped(object $other, [callable $callback], [mixed $data], [int $priority]): void
```php

Idéntico al método EvEmbed::\_\_construct, pero no inicia automáticamente el watcher.

## Parámetros

`other`  
Idéntico al argumento del método EvEmbed::\_\_construct

`callback`  
Ver las [retrollamadas de los Watcher](#ev.watcher-callbacks).

`data`  
Datos personalizados para asociar con el watcher.

`priority`  
[Prioridad del Watcher](#ev.constants.watcher-pri)

## Valores devueltos

Retorna un objeto EvEmbed detenido en caso de éxito.

## Véase también

EvEmbed::\_\_construct

Ev::embeddableBackends
