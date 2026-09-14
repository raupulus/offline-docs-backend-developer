---
title: imagerectangle
description: Dibuja un rectángulo
source_url: https://www.php.net/manual/es/function.imagerectangle.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagerectangle.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: d56953fc8
order: 32270
---

imagerectangle

Dibuja un rectángulo

## Descripción

```php
imagerectangle(GdImage $image, int $x1, int $y1, int $x2, int $y2, int $color): true
```php

`imagerectangle` dibuja un rectángulo en las coordenadas especificadas. El punto 0, 0 es la esquina superior izquierda de la imagen.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`x1`  
X: coordenada de la esquina superior izquierda.

`y1`  
Y: coordenada de la esquina superior izquierda.

`x2`  
X: coordenada del punto inferior derecho.

`y2`  
Y: coordenada del punto inferior derecho.

`color`  
Un identificador de color creado con `imagecolorallocate`.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Ejemplo con `imagerectangle`

```
<?php
// Creación de una imagen de 200 x 200 píxeles
$canvas = imagecreatetruecolor(200, 200);

// Asigna los colores
$pink = imagecolorallocate($canvas, 255, 105, 180);
$white = imagecolorallocate($canvas, 255, 255, 255);
$green = imagecolorallocate($canvas, 132, 135, 28);

// Dibuja 3 rectángulos, cada uno con su color
imagerectangle($canvas, 50, 50, 150, 150, $pink);
imagerectangle($canvas, 45, 60, 120, 100, $white);
imagerectangle($canvas, 100, 120, 75, 160, $green);

// Visualización
header('Content-Type: image/jpeg');
imagejpeg($canvas);
?>

    
```php

Resultado del ejemplo anterior es similar a:

![Visualización del ejemplo: imagerectangle()](en/reference/image/figures/imagerectangle.jpg)
