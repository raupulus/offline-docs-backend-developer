---
title: Imagick::clutImage
description: Reemplaza los colores de una imagen
source_url: https://www.php.net/manual/es/imagick.clutimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/clutimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 32850
---

Imagick::clutImage

Reemplaza los colores de una imagen

## Descripción

```php
public Imagick::clutImage(Imagick $lookup_table, [int $channel]): bool
```php

Reemplaza los colores en una imagen con una paleta de colores. El segundo parámetro opcional reemplaza los colores de un canal específico. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.6 o superior.

## Parámetros

`lookup_table`  
Objeto Imagick que contiene la paleta de colores

`channel`  
La constante [Channeltype](#imagick.constants.channel). Cuando no se proporciona, los canales predeterminados se reemplazan.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Usar `Imagick::clutImage`:

Reemplazar los colores de una imagen desde una paleta de colores.

```
<?php
$imagen = new Imagick('test.jpg');
$clut = new Imagick();
$clut->newImage(1, 1, new ImagickPixel('black'));
$imagen->clutImage($clut);
$imagen->writeImage('test_out.jpg');
?>

    
```php

## Véase también

`Imagick::adaptiveBlurImage`, `Imagick::motionBlurImage`, `Imagick::radialBlurImage`
