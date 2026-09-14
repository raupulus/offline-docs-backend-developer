---
title: msg_get_queue
description: Crea o se adhiere a una cola de mensajes
source_url: https://www.php.net/manual/es/function.msg-get-queue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sem/functions/msg-get-queue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sem
translation_status: ready
translation_reviewed: true
translation_revision: fd2f14b2e
order: 73450
---

msg_get_queue

Crea o se adhiere a una cola de mensajes

## Descripción

```php
msg_get_queue(int $key, [int $permissions]): SysvMessageQueue
```php

`msg_get_queue` devuelve un recurso que puede ser utilizado con las colas de mensajes System V y la clave `key`. La primera llamada a la función va a crear la cola de mensajes, con los permisos opcionales de `permissions`. Una segunda llamada a `msg_get_queue` con la misma clave `key` devolverá otro recurso de cola de mensajes, pero los dos identificadores conducen a la misma cola de mensajes.

## Parámetros

`key`  
Identificador numérico de la cola de mensajes.

`permissions`  
Permisos en la cola. Por omisión, vale 0666. Si la cola de mensajes ya existe, el argumento `permissions` será ignorado.

## Valores devueltos

Devuelve un recurso que puede ser utilizado para acceder a la cola de mensajes System V. Devuelve una instancia de `SysvMessageQueue` que puede ser utilizada para acceder a la cola de mensajes System V, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | En caso de éxito, esta función devuelve una instancia de `SysvMessageQueue` ahora; anteriormente, se devolvía un `resource`. |

## Véase también

msg_remove_queue

msg_receive

msg_send

msg_stat_queue

msg_set_queue
