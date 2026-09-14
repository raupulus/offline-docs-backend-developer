---
title: ps_rect
description: Dibujar un rectángulo
source_url: https://www.php.net/manual/es/function.ps-rect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-rect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 330a38c4d
order: 65940
---

ps_rect

Dibujar un rectángulo

## Descripción

```php
ps_rect(resource $psdoc, float $x, float $y, float $width, float $height): bool
```php

Dibuja un rectángulo con su esquina inferior izquierda en (`x`, `y`). El rectángulo comienza y finaliza en su esquina inferior izquierda. Si se llama a esta función fuera de un trazado iniciará un nuevo trazado. Se es llamada dentro de un trazado añadirá el rectángulo como un subtrazado. Si la última operación de dibujo no finaliza en la esquina inferior izquierda, existirá un hueco en el trazado.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`x`  
La coordenada x de la esquina inferior izquierda del rectángulo.

`y`  
La coordenada y de la esquina inferior izquierda del rectángulo.

`width`  
El ancho de la imagen.

`height`  
El alto de la imagen.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_arc`, `ps_circle`, `ps_lineto`
