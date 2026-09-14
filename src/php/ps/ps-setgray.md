---
title: ps_setgray
description: Establecer el valor de gris
source_url: https://www.php.net/manual/es/function.ps-setgray.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-setgray.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 66100
---

ps_setgray

Establecer el valor de gris

## Descripción

```php
ps_setgray(resource $psdoc, float $gray): bool
```php

Establece el valor de gris para todas las operaciones de dibujo siguientes.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`gray`  
El valor debe estar entre 0 (blanco) and 1 (negro).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_setcolor`
