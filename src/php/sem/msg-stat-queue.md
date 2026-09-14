---
title: msg_stat_queue
description: Devuelve información sobre la cola de mensajes
source_url: https://www.php.net/manual/es/function.msg-stat-queue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sem/functions/msg-stat-queue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sem
translation_status: ready
translation_reviewed: true
translation_revision: fd2f14b2e
order: 73510
---

msg_stat_queue

Devuelve información sobre la cola de mensajes

## Descripción

```php
msg_stat_queue(SysvMessageQueue $queue): array
```php

`msg_stat_queue` devuelve información sobre la cola de mensajes identificada por `queue`. Es una función práctica para conocer el proceso que emitió el mensaje que acaba de ser recibido.

## Parámetros

`queue`  
La cola de mensajes

## Valores devueltos

El valor devuelto por la función es un array cuyos índices y valores son los siguientes :

|  |  |
|----|----|
| `msg_perm.uid` | El uid del propietario de la cola. |
| `msg_perm.gid` | El gid del propietario de la cola. |
| `msg_perm.mode` | El modo de acceso a la cola. |
| `msg_stime` | La hora del último mensaje enviado a la cola. |
| `msg_rtime` | La hora del último mensaje emitido por la cola. |
| `msg_ctime` | La hora de modificación de la cola. |
| `msg_qnum` | El número de mensajes en espera en la cola. |
| `msg_qbytes` | El número máximo de bytes autorizados en un mensaje de la cola de espera. En Linux, este valor puede ser leído y modificado a través del archivo `/proc/sys/kernel/msgmnb`. |
| `msg_lspid` | El pid del proceso que envió el último mensaje a la cola. |
| `msg_lrpid` | El pid del proceso que recibió el último mensaje de la cola. |

Estructura de respuesta de `msg_stat_queue`

Devuelve `false` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `queue` ahora espera una `SysvMessageQueue`; anteriormente, se esperaba un `resource`. |

## Véase también

msg_remove_queue

msg_receive

msg_get_queue

msg_set_queue
