---
title: ps_clip
description: Realizar un recorte utilizando el trazado actual
source_url: https://www.php.net/manual/es/function.ps-clip.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-clip.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 65660
---

ps_clip

Realizar un recorte utilizando el trazado actual

## Descripción

```php
ps_clip(resource $psdoc): bool
```php

Toma el trazado actual y lo usa para definir el borde de un área de recorte. Todo lo dibujado fuera de ese área no será visible.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_closepath`
