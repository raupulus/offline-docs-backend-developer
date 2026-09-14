---
title: ImagickDraw::pathCurveToAbsolute
description: Dibuja una curva de Bézier cúbica, en coordenadas absolutas
source_url: https://www.php.net/manual/es/imagickdraw.pathcurvetoabsolute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/pathcurvetoabsolute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: fa0c88f1e
order: 36610
---

ImagickDraw::pathCurveToAbsolute

Dibuja una curva de Bézier cúbica, en coordenadas absolutas

## Descripción

```php
public ImagickDraw::pathCurveToAbsolute(float $x1, float $y1, float $x2, float $y2, float $x, float $y): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Dibuja una curva de Bézier cúbica, a partir del punto actual (`x`,`y`) utilizando el punto (`x1`,`y1`) como punto de control al inicio de la curva y (`x2`,`y2`) como punto de control al final de la curva, utilizando coordenadas absolutas. Al final de la orden, el nuevo punto actual es el punto final (`x`,`y`), utilizado por el polybezier.

## Parámetros

`x1`  
Abscisa del primer punto de control

`y1`  
Ordenada del primer punto de control

`x2`  
Abscisa del segundo punto de control

`y2`  
Ordenada del segundo punto de control

`x`  
Abscisa del final de la curva

`y`  
Ordenada del final de la curva

## Valores devueltos

No se retorna ningún valor.
