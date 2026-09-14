---
title: Imagick::cropImage
description: Extrae una región de la imagen
source_url: https://www.php.net/manual/es/imagick.cropimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/cropimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: 0ffb9c9fc
order: 33010
---

Imagick::cropImage

Extrae una región de la imagen

## Descripción

```php
public Imagick::cropImage(int $width, int $height, int $x, int $y): bool
```php

Extrae una región de la imagen.

## Parámetros

`width`  
El ancho del recorte

`height`  
El alto del recorte

`x`  
La coordenada X de la esquina superior izquierda de la región recortada

`y`  
La coordenada Y de la esquina superior izquierda de la región recortada

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

`Imagick::cropImage`

```
      
<?php
function cropImage($imagePath, $startX, $startY, $width, $height) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->cropImage($width, $height, $startX, $startY);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
