---
title: imagesetbrush
description: Modifica el pincel para el dibujo de líneas
source_url: https://www.php.net/manual/es/function.imagesetbrush.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagesetbrush.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: d56953fc8
order: 32320
---

imagesetbrush

Modifica el pincel para el dibujo de líneas

## Descripción

```php
imagesetbrush(GdImage $image, GdImage $brush): true
```php

`imagesetbrush` reemplaza el pincel actual para el dibujo de líneas por `brush`. Este pincel será entonces utilizado con funciones como `imageline` o `imagepolygon` y con los colores especiales `IMG_COLOR_BRUSHED` o `IMG_COLOR_STYLEDBRUSHED`.

> [!CAUTION]
> No es necesario realizar ninguna acción cuando se ha terminado con un pincel, pero si se destruye la imagen del pincel, NO DEBE utilizarse las opciones `IMG_COLOR_BRUSHED` y `IMG_COLOR_STYLEDBRUSHED` antes de crear un nuevo pincel.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`brush`  
Un objeto de imagen.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` y `brush` ahora requieren instancias de `GdImage` ; anteriormente, se esperaban `resource`s. |

## Ejemplos

Ejemplo con `imagesetbrush`

```
<?php

// Carga un mini-logo PHP
$php = imagecreatefrompng('./php.png');

// Creación de la imagen principal, 100x100
$im = imagecreatetruecolor(100, 100);

// Define el fondo en blanco
$white = imagecolorallocate($im, 255, 255, 255);
imagefilledrectangle($im, 0, 0, 99, 99, $white);

// Define el pincel
imagesetbrush($im, $php);

// Dibuja algunas pinceladas
imageline($im, 50, 50, 50, 60, IMG_COLOR_BRUSHED);

// Muestra la imagen en el navegador
header('Content-type: image/png');

imagepng($im);
?>

    
```php

Resultado del ejemplo anterior es similar a:

![Visualización del ejemplo: imagesetbrush()](en/reference/image/figures/imagesetbrush.png)
