---
title: ps_setlinewidth
description: Establecer el ancho de una línea
source_url: https://www.php.net/manual/es/function.ps-setlinewidth.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-setlinewidth.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 66130
---

ps_setlinewidth

Establecer el ancho de una línea

## Descripción

```php
ps_setlinewidth(resource $psdoc, float $width): bool
```php

Esteblece el ancho de línea para todas las operaciones de dibujo siguientes.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`width`  
El ancho de las líneas en puntos.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_setlinecap`, `ps_setlinejoin`, `ps_setmiterlimit`
