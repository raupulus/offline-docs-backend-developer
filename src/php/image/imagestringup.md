---
title: imagestringup
description: Dibuja una cadena vertical
source_url: https://www.php.net/manual/es/function.imagestringup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagestringup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: fcd921429
order: 32400
---

imagestringup

Dibuja una cadena vertical

## Descripción

```php
imagestringup(GdImage $image, GdFont $font, int $x, int $y, string $string, int $color): true
```php

Dibuja una cadena en una línea vertical en la imagen `image` en las coordenadas especificadas.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`font`  
Puede ser 1, 2, 3, 4, 5 para las fuentes internas de codificación Latin2 (donde los números más grandes corresponden a fuentes anchas) o una instancia de `GdFont` retornado por `imageloadfont`.

`x`  
Coordenada X del ángulo superior izquierdo.

`y`  
Coordenada Y del ángulo superior izquierdo.

`string`  
El `string` a escribir.

`color`  
Un identificador de color creado con `imagecolorallocate`.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `font` ahora acepta una instancia de `GdFont` y un `int`; anteriormente solo un `int` era aceptado. |
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Ejemplo con `imagestringup`

```
<?php
// Creación de una imagen de 100*100 píxeles
$im = imagecreatetruecolor(100, 100);

// Dibuja un texto
$textcolor = imagecolorallocate($im, 0xFF, 0xFF, 0xFF);
imagestringup($im, 3, 40, 80, 'gd library', $textcolor);

// Guarda la imagen
imagepng($im, './stringup.png');
?>

    
```php

Resultado del ejemplo anterior es similar a:

![Visualización del ejemplo: imagestringup()](en/reference/image/figures/imagestringup.png)

## Véase también

imagestring

imageloadfont
