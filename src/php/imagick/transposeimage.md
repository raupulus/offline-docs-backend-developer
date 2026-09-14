---
title: Imagick::transposeImage
description: Aplica una simetría vertical
source_url: https://www.php.net/manual/es/imagick.transposeimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/transposeimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 65c4446ab
order: 36000
---

Imagick::transposeImage

Aplica una simetría vertical

## Descripción

```php
public Imagick::transposeImage(): bool
```php

Aplica una simetría vertical, creando la reflexión de cada píxel alrededor de un eje horizontal, con una rotación de 90 grados. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.2.9 o superior.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Ejemplo con `Imagick::transposeImage`

```
      
<?php
function transposeImage($imagePath) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->transposeImage();
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php

## Véase también

`Imagick::transverseImage`
