---
title: imagecolorexactalpha
description: Devuelve el índice de un color con su canal alfa
source_url: https://www.php.net/manual/es/function.imagecolorexactalpha.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecolorexactalpha.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 9960a09a5
order: 31610
---

imagecolorexactalpha

Devuelve el índice de un color con su canal alfa

## Descripción

```php
imagecolorexactalpha(GdImage $image, int $red, int $green, int $blue, int $alpha): int
```php

Devuelve el índice de un color con su canal alfa.

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

Devuelve el índice del color proporcionado y su canal alfa en la paleta de la imagen, o -1 si el color no existe en la paleta de la imagen.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Obtención de los colores que componen el logo GD

```
<?php

// Define la imagen
$im = imagecreatefrompng('./gdlogo.png');

$colors   = Array();
$colors[] = imagecolorexactalpha($im, 255, 0, 0, 0);
$colors[] = imagecolorexactalpha($im, 0, 0, 0, 127);
$colors[] = imagecolorexactalpha($im, 255, 255, 255, 55);
$colors[] = imagecolorexactalpha($im, 100, 255, 52, 20);

print_r($colors);

?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => 16711680
        [1] => 2130706432
        [2] => 939524095
        [3] => 342163252
    )

## Véase también

imagecolorclosestalpha
