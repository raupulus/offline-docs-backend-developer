---
title: inotify_read
description: Lee eventos de una instancia inotify
source_url: https://www.php.net/manual/es/function.inotify-read.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/inotify/functions/inotify-read.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: inotify
translation_status: ready
translation_revision: ab6d54b20
order: 39330
---

inotify_read

Lee eventos de una instancia inotify

## Descripción

```php
inotify_read(resource $inotify_instance): array
```php

Leer eventos inotify de una instancia inotify.

## Parámetros

`inotify_instance`  
Recurso retornado por `inotify_init`

## Valores devueltos

Un array de eventos inotify o `false` si no hay eventos pendientes e `inotify_instance` no es de bloqueo. Cada evento es un array con las siguientes claves: wd es un descriptor de seguimiento devuelto por `inotify_add_watch`, mask es una máscara de bits de [eventos](#inotify.constants), cookie es un identificador único para conectar los eventos relacionados (por ejemplo: `IN_MOVE_FROM` e `IN_MOVE_TO`), name es el nombre de un fichero (por ejemplo: si un fichero se ha modificado en un directorio observado)

## Véase también

inotify_init

stream_select

stream_set_blocking

inotify_queue_len
