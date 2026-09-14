---
title: ImagickDraw::pathCurveToSmoothAbsolute
description: Dibuja una curva de Bézier, en coordenadas absolutas
source_url: https://www.php.net/manual/es/imagickdraw.pathcurvetosmoothabsolute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/pathcurvetosmoothabsolute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: fa0c88f1e
order: 36670
---

ImagickDraw::pathCurveToSmoothAbsolute

Dibuja una curva de Bézier, en coordenadas absolutas

## Descripción

```php
public ImagickDraw::pathCurveToSmoothAbsolute(float $x2, float $y2, float $x, float $y): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Dibuja una curva de Bézier, en coordenadas absolutas, a partir del punto actual (`x`,`y`). El primer punto de control es la reflexión del segundo punto de control del comando anterior, relativo al punto actual. Si no ha habido un comando anterior, o si el comando anterior no era DrawPathCurveToAbsolute, DrawPathCurveToRelative, DrawPathCurveToSmoothAbsolute o DrawPathCurveToSmoothRelative, se asume entonces que el primer punto de control coincide con el punto actual. (`x2`,`y2`) es el segundo punto de control (es decir, el punto de control al final de la línea. Al final del comando, el nuevo punto actual es el punto final, de coordenadas (`x`,`y`), en el polybezier.

## Parámetros

`x2`  
abscisa del segundo punto de control

`y2`  
ordenada del segundo punto de control

`x`  
abscisa del punto de control final

`y`  
ordenada del punto de control final

## Valores devueltos

No se retorna ningún valor.
