---
title: Imagick::exportImagePixels
description: Exporta los píxeles brutos de la imagen
source_url: https://www.php.net/manual/es/imagick.exportimagepixels.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/exportimagepixels.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: 65c4446ab
order: 33220
---

Imagick::exportImagePixels

Exporta los píxeles brutos de la imagen

## Descripción

```php
public Imagick::exportImagePixels(int $x, int $y, int $width, int $height, string $map, int $STORAGE): array
```php

Exporta los píxeles de la imagen a un array. El mapa define el orden de exportación de los píxeles. El tamaño del array devuelto corresponde a `width * height * strlen(map)`. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.7 o superior.

## Parámetros

`x`  
Coordenada en X del espacio exportado.

`y`  
Coordenada en Y del espacio exportado.

`width`  
Ancho del espacio exportado.

`height`  
Alto del espacio exportado.

`map`  
Orden de los píxeles exportados. Por ejemplo, `"RGB"`. Los caracteres válidos para el mapa son R, G, B, A, O, C, Y, M, K, I y P.

`STORAGE`  
Consulte la lista de [constantes de tipo pixel](#imagick.constants.pixel)

## Valores devueltos

Devuelve un array que contiene los valores de los píxeles.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Ejemplo con `Imagick::exportImagePixels`

Exportación de los píxeles de la imagen a un array.

```
<?php

/* Crea un nuevo objeto */
$im = new Imagick();

/* Crea una nueva imagen */
$im->newPseudoImage(0, 0, "magick:rose");

/* Exporta los píxeles de la imagen */
$pixels = $im->exportImagePixels(10, 10, 2, 2, "RGB", Imagick::PIXEL_CHAR);

/* Visualización */
var_dump($pixels);
?>

    
```php

El ejemplo anterior mostrará:

    array(12) {
      [0]=>
      int(72)
      [1]=>
      int(64)
      [2]=>
      int(57)
      [3]=>
      int(69)
      [4]=>
      int(59)
      [5]=>
      int(43)
      [6]=>
      int(124)
      [7]=>
      int(120)
      [8]=>
      int(-96)
      [9]=>
      int(91)
      [10]=>
      int(84)
      [11]=>
      int(111)
    }
