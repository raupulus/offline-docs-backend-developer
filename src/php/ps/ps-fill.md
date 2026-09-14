---
title: ps_fill
description: Rellenar el trazado actual
source_url: https://www.php.net/manual/es/function.ps-fill.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-fill.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 65780
---

ps_fill

Rellenar el trazado actual

## Descripción

```php
ps_fill(resource $psdoc): bool
```php

Rellena el trazaco construido previamente con llamdas a las funciones de dibujo, como `ps_lineto`.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_fill_stroke`, `ps_stroke`
