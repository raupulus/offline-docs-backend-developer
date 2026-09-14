---
title: Imagick::quantizeImage
description: Analiza los colores dentro de una imagen de referencia
source_url: https://www.php.net/manual/es/imagick.quantizeimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/quantizeimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34750
---

Imagick::quantizeImage

Analiza los colores dentro de una imagen de referencia

## Descripción

```php
public Imagick::quantizeImage(int $numberColors, int $colorspace, int $treedepth, bool $dither, bool $measureError): bool
```php

## Parámetros

`numberColors`  

`colorspace`  

`treedepth`  

`dither`  

`measureError`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

`Imagick::quantizeImage`

```
      
<?php
function quantizeImage($imagePath, $numberColors, $colorSpace, $treeDepth, $dither) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->quantizeImage($numberColors, $colorSpace, $treeDepth, $dither, false);
    $imagick->setImageFormat('png');
    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

?>

      
```php
