---
title: Imagick::getImagePixelColor
description: Devuelve el color del píxel especificado
source_url: https://www.php.net/manual/es/imagick.getimagepixelcolor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/getimagepixelcolor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 33900
---

Imagick::getImagePixelColor

Devuelve el color del píxel especificado

## Descripción

```php
public Imagick::getImagePixelColor(int $x, int $y): ImagickPixel
```php

Devuelve el color del píxel especificado.

## Parámetros

`x`  
La coordenada x del píxel

`y`  
La coordenada y del píxel

## Valores devueltos

Devuelve una instancia de ImagickPixel para el color en las coordenadas dadas.

## Errores/Excepciones

Lanza una ImagickException en caso de error.
