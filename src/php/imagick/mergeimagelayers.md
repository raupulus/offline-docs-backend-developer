---
title: Imagick::mergeImageLayers
description: Fusiona las capas de la imagen
source_url: https://www.php.net/manual/es/imagick.mergeimagelayers.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/mergeimagelayers.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: 8e2cfbdce
order: 34470
---

Imagick::mergeImageLayers

Fusiona las capas de la imagen

## Descripción

```php
public Imagick::mergeImageLayers(int $layer_method): Imagick
```php

Fusiona las capas de la imagen en una sola. Este método es útil al utilizar formatos de imagen que emplean múltiples capas, como los PSD. La fusión se controla mediante el argumento `layer_method` que define la forma en que las capas deben fusionarse. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.7 o superior.

## Parámetros

`layer_method`  
Una constante entre las constantes `Imagick::LAYERMETHOD_*`.

## Valores devueltos

Devuelve un objeto Imagick que contiene la imagen fusionada.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Ejemplo con `Imagick::mergeImageLayers`

```
<?php
function mergeImageLayers($layerMethodType, $imagePath1, $imagePath2) {

    $imagick = new \Imagick(realpath($imagePath1));

    $imagick2 = new \Imagick(realpath($imagePath2));
    $imagick->addImage($imagick2);
    $imagick->setImageFormat('png');

    $result = $imagick->mergeImageLayers($layerMethodType);
    header("Content-Type: image/png");
    echo $result->getImageBlob();
}

?>

     
```php

## Véase también

`Imagick::flattenImages`
