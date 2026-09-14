---
title: Imagick::getImageGeometry
description: Lee las dimensiones de la imagen en un array
source_url: https://www.php.net/manual/es/imagick.getimagegeometry.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/getimagegeometry.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: b0268930d
order: 33750
---

Imagick::getImageGeometry

Lee las dimensiones de la imagen en un array

## Descripción

```php
public Imagick::getImageGeometry(): array
```php

Devuelve el ancho y la altura de la imagen en forma de array asociativo.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `array` con las dimensiones de la imagen.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Uso de `Imagick::getImageGeometry`

```
<?php
$imagick = new Imagick();
$imagick->newImage(100, 200, "black");
print_r($imagick->getImageGeometry());
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [width] => 100
        [height] => 200
    )
