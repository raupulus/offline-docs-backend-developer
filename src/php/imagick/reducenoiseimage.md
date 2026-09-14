---
title: Imagick::reduceNoiseImage
description: Suaviza los contornos de una imagen
source_url: https://www.php.net/manual/es/imagick.reducenoiseimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/reducenoiseimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34880
---

Imagick::reduceNoiseImage

Suaviza los contornos de una imagen

> [!WARNING]
> Esta función está *DEPRECADA* a partir de Imagick 3.4.4. Depender de esta funcionalidad está fuertemente desaconsejado.

## Descripción

```php
public Imagick::reduceNoiseImage(float $radius): bool
```php

Suaviza los contornos de una imagen mientras que se preserva todavía la información del borde. El algoritmo funciona reemplazando cada píxel con su más cercano inmediato en valor. La zona inmediata está definida por el radio. Use un radio de 0 y Imagick::reduceNoiseImage() seleccionará una radio apropiado automáticamente.

## Parámetros

`radius`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

`Imagick::reduceNoiseImage`

```
      
<?php
function reduceNoiseImage($imagePath, $reduceNoise) {
    $imagick = new \Imagick(realpath($imagePath));
    @$imagick->reduceNoiseImage($reduceNoise);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
