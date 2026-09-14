---
title: Imagick::segmentImage
description: Segmenta una imagen
source_url: https://www.php.net/manual/es/imagick.segmentimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/segmentimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: b8758b060
order: 35020
---

Imagick::segmentImage

Segmenta una imagen

## Descripción

```php
public Imagick::segmentImage(int $COLORSPACE, float $cluster_threshold, float $smooth_threshold, [bool $verbose]): bool
```php

Analiza la imagen e identifica las unidades similares. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.5 o superior.

## Parámetros

`COLORSPACE`  
Una constante entre las [constantes COLORSPACE](#imagick.constants.colorspace).

`cluster_threshold`  
Un porcentaje que describe el número mínimo de píxeles contenidos en el hexedro antes de que sea considerado válido.

`smooth_threshold`  
Elimina el ruido del histograma.

`verbose`  
Si se deben o no mostrar las informaciones detalladas sobre el reconocimiento de las clases.

## Valores devueltos

## Ejemplos

Ejemplo con `Imagick::segmentImage`

```
<?php
function segmentImage($imagePath, $colorSpace, $clusterThreshold, $smoothThreshold) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->segmentImage($colorSpace, $clusterThreshold, $smoothThreshold);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

segmentImage($imagePath, \Imagick::COLORSPACE_RGB, 5, 5);

?>

     
```php
