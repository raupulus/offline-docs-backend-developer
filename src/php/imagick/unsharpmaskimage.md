---
title: Imagick::unsharpMaskImage
description: Afila una imagen
source_url: https://www.php.net/manual/es/imagick.unsharpmaskimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/unsharpmaskimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 36040
---

Imagick::unsharpMaskImage

Afila una imagen

## Descripción

```php
public Imagick::unsharpMaskImage(float $radius, float $sigma, float $amount, float $threshold, [int $channel]): bool
```php

Afila una imagen. Se convoluciona la imagen con un operador gaussiano del radio y la desviación estándar (sigma) dados. Para obtener resultados razonables, el radio debería ser mayor que sigma. Use un radio de 0 y Imagick::sketchImage() seleccionará un radio apropiado automáticamente.

## Parámetros

`radius`  

`sigma`  

`amount`  

`threshold`  

`channel`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

`Imagick::unsharpMaskImage`

```
      
<?php
function unsharpMaskImage($imagePath, $radius, $sigma, $amount, $unsharpThreshold) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->unsharpMaskImage($radius, $sigma, $amount, $unsharpThreshold);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
