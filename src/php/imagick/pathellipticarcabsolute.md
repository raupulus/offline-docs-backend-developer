---
title: ImagickDraw::pathEllipticArcAbsolute
description: Dibuja un arco de elipse, en coordenadas absolutas
source_url: https://www.php.net/manual/es/imagickdraw.pathellipticarcabsolute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/pathellipticarcabsolute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: e4ec40195
order: 36690
---

ImagickDraw::pathEllipticArcAbsolute

Dibuja un arco de elipse, en coordenadas absolutas

## Descripción

```php
public ImagickDraw::pathEllipticArcAbsolute(float $rx, float $ry, float $x_axis_rotation, bool $large_arc, bool $sweep, float $x, float $y): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Dibuja un arco de elipse a partir del punto actual (`x`, `y`), utilizando coordenadas relativas. El tamaño y la orientación de la elipse se definen mediante dos radios, (`rx`, `ry`) y una rotación xAxisRotation, que indica cómo la elipse, en su conjunto, está situada en el sistema de coordenadas. El centro (`cx`, `cy`) de la elipse se calcula automáticamente para satisfacer las restricciones de los demás parámetros. Si `large_arc` es `true`, entonces se dibuja el arco más grande. Si `sweep` es `true`, entonces el dibujo del arco se realiza en sentido horario.

## Parámetros

`rx`  
Radio X

`ry`  
Radio Y

`x_axis_rotation`  
Rotación sobre el eje X

`large_arc`  
Opción de `large_arc_flag`

`sweep`  
Opción `sweep_flag`

`x`  
La abscisa

`y`  
La ordenada

## Valores devueltos

No se retorna ningún valor.
