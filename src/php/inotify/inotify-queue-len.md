---
title: inotify_queue_len
description: Devuelve un número superior a cero si hay eventos pendientes
source_url: https://www.php.net/manual/es/function.inotify-queue-len.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/inotify/functions/inotify-queue-len.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: inotify
translation_status: ready
translation_revision: ab6d54b20
order: 39320
---

inotify_queue_len

Devuelve un número superior a cero si hay eventos pendientes

## Descripción

```php
inotify_queue_len(resource $inotify_instance): int
```php

Esta función permite saber si `inotify_read` bloqueará o no. Si un número superior a cero es devuelto, hay eventos pendientes e `inotify_read` no bloqueará.

## Parámetros

`inotify_instance`  
Recurso retornado por `inotify_init`

## Valores devueltos

Devuelve un número superior a cero si hay eventos pendientes.

## Véase también

inotify_init

stream_select

stream_set_blocking
