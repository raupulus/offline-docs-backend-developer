---
title: Imagick::shaveImage
description: Recorta píxeles de los extremos de la imagen
source_url: https://www.php.net/manual/es/imagick.shaveimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/shaveimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35770
---

Imagick::shaveImage

Recorta píxeles de los extremos de la imagen

## Descripción

```php
public Imagick::shaveImage(int $columns, int $rows): bool
```php

Recorta píxeles de los extremos de la imagen. Asigna la memoria necesaria para la estructura de la nueva imagen y devuelve un puntero a la nueva imagen.

## Parámetros

`columns`  

`rows`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`Imagick::shaveImage`

```
      
<?php
function shaveImage($imagePath) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->shaveImage(100, 50);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
