---
title: Imagick::blueShiftImage
description: Atenúa los colores de la imagen
source_url: https://www.php.net/manual/es/imagick.blueshiftimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/blueshiftimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 1ef9c7a76
order: 32730
---

Imagick::blueShiftImage

Atenúa los colores de la imagen

## Descripción

```php
public Imagick::blueShiftImage([float $factor]): bool
```php

Atenúa los colores de la imagen para simular una escena nocturna a la luz de la luna.

## Parámetros

`factor`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`Imagick::blueShiftImage`

```
      
<?php
function blueShiftImage($imagePath, $blueShift) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->blueShiftImage($blueShift);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
