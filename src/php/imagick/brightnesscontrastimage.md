---
title: Imagick::brightnessContrastImage
description: Cambia el brillo y/o el contraste de una imagen
source_url: https://www.php.net/manual/es/imagick.brightnesscontrastimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/brightnesscontrastimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 6047c10c1
order: 32760
---

Imagick::brightnessContrastImage

Cambia el brillo y/o el contraste de una imagen

## Descripción

```php
public Imagick::brightnessContrastImage(float $brightness, float $contrast, [int $channel]): bool
```php

Cambia el brillo y/o el contraste de una imagen. Convierte los parámetros de brillo y contraste en pendiente e intercepción y llama a una función polinómica para aplicarla a la imagen.

## Parámetros

`brightness`  

`contrast`  

`channel`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`Imagick::brightnessContrastImage`

```
      
<?php
function brightnessContrastImage($imagePath, $brightness, $contrast, $channel) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->brightnessContrastImage($brightness, $contrast, $channel);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
