---
title: Imagick::setImageResolution
description: Establece la resolución de la imagen
source_url: https://www.php.net/manual/es/imagick.setimageresolution.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/setimageresolution.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35530
---

Imagick::setImageResolution

Establece la resolución de la imagen

## Descripción

```php
public Imagick::setImageResolution(float $x_resolution, float $y_resolution): bool
```php

Establece la resolución de la imagen.

## Parámetros

`x_resolution`  

`y_resolution`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

`Imagick::setImageResolution`

```
      
<?php
function setImageResolution($imagePath) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->setImageResolution(50, 50);

    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
