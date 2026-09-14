---
title: Imagick::rotateImage
description: Rota una imagen
source_url: https://www.php.net/manual/es/imagick.rotateimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/rotateimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34970
---

Imagick::rotateImage

Rota una imagen

## Descripción

```php
public Imagick::rotateImage(mixed $background, float $degrees): bool
```php

Rota una imagen el número de grados especificado. Los triángulos vacíos sobrantes por la rotación de la imagen se rellenan con el color de fondo.

## Parámetros

`background`  
El color de fondo

`degrees`  
Ángulo de rotación, en grados. El ángulo de rotación se interpreta como el número de grados a rotar la imagen en sentido de las agujas del reloj.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL imagick 2.1.0 | Ahora se permite que una string represente el color como primer parámetro. Versiones anteriores sólo permitían un objeto ImagickPixel. |

## Ejemplos

`Imagick::rotateImage`

```
      
<?php
function rotateImage($imagePath, $angle, $color) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->rotateimage($color, $angle);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
