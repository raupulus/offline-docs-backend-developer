---
title: imagecolorresolvealpha
description: Devuelve un índice de color o su alternativa más cercana, incluyendo
  el canal alpha
source_url: https://www.php.net/manual/es/function.imagecolorresolvealpha.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecolorresolvealpha.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 9960a09a5
order: 31640
---

imagecolorresolvealpha

Devuelve un índice de color o su alternativa más cercana, incluyendo el canal alpha

## Descripción

```php
imagecolorresolvealpha(GdImage $image, int $red, int $green, int $blue, int $alpha): int
```php

`imagecolorresolvealpha` siempre devuelve un índice de color, disponible en la paleta de la imagen `image`: ya sea el color exacto o la mejor aproximación.

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

Los parámetros sobre los colores son enteros entre 0 y 255 o hexadecimales comprendidos entre 0x00 y 0xFF.

## Valores devueltos

Devuelve un índice de color.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Ejemplo con `imagecoloresolve` para recuperar los colores de una imagen

```
<?php
// Carga de la imagen
$im = imagecreatefromgif('phplogo.gif');

// Recuperación de los colores más cercanos de la imagen
$colors = array();
$colors[] = imagecolorresolvealpha($im, 255, 255, 255, 0);
$colors[] = imagecolorresolvealpha($im, 0, 0, 200, 127);

// Mostrar
print_r($colors);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => 89
        [1] => 85
    )

## Véase también

imagecolorclosestalpha
