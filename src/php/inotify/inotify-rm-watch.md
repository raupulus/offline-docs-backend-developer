---
title: inotify_rm_watch
description: Elimina un seguimiento existente de una instancia inotify
source_url: https://www.php.net/manual/es/function.inotify-rm-watch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/inotify/functions/inotify-rm-watch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: inotify
translation_status: ready
translation_revision: ab6d54b20
order: 39340
---

inotify_rm_watch

Elimina un seguimiento existente de una instancia inotify

## Descripción

```php
inotify_rm_watch(resource $inotify_instance, int $watch_descriptor): bool
```php

`inotify_rm_watch` elimina el seguimiento `watch_descriptor` de la instancia inotify `inotify_instance`.

## Parámetros

`inotify_instance`  
Recurso retornado por `inotify_init`

`watch_descriptor`  
Seguimiento a eliminar de la instancia

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

inotify_init
