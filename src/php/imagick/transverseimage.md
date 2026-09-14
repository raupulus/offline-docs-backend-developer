---
title: Imagick::transverseImage
description: Crea un espejo horizontal de la imagen
source_url: https://www.php.net/manual/es/imagick.transverseimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/transverseimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 65c4446ab
order: 36010
---

Imagick::transverseImage

Crea un espejo horizontal de la imagen

## Descripción

```php
public Imagick::transverseImage(): bool
```php

Crea un espejo horizontal de la imagen reflejando los píxeles alrededor de un eje Y central, y realizando una rotación de 270 grados. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.2.9 o superior.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Ejemplo con `Imagick::transverseImage`

```
      
<?php
function transverseImage($imagePath) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->transverseImage();
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php

## Véase también

`Imagick::transposeImage`
