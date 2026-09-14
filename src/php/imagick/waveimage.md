---
title: Imagick::waveImage
description: Añade un filtro de ondas a la imagen
source_url: https://www.php.net/manual/es/imagick.waveimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/waveimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 65c4446ab
order: 36070
---

Imagick::waveImage

Añade un filtro de ondas a la imagen

## Descripción

```php
public Imagick::waveImage(float $amplitude, float $length): bool
```php

Añade un filtro de ondas a la imagen. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.2.9 o superior.

## Parámetros

`amplitude`  
Amplitud de la onda.

`length`  
Longitud de la onda.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

WaveImage puede ser muy lento: `Imagick::waveImage`

```
<?php
function waveImage($imagePath, $amplitude, $length) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->waveImage($amplitude, $length);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

    
```php

## Véase también

`Imagick::solarizeImage`, `Imagick::oilpaintImage`, `Imagick::embossImage`, `Imagick::addNoiseImage`, `Imagick::swirlImage`
