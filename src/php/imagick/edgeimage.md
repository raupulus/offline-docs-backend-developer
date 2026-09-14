---
title: Imagick::edgeImage
description: Mejora los bordes de la imagen
source_url: https://www.php.net/manual/es/imagick.edgeimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/edgeimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 33160
---

Imagick::edgeImage

Mejora los bordes de la imagen

## Descripción

```php
public Imagick::edgeImage(float $radius): bool
```php

Mejora los bordes de la imagen con un filtro de convolución del radio dado. Use un radio de 0 y éste será autoseleccionado.

## Parámetros

`radius`  
El radio de la operación.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

`Imagick::edgeImage`

```
      
<?php
function edgeImage($imagePath, $radius) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->edgeImage($radius);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
