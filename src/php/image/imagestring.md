---
title: imagestring
description: Dibuja una cadena horizontal
source_url: https://www.php.net/manual/es/function.imagestring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagestring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: fcd921429
order: 32390
---

imagestring

Dibuja una cadena horizontal

## Descripción

```php
imagestring(GdImage $image, GdFont $font, int $x, int $y, string $string, int $color): true
```php

Dibuja una cadena en las coordenadas especificadas.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`font`  
Puede ser 1, 2, 3, 4, 5 para las fuentes internas de codificación Latin2 (donde los números más grandes corresponden a fuentes anchas) o una instancia de `GdFont` retornado por `imageloadfont`.

`x`  
X: coordenada de la esquina superior izquierda.

`y`  
Y: coordenada de la esquina superior izquierda.

`string`  
La cadena a escribir.

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

Ejemplo con `imagestring`

```
<?php
// Nueva imagen 100*30
$im = imagecreate(100, 30);

// Fondo blanco y texto azul
$bg = imagecolorallocate($im, 255, 255, 255);
$textcolor = imagecolorallocate($im, 0, 0, 255);

// Añadir la frase en la esquina superior izquierda
imagestring($im, 5, 0, 0, 'Hello world!', $textcolor);

// Mostrar la imagen
header('Content-type: image/png');

imagepng($im);
?>

    
```php

Resultado del ejemplo anterior es similar a:

![Visualización del ejemplo: imagestring()](en/reference/image/figures/imagestring.png)

## Véase también

imagestringup

imageloadfont

imagettftext
