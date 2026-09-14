---
title: imagedashedline
description: Dibuja una línea punteada
source_url: https://www.php.net/manual/es/function.imagedashedline.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagedashedline.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: d56953fc8
order: 31930
---

imagedashedline

Dibuja una línea punteada

## Descripción

```php
imagedashedline(GdImage $image, int $x1, int $y1, int $x2, int $y2, int $color): true
```php

`imagedashedline` está obsoleto. Se recomienda utilizar una combinación de las funciones `imagesetstyle` y `imageline`. El punto 0, 0 es la esquina superior izquierda de la imagen.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`x1`  
Coordenada x del primer punto.

`y1`  
Coordenada y del primer punto.

`x2`  
Coordenada x del segundo punto.

`y2`  
Coordenada y del segundo punto.

`color`  
El color de relleno. Un identificador de color creado con `imagecolorallocate`.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Ejemplo con `imagedashedline`

```
<?php
// Crea una imagen de 100x100 píxeles
$im = imagecreatetruecolor(100, 100);
$white = imagecolorallocate($im, 0xFF, 0xFF, 0xFF);

// Dibuja una línea vertical punteada
imagedashedline($im, 50, 25, 50, 75, $white);

// Guarda la imagen
imagepng($im, './dashedline.png');
?>

    
```php

Resultado del ejemplo anterior es similar a:

![Visualización del ejemplo: imagedashedline()](en/reference/image/figures/imagedashedline.png)

Alternativa a la función `imagedashedline`

```
<?php
// Crea una imagen de 100x100 píxeles
$im = imagecreatetruecolor(100, 100);
$white = imagecolorallocate($im, 0xFF, 0xFF, 0xFF);

// Define el estilo: Los 4 primeros píxeles son blancos y los 4 siguientes
// son transparentes. Esto va a crear el efecto de línea punteada
$style = Array(
                $white,
                $white,
                $white,
                $white,
                IMG_COLOR_TRANSPARENT,
                IMG_COLOR_TRANSPARENT,
                IMG_COLOR_TRANSPARENT,
                IMG_COLOR_TRANSPARENT
                );

imagesetstyle($im, $style);

// Dibuja la línea punteada
imageline($im, 50, 25, 50, 75, IMG_COLOR_STYLED);

// Guarda la imagen
imagepng($im, './imageline.png');
?>

    
```php

## Véase también

imagesetstyle

imageline
