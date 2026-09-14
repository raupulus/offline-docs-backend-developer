---
title: Imagick::setImageBias
description: Establece el sesgo de la imagen para cualquier método que convolucione
  una imagen
source_url: https://www.php.net/manual/es/imagick.setimagebias.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/setimagebias.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35200
---

Imagick::setImageBias

Establece el sesgo de la imagen para cualquier método que convolucione una imagen

> [!WARNING]
> Esta función está *DEPRECADA* a partir de Imagick 3.4.4. Depender de esta funcionalidad está fuertemente desaconsejado.

## Descripción

```php
public Imagick::setImageBias(float $bias): bool
```php

Establece el sesgo de la imagen para cualquier método que convolucione una imagen (p.ej. Imagick::ConvolveImage()).

## Parámetros

`bias`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

`Imagick::setImageBias`

```
<?php
//requires ImageMagick version 6.9.0-1 to have an effect on convolveImage
function setImageBias($bias) {
    $imagick = new \Imagick(realpath("images/stack.jpg"));

    $xKernel = array(
        -0.70, 0, 0.70,
        -0.70, 0, 0.70,
        -0.70, 0, 0.70
    );

    $imagick->setImageBias($bias * \Imagick::getQuantum());
    $imagick->convolveImage($xKernel, \Imagick::CHANNEL_ALL);

    $imagick->setImageFormat('png');

    header('Content-type: image/png');
    echo $imagick->getImageBlob();
}

?>

     
```php
