---
title: Imagick::liquidRescaleImage
description: Anima una imagen o imágenes
source_url: https://www.php.net/manual/es/imagick.liquidrescaleimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/liquidrescaleimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34410
---

Imagick::liquidRescaleImage

Anima una imagen o imágenes

## Descripción

```php
public Imagick::liquidRescaleImage(int $width, int $height, float $delta_x, float $rigidity): bool
```php

Este método escala las imágenes usando un método de re-escalada líquido. Este método es una implementación de una técnica llamada "seam carving" (talla de costura). Para que este método funcione como es debido, ImageMagick se debe compilar con el soporte para la biblioteca liblqr. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.9 o superior.

## Parámetros

`width`  
El ancho del tamaño objetivo

`height`  
El alto del tamaño objetivo

`delta_x`  
Cuánto puede atravesar la costura el eje x. Pasar 0 causa que las costuras sean rectas.

`rigidity`  
Introduce un sesgo para costuras no rectas. Este parámetro normalmente es 0.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Véase también

`Imagick::resizeImage`
