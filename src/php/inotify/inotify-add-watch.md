---
title: inotify_add_watch
description: Añade un punto de vigilancia a una instancia inotify
source_url: https://www.php.net/manual/es/function.inotify-add-watch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/inotify/functions/inotify-add-watch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: inotify
translation_status: ready
translation_reviewed: false
translation_revision: ab6d54b20
order: 39300
---

inotify_add_watch

Añade un punto de vigilancia a una instancia inotify

## Descripción

```php
inotify_add_watch(resource $inotify_instance, string $pathname, int $mask): int
```php

`inotify_add_watch` añade un punto de vigilancia a una instancia inotify o modifica un punto de vigilancia en curso hacia un nuevo fichero o directorio especificado por la ruta `pathname`.

Utilizar `inotify_add_watch` sobre un objeto ya en vigilancia modifica la configuración. Utilizar la constante `IN_MASK_ADD` añade los eventos (operación OR lógica).

## Parámetros

`inotify_instance`  
Recurso retornado por `inotify_init`

`pathname`  
Fichero o directorio a vigilar.

`mask`  
Eventos a vigilar. Véase [Constantes predefinidas](#inotify.constants).

## Valores devueltos

El valor devuelto es un puntero inotify único (inotify instance wide), o `false` si ocurre un error.

## Véase también

inotify_init
