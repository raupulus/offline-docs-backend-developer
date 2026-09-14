---
title: Imagick::sharpenImage
description: Afila una imagen
source_url: https://www.php.net/manual/es/imagick.sharpenimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/sharpenimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: 0ffb9c9fc
order: 35760
---

Imagick::sharpenImage

Afila una imagen

## Descripción

```php
public Imagick::sharpenImage(float $radius, float $sigma, [int $channel]): bool
```php

Afila una imagen. Se convoluciona la imagen con un operador gaussiano del radio y la desviación estándar (sigma) dados. Para obtener resultados razonables, el radio debería ser mayor que sigma. Use un radio de 0 y `Imagick::sketchImage()` seleccionará un radio apropiado automáticamente.

## Parámetros

`radius`  

`sigma`  

`channel`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`Imagick::sharpenImage`

```
      
<?php
function sharpenImage($imagePath, $radius, $sigma, $channel) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->sharpenimage($radius, $sigma, $channel);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
