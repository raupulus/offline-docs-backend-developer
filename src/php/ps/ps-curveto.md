---
title: ps_curveto
description: Dibujar una curva
source_url: https://www.php.net/manual/es/function.ps-curveto.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-curveto.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 14af302c9
order: 65720
---

ps_curveto

Dibujar una curva

## Descripción

```php
ps_curveto(resource $psdoc, float $x1, float $y1, float $x2, float $y2, float $x3, float $y3): bool
```php

Añade una sección de una curva cúbica de Bézier al trazado actual descrita por los tres puntos de control dados.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`x1`  
La coordenada x del primer punto de control.

`y1`  
La coordenada y del primer punto de control.

`x2`  
La coordenada x del segundo punto de control.

`y2`  
La coordenada y del segundo punto de control.

`x3`  
La coordenada x del tercer punto de control.

`y3`  
La coordenada y del tercer punto de control.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_lineto`
