---
title: ps_closepath_stroke
description: Cerrar y contornear un trazado
source_url: https://www.php.net/manual/es/function.ps-closepath-stroke.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-closepath-stroke.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 65690
---

ps_closepath_stroke

Cerrar y contornear un trazado

## Descripción

```php
ps_closepath_stroke(resource $psdoc): bool
```php

Conecta el último punto con el primer punto de un trazado y dibuja la línea cerrada resultante.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_closepath`
