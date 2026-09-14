---
title: imagecolorclosest
description: Devuelve el índice de la color más cercana a una color dada
source_url: https://www.php.net/manual/es/function.imagecolorclosest.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecolorclosest.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 9960a09a5
order: 31560
---

imagecolorclosest

Devuelve el índice de la color más cercana a una color dada

## Descripción

```php
imagecolorclosest(GdImage $image, int $red, int $green, int $blue): int
```php

Devuelve el índice de la color de la paleta que es la más cercana al valor RGB pasado.

La "distancia" entre la color deseada y las colores de la paleta se calcula considerando el espacio RGB como un espacio de 3 dimensiones.

Si la imagen fue creada a partir de un fichero, solo se resuelven los colores utilizados en la imagen. Los colores presentes únicamente en la paleta no se resuelven.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`red`  
Valor del componente rojo.

`green`  
Valor del componente verde.

`blue`  
Valor del componente azul.

Los argumentos sobre las colores son enteros comprendidos entre 0 y 255 o hexadecimales comprendidos entre 0x00 y 0xFF.

## Valores devueltos

Devuelve el índice de la color más cercana, en la paleta de la imagen, a la dada.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Búsqueda de un juego de colores en una imagen

```
<?php
// Se comienza con una imagen y se convierte en una imagen de paleta
$im = imagecreatefrompng('figures/imagecolorclosest.png');
imagetruecolortopalette($im, false, 255);

// Colores buscados (RGB)
$colors = array(
    array(254, 145, 154),
    array(153, 145, 188),
    array(153, 90, 145),
    array(255, 137, 92)
);

// Se itera sobre cada búsqueda y se encuentra la color de la paleta más cercana.
// Devuelve el número de la búsqueda, el RGB buscado y la correspondencia en RGB
foreach($colors as $id => $rgb)
{
    $result = imagecolorclosest($im, $rgb[0], $rgb[1], $rgb[2]);
    $result = imagecolorsforindex($im, $result);
    $result = "({$result['red']}, {$result['green']}, {$result['blue']})";

    echo "#$id: Búsqueda ($rgb[0], $rgb[1], $rgb[2]); Correspondencia : $result.\n";
}

?>

    
```php

Resultado del ejemplo anterior es similar a:

    #0: Búsqueda (254, 145, 154); Correspondencia : (252, 150, 148).
    #1: Búsqueda (153, 145, 188); Correspondencia : (148, 150, 196).
    #2: Búsqueda (153, 90, 145); Correspondencia : (148, 90, 156).
    #3: Búsqueda (255, 137, 92); Correspondencia : (252, 150, 92).

## Véase también

imagecolorexact

imagecolorclosestalpha

imagecolorclosesthwb
