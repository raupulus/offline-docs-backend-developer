---
title: imagecolorclosestalpha
description: Devuelve el color más cercano, teniendo en cuenta el canal alpha
source_url: https://www.php.net/manual/es/function.imagecolorclosestalpha.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecolorclosestalpha.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_revision: 9960a09a5
order: 31570
---

imagecolorclosestalpha

Devuelve el color más cercano, teniendo en cuenta el canal alpha

## Descripción

```php
imagecolorclosestalpha(GdImage $image, int $red, int $green, int $blue, int $alpha): int
```php

Devuelve el índice del color, en la paleta de la imagen `image`, más cercano al color especificado por los demás parámetros, en formato RGB y con canal alpha `alpha`.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`red`  
Valor del componente rojo.

`green`  
Valor del componente verde.

`blue`  
Valor del componente azul.

`alpha`  
Un valor comprendido entre `0` y `127`. `0` indica una opacidad completa mientras que `127` indica una transparencia completa.

Los parámetros sobre los colores son enteros comprendidos entre 0 y 255 o hexadecimales comprendidos entre 0x00 y 0xFF.

## Valores devueltos

Devuelve el índice del color más cercano en la paleta.

## Ejemplos

Busca un juego de colores en una imagen

```
<?php
// Se comienza con una imagen y se la convierte en paleta
$im = imagecreatefrompng('figures/imagecolorclosest.png');
imagetruecolortopalette($im, false, 255);

// Búsqueda de colores (RGB)
$colors = array(
    array(254, 145, 154, 50),
    array(153, 145, 188, 127),
    array(153, 90, 145, 0),
    array(255, 137, 92, 84)
);

// Se itera sobre cada búsqueda y se encuentra el color más cercano de la paleta.
// Devuelve el número de la búsqueda, la búsqueda RGB y el resultado convertido en RGB
foreach($colors as $id => $rgb)
{
    $result = imagecolorclosestalpha($im, $rgb[0], $rgb[1], $rgb[2], $rgb[3]);
    $result = imagecolorsforindex($im, $result);
    $result = "({$result['red']}, {$result['green']}, {$result['blue']}, {$result['alpha']})";

    echo "#$id: Búsqueda ($rgb[0], $rgb[1], $rgb[2], $rgb[3]); Resultado más cercano: $result.\n";
}

?>

    
```php

Resultado del ejemplo anterior es similar a:

    #0: Búsqueda (254, 145, 154, 50); Resultado más cercano : (252, 150, 148, 0).
    #1: Búsqueda (153, 145, 188, 127); Resultado más cercano : (148, 150, 196, 0).
    #2: Búsqueda (153, 90, 145, 0); Resultado más cercano : (148, 90, 156, 0).
    #3: Búsqueda (255, 137, 92, 84); Resultado más cercano : (252, 150, 92, 0).

## Véase también

imagecolorexactalpha

imagecolorclosest

imagecolorclosesthwb
