---
title: GmagickDraw::roundrectangle
description: Dibuja un rectángulo redondeado
source_url: https://www.php.net/manual/es/gmagickdraw.roundrectangle.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagickdraw/roundrectangle.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_revision: 35752f072
order: 28080
---

GmagickDraw::roundrectangle

Dibuja un rectángulo redondeado

## Descripción

```php
public GmagickDraw::roundrectangle(float $x1, float $y1, float $x2, float $y2, float $rx, float $ry): GmagickDraw
```php

Dibuja aun rectángulo redondeado dadas dos coordenadas, los radios de las esquinas x e y, y usando el contorno, el ancho del contorno, y la configuración de relleno actuales.

## Parámetros

`x1`  
primera coordenada x

`y1`  
primera coordenada y

`x2`  
segunda coordenada x

`y2`  
segunda coordenada y

`rx`  
radio de la esquina en dirección horizontal

`ry`  
radio de la esquina en dirección vertical

## Valores devueltos

El objeto `GmagickDraw` si se tuvo éxito
