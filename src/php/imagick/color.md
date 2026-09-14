---
title: ImagickDraw::color
description: Dibuja un color sobre una imagen
source_url: https://www.php.net/manual/es/imagickdraw.color.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/color.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: e4ec40195
order: 36210
---

ImagickDraw::color

Dibuja un color sobre una imagen

## Descripción

```php
public ImagickDraw::color(float $x, float $y, int $paint): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Dibuja un color sobre una imagen, con el color de relleno actual, comenzando en una posición dada, y utilizando el método de coloración indicado.

## Parámetros

`x`  
Abscisa del punto de pintura

`y`  
Ordenada del punto de pintura

`paint`  
Una de las constantes [PAINT](#imagick.constants.paint) (`imagick::PAINT_*`).

## Valores devueltos

No se retorna ningún valor.
