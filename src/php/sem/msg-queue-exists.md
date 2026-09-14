---
title: msg_queue_exists
description: Verificar si una cola de mensajes existe
source_url: https://www.php.net/manual/es/function.msg-queue-exists.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sem/functions/msg-queue-exists.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sem
translation_status: ready
translation_revision: fd2f14b2e
order: 73460
---

msg_queue_exists

Verificar si una cola de mensajes existe

## Descripción

```php
msg_queue_exists(int $key): bool
```php

Verifica si la clave dada por el parámetro `key` de la cola de mensajes existe.

## Parámetros

`key`  
La clave de la cola.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

msg_remove_queue

msg_receive

msg_stat_queue
