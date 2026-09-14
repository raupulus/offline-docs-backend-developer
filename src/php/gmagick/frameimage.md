---
title: Gmagick::frameimage
description: Añade un borde tridimensional simulado
source_url: https://www.php.net/manual/es/gmagick.frameimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/frameimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_revision: 35752f072
order: 26700
---

Gmagick::frameimage

Añade un borde tridimensional simulado

## Descripción

```php
public Gmagick::frameimage(GmagickPixel $color, int $width, int $height, int $inner_bevel, int $outer_bevel): Gmagick
```php

Añade un borde tridimensional simulado alrededor de la imagen. El ancho y alto especifican el ancho del borde de las caras verticales y horizontales del marco. Los biseles interior y exterior indican el ancho de las sombras interiores y exteriores del marco.

## Parámetros

`color`  
Objeto `GmagickPixel` o un valor de tipo float que representa el color mate

`width`  
El ancho del borde.

`height`  
El alto del borde.

`inner_bevel`  
El ancho del bisel interior.

`outer_bevel`  
El ancho del bisel exterior.

## Valores devueltos

El objeto `Gmagick` enmarcado.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
