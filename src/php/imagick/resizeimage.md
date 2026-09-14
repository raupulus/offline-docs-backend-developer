---
title: Imagick::resizeImage
description: Escala una imagen
source_url: https://www.php.net/manual/es/imagick.resizeimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/resizeimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34950
---

Imagick::resizeImage

Escala una imagen

## Descripción

```php
public Imagick::resizeImage(int $columns, int $rows, int $filter, float $blur, [bool $bestfit], [bool $legacy]): bool
```php

Escala una imagen a las dimensiones deseadas con un [filtro](#imagick.constants.filters).

> [!NOTE]
> El comportamiento del parámetro `bestfit` cambió con Imagick 3.0.0. Antes de esta versión, proporcionar las dimensiones 400x400 a una imagen de dimensiones 200x150 hacía que la parte izquierda permaneciera sin cambios. Con Imagick 3.0.0 y posteriores, la imagen se reduce al tamaño 400x300, siendo este el mejor resultado para esas dimensiones. Si el parámetro `bestfit` es utilizado, la anchura y la altura deben ser proporcionadas.

## Parámetros

`columns`  
Ancho de la imagen

`rows`  
Alto de la imagen

`filter`  
Consulte la lista de [constantes de filtro](#imagick.constants.filters).

`blur`  
El factor de borrosidad donde \> 1 es borroso, \< 1 es nítido.

`bestfit`  
Parámetro de ajuste opcional.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL imagick 2.1.0 | Añadido el parámetro opcional de ajuste. Este método ahora soporta escalas proporcionales. Pase cero como parámetro para escalar proporcionalmente. |

## Ejemplos

`Imagick::resizeImage`

```
      
<?php
function resizeImage($imagePath, $width, $height, $filterType, $blur, $bestFit, $cropZoom) {
    //The blur factor where > 1 is blurry, < 1 is sharp.
    $imagick = new \Imagick(realpath($imagePath));

    $imagick->resizeImage($width, $height, $filterType, $blur, $bestFit);

    $cropWidth = $imagick->getImageWidth();
    $cropHeight = $imagick->getImageHeight();

    if ($cropZoom) {
        $newWidth = $cropWidth / 2;
        $newHeight = $cropHeight / 2;

        $imagick->cropimage(
            $newWidth,
            $newHeight,
            ($cropWidth - $newWidth) / 2,
            ($cropHeight - $newHeight) / 2
        );

        $imagick->scaleimage(
            $imagick->getImageWidth() * 4,
            $imagick->getImageHeight() * 4
        );
    }

    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
