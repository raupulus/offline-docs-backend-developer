---
title: Imagick::radialBlurImage
description: Hace borrosa de forma radial una imagen
source_url: https://www.php.net/manual/es/imagick.radialblurimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/radialblurimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34800
---

Imagick::radialBlurImage

Hace borrosa de forma radial una imagen

> [!WARNING]
> Esta función está *DEPRECADA* a partir de Imagick 3.4.4. Depender de esta funcionalidad está fuertemente desaconsejado.

## Descripción

```php
public Imagick::radialBlurImage(float $angle, [int $channel]): bool
```php

Hace borrosa de forma radial una imagen.

## Parámetros

`angle`  

`channel`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`Imagick::radialBlurImage`

```
      
<?php
function radialBlurImage($imagePath) {
    $imagick = new \Imagick(realpath($imagePath));
    //Blur 3 times with different radii
    $imagick->radialBlurImage(3);
    $imagick->radialBlurImage(5);
    $imagick->radialBlurImage(7);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
