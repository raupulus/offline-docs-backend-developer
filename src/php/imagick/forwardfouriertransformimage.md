---
title: Imagick::forwardFourierTransformImage
description: Implementa la transformada discreta de Fourier (Discrete Fourier Transform
  - DFT)
source_url: https://www.php.net/manual/es/imagick.forwardfouriertransformimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/forwardfouriertransformimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 7cecc752c
order: 33290
---

Imagick::forwardFourierTransformImage

Implementa la transformada discreta de Fourier (Discrete Fourier Transform - DFT)

## Descripción

```php
public Imagick::forwardFourierTransformimage(bool $magnitude): bool
```php

Implementa la transformada discreta de Fourier (DFT) de la imagen ya sea como un par de imágenes magnitud/fase o como un par de imágenes reales/imaginarias.

## Parámetros

`magnitude`  
Si es verdadero, devuelve como un par magnitud/fase, de lo contrario un par de imágenes reales/imaginarias.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`Imagick::forwardFourierTransformImage`

```
      
<?php
//Función de utilidad para forwardTransformImage
function createMask() {
    $draw = new \ImagickDraw();

    $draw->setStrokeOpacity(0);
    $draw->setStrokeColor('rgb(255, 255, 255)');
    $draw->setFillColor('rgb(255, 255, 255)');

    // Dibuja un círculo en el eje y, con su centro
    // en x, y que toca el origen
    $draw->circle(250, 250, 220, 250);

    $imagick = new \Imagick();
    $imagick->newImage(512, 512, "black");
    $imagick->drawImage($draw);
    $imagick->gaussianBlurImage(20, 20);
    $imagick->autoLevelImage();

    return $imagick;
}

function forwardFourierTransformImage($imagePath) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->resizeimage(512, 512, \Imagick::FILTER_LANCZOS, 1);

    $mask = createMask();
    $imagick->forwardFourierTransformImage(true);

    @$imagick->setimageindex(0);
    $magnitude = $imagick->getimage();

    @$imagick->setimageindex(1);
    $imagickPhase = $imagick->getimage();

    if (true) {
        $imagickPhase->compositeImage($mask, \Imagick::COMPOSITE_MULTIPLY, 0, 0);
    }

    if (false) {
        $output = clone $imagickPhase;
        $output->setimageformat('png');
        header("Content-Type: image/png");
        echo $output->getImageBlob();
    }

    $magnitude->inverseFourierTransformImage($imagickPhase, true);

    $magnitude->setimageformat('png');
    header("Content-Type: image/png");
    echo $magnitude->getImageBlob();
}

?>

      
```php
