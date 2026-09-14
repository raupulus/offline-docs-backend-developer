---
title: imagesetstyle
description: Configura el estilo para el dibujo de líneas
source_url: https://www.php.net/manual/es/function.imagesetstyle.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagesetstyle.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 9960a09a5
order: 32360
---

imagesetstyle

Configura el estilo para el dibujo de líneas

## Descripción

```php
imagesetstyle(GdImage $image, array $style): bool
```php

`imagesetstyle` permite seleccionar el estilo a utilizar al dibujar líneas (como con las funciones `imageline` y `imagepolygon`) al utilizar la color especial `IMG_COLOR_STYLED` o bien al dibujar líneas con la color `IMG_COLOR_STYLEDBRUSHED`.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`style`  
Un array de colores de píxeles. Puede utilizarse la constante `IMG_COLOR_TRANSPARENT` para añadir un píxel transparente. Tenga en cuenta que `style` no debe ser un array `array` vacío.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

El siguiente ejemplo dibuja una línea punteada desde la esquina superior izquierda hacia la esquina inferior derecha de la imagen:

Ejemplo para `imagesetstyle`

```
<?php
header("Content-type: image/jpeg");
$im  = imagecreatetruecolor(100, 100);
$w   = imagecolorallocate($im, 255, 255, 255);
$red = imagecolorallocate($im, 255, 0, 0);

/* Dibuja una línea punteada de 5 píxeles rojos, 5 píxeles blancos */
$style = array($red, $red, $red, $red, $red, $w, $w, $w, $w, $w);
imagesetstyle($im, $style);
imageline($im, 0, 0, 100, 100, IMG_COLOR_STYLED);

/* Dibuja una línea con smileys, utilizando imagesetbrush() y imagesetstyle */
$style = array($w, $w, $w, $w, $w, $w, $w, $w, $w, $w, $w, $w, $red);
imagesetstyle($im, $style);

$brush = imagecreatefrompng("http://www.libpng.org/pub/png/images/smile.happy.png");
$w2 = imagecolorallocate($brush, 255, 255, 255);
imagecolortransparent($brush, $w2);
imagesetbrush($im, $brush);
imageline($im, 100, 0, 0, 100, IMG_COLOR_STYLEDBRUSHED);

imagejpeg($im);
?>

    
```php

Resultado del ejemplo anterior es similar a:

![Visualización del ejemplo: imagesetstyle()](en/reference/image/figures/imagesetstyle.jpg)

## Véase también

imagesetbrush

imageline
