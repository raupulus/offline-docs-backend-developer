---
title: msg_set_queue
description: Modifica información en la cola de mensajes
source_url: https://www.php.net/manual/es/function.msg-set-queue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sem/functions/msg-set-queue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sem
translation_status: ready
translation_reviewed: true
translation_revision: fd2f14b2e
order: 73500
---

msg_set_queue

Modifica información en la cola de mensajes

## Descripción

```php
msg_set_queue(SysvMessageQueue $queue, array $data): bool
```php

`msg_set_queue` permite modificar ciertos valores como msg_perm.uid, msg_perm.gid, msg_perm.mode y msg_qbytes, que son campos de la estructura que alberga la cola de mensajes.

Modificar la estructura de datos requiere que PHP funcione con el mismo usuario que aquel que creó la cola, que posee la cola (como se determina por los campos msg_perm.xxx), o que funcione con los derechos de superusuario. Los derechos de superusuario son necesarios para asignar a msg_qbytes valores superiores a los límites del sistema.

## Parámetros

`queue`  
La cola de mensajes

`data`  
Deben especificarse los valores deseados definiendo el valor de las claves que se quieren recuperar en el array `data`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `queue` ahora espera una `SysvMessageQueue`; anteriormente, se esperaba un `resource`. |

## Véase también

msg_remove_queue

msg_receive

msg_stat_queue

msg_get_queue
