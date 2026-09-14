---
title: Imagick::recolorImage
description: Recolorear la imagen
source_url: https://www.php.net/manual/es/imagick.recolorimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/recolorimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: 65c4446ab
order: 34870
---

Imagick::recolorImage

Recolorear la imagen

> [!WARNING]
> Esta función está *DEPRECADA* a partir de Imagick 3.4.4. Depender de esta funcionalidad está fuertemente desaconsejado.

## Descripción

```php
public Imagick::recolorImage(array $matrix): bool
```php

Traduce, escala, recorta y rota los colores de la imagen. Este método soporta matrices variables de escalado, pero normalmente, se utiliza una matriz 5x5 para RGBA y una matriz 6x6 para CMYK. La última línea debe contener los valores normalizados. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.6 o superior.

## Parámetros

`matrix`  
La matriz que contiene los valores de los colores.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Ejemplo con `Imagick::recolorImage`

```
<?php
function recolorImage($imagePath) {
    $imagick = new \Imagick(realpath($imagePath));
    $remapColor = [ 1, 0, 0,
        0, 0, 1,
        0, 1, 0,];

//$remapColor = [
//    1.438, -0.122, -0.016,  0, 0, -0.03,
//    -0.062,  1.378, -0.016,  0, 0,  0.05,
//    -0.062, -0.122, 1.483,   0, 0, -0.02,
//];

    @$imagick->recolorImage($remapColor);

    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

     
```php

## Véase también

`Imagick::displayImage`
