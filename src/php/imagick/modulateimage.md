---
title: Imagick::modulateImage
description: Controla el brillo, la saturación y el tono
source_url: https://www.php.net/manual/es/imagick.modulateimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/modulateimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34490
---

Imagick::modulateImage

Controla el brillo, la saturación y el tono

## Descripción

```php
public Imagick::modulateImage(float $brightness, float $saturation, float $hue): bool
```php

Permite controlar el brillo, la saturación y el tono de una imagen. El tono es el porcentaje de la rotación absoluta desde la posición actual. Por ejemplo, 50 resulta en una rotación en el sentido contrario a las agujas del reloj de 90 grados, 150 resulta en una rotación en el sentido de las agujas del reloj de 90 grados, con 0 y 200 resultando en una rotación de 180 grados.

## Parámetros

`brightness`  

`saturation`  

`hue`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`Imagick::modulateImage`

```
      
<?php
function modulateImage($imagePath, $hue, $brightness, $saturation) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->modulateImage($brightness, $saturation, $hue);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
