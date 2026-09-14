---
title: Imagick::raiseImage
description: Crea un efecto de botón en 3D simulado
source_url: https://www.php.net/manual/es/imagick.raiseimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/raiseimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34810
---

Imagick::raiseImage

Crea un efecto de botón en 3D simulado

## Descripción

```php
public Imagick::raiseImage(int $width, int $height, int $x, int $y, bool $raise): bool
```php

Crea un efecto de botón tridimensional simulado aclarando y oscureciendo los bordes de la imagen. Los miembros ancho y alto de la información de elevación definen el ancho del borde vertical y horizontal del efecto.

## Parámetros

`width`  

`height`  

`x`  

`y`  

`raise`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`Imagick::raiseImage`

```
      
<?php
function raiseImage($imagePath, $width, $height, $x, $y, $raise) {
    $imagick = new \Imagick(realpath($imagePath));

    //x and y do nothing?
    $imagick->raiseImage($width, $height, $x, $y, $raise);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
