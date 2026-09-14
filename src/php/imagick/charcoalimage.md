---
title: Imagick::charcoalImage
description: Simula un dibujo a carboncillo
source_url: https://www.php.net/manual/es/imagick.charcoalimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/charcoalimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 32770
---

Imagick::charcoalImage

Simula un dibujo a carboncillo

## Descripción

```php
public Imagick::charcoalImage(float $radius, float $sigma): bool
```php

Simula un dibujo a carboncillo.

## Parámetros

`radius`  
El radio gaussiano, en píxeles, sin contar el píxel central

`sigma`  
La desviación estándar gaussiana, en píxeles

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`Imagick::charcoalImage`

```
      
<?php
function charcoalImage($imagePath, $radius, $sigma) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->charcoalImage($radius, $sigma);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
