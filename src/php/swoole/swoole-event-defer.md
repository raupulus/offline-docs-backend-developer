---
title: swoole_event_defer
description: Añade una retrollamada a la próxima iteración del bucle de eventos
source_url: https://www.php.net/manual/es/function.swoole-event-defer.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/functions/swoole-event-defer.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_revision: 17623bf36
order: 90510
---

swoole_event_defer

Añade una retrollamada a la próxima iteración del bucle de eventos

## Descripción

```php
swoole_event_defer(callable $callback): bool
```php

## Parámetros

`callback`  

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
