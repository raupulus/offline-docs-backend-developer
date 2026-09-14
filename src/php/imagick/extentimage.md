---
title: Imagick::extentImage
description: Establecer el tamaño de la imagen
source_url: https://www.php.net/manual/es/imagick.extentimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/extentimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 6047c10c1
order: 33230
---

Imagick::extentImage

Establecer el tamaño de la imagen

## Descripción

```php
public Imagick::extentImage(int $width, int $height, int $x, int $y): bool
```php

Método cómodo para establecer el tamaño de una imagen. El método establece el tamaño de la imagen y permite ajustar las coordenadas x,y donde comienza el nuevo área. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.1 o superior.

> [!CAUTION]
> Antes de ImageMagick 6.5.7-8 (1623), \$x era positivo cuando se desplazaba hacia la izquierda y negativo cuando se desplazaba hacia la derecha, e \$y era positivo cuando se desplazaba una imagen hacia arriba y negativo cuando se desplazaba hacia abajo. Entre ImageMagick 6.3.7 (1591) e ImageMagick 6.5.7-8 (1623), los ejes de \$x e \$y se voltearon, por lo que \$x era negativo cuando se desplazaba hacia la izquierda y positivo cuando se desplazaba hacia la derecha, e \$y era negativo cuando se desplazaba una imagen hacia arriba y positivo cuando se desplazaba hacia abajo. Entre ImageMagick 6.5.7-8 (1623) e ImageMagick 6.6.9-7 (1641), los ejes de \$x e \$y se volvieron a voltear a la funcionalidad anterior de ImageMagick 6.5.7-8 (1623).

## Parámetros

`width`  
El nuevo ancho

`height`  
El nuevo alto

`x`  
Posición X para el nuevo tamaño

`y`  
Posición Y para el nuevo tamaño

## Valores devueltos

Devuelve `true` en caso de éxito.

## Véase también

`Imagick::resizeImage`, `Imagick::thumbnailImage`, `Imagick::cropImage`
