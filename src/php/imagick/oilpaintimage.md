---
title: Imagick::oilPaintImage
description: Simula una pintura al óleo
source_url: https://www.php.net/manual/es/imagick.oilpaintimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/oilpaintimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34600
---

Imagick::oilPaintImage

Simula una pintura al óleo

## Descripción

```php
public Imagick::oilPaintImage(float $radius): bool
```php

Aplica un filtro de efecto especial que simula una pintura al óleo. Cada píxel es reemplazado por el color más frecuente que suceda en una región circular definida por el radio.

## Parámetros

`radius`  
El radio de la zona circular inmediata.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`Imagick::oilPaintImage`

```
      
<?php
function oilPaintImage($imagePath, $radius) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->oilPaintImage($radius);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
