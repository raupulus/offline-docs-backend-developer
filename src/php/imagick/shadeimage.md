---
title: Imagick::shadeImage
description: Crea un efecto en 3D
source_url: https://www.php.net/manual/es/imagick.shadeimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/shadeimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: 0ffb9c9fc
order: 35740
---

Imagick::shadeImage

Crea un efecto en 3D

## Descripción

```php
public Imagick::shadeImage(bool $gray, float $azimuth, float $elevation): bool
```php

Hace brillar una luz distante sobre una imagen para crear un efecto tridimensional. Se controla la posición de la luz con los parámetros azimuth (acimut) y elevation (elevación); el acimut se mide en grados desde el eje X y la elevación se mide en píxeles por encima del eje Z. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.2.9 o superior.

## Parámetros

`gray`  
Un valor distinto de cero sombrea la intensidad de cada píxel.

`azimuth`  
Define la dirección de la fuente de luz.

`elevation`  
Define la dirección de la fuente de luz.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una excepción de tipo ImagickException en caso de error.

## Ejemplos

`Imagick::shadeImage`

```
      
<?php
function shadeImage($imagePath) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->shadeImage(true, 45, 20);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
