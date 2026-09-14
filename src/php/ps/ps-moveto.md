---
title: ps_moveto
description: Establecer el punto actual
source_url: https://www.php.net/manual/es/function.ps-moveto.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-moveto.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 65870
---

ps_moveto

Establecer el punto actual

## Descripción

```php
ps_moveto(resource $psdoc, float $x, float $y): bool
```php

Establece el punto actual a unas coordenadas nuevas. Si esta es la primera llamada a la función `ps_moveto` después de haber finalizado un trazado previo, se iniciará un nuevo trazado. Si esta función es llamada en mitad de un trazado establecerá el punto actual e iniciará un subtrazado.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`x`  
La coordenada x del punto al que moverse.

`y`  
La coordenada y del punto al que moverse.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_lineto`
