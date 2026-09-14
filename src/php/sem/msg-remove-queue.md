---
title: msg_remove_queue
description: Destruye una cola de mensajes
source_url: https://www.php.net/manual/es/function.msg-remove-queue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sem/functions/msg-remove-queue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sem
translation_status: ready
translation_reviewed: true
translation_revision: fd2f14b2e
order: 73480
---

msg_remove_queue

Destruye una cola de mensajes

## Descripción

```php
msg_remove_queue(SysvMessageQueue $queue): bool
```php

`msg_remove_queue` destruye la cola de mensajes identificada por `queue`. Únicamente debe utilizarse esta función cuando todos los procesos hayan finalizado su trabajo en la cola de mensajes, y se desee liberar los recursos.

## Parámetros

`queue`  
La cola de mensajes

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `queue` ahora requiere una `SysvMessageQueue`; anteriormente se esperaba un `resource`. |

## Véase también

msg_get_queue

msg_receive

msg_stat_queue

msg_set_queue
