---
title: Gmagick::borderimage
description: Rodea la imagen con un borde
source_url: https://www.php.net/manual/es/gmagick.borderimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/borderimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_revision: 35752f072
order: 26490
---

Gmagick::borderimage

Rodea la imagen con un borde

## Descripción

```php
public Gmagick::borderimage(GmagickPixel $color, int $width, int $height): Gmagick
```php

Rodea la imagen con un borde del color definido por el objeto `GmagickPixel` de color de borde o por una cadena de color.

## Parámetros

`color`  
El objeto `GmagickPixel` o una cadena que contiene el color del borde

`width`  
Ancho del borode.

`height`  
Alto del borde.

## Valores devueltos

El objeto `Gmagick` con el borde definido

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
