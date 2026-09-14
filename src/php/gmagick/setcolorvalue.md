---
title: GmagickPixel::setcolorvalue
description: Establece el valor normalizado de uno de los canales
source_url: https://www.php.net/manual/es/gmagickpixel.setcolorvalue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagickpixel/setcolorvalue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_revision: 35752f072
order: 28280
---

GmagickPixel::setcolorvalue

Establece el valor normalizado de uno de los canales

## Descripción

```php
public GmagickPixel::setcolorvalue(int $color, float $value): GmagickPixel
```php

Establece el valor del canal especificado de este objeto al valor proporcionado, el cuál debería estar entre 0 y 1. Esta función se puede usar para proporcionar un canal de opacidad al objeto `GmagickPixel`.

## Parámetros

`color`  
Una de las constantes de color de canal de Gmagick.

`value`  
El valor para establecer este canal tiene un rango desde 0 a 1.

## Valores devueltos

El objeto `GmagickPixel` si se tuvo éxtio.
