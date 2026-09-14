---
title: imagecharup
description: Dibuja un carácter verticalmente
source_url: https://www.php.net/manual/es/function.imagecharup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecharup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: fcd921429
order: 31520
---

imagecharup

Dibuja un carácter verticalmente

## Descripción

```php
imagecharup(GdImage $image, GdFont $font, int $x, int $y, string $char, int $color): true
```php

Dibuja el primer carácter de la cadena `char` verticalmente en la imagen `image` proporcionada.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`font`  
Puede ser 1, 2, 3, 4, 5 para las fuentes internas de codificación Latin2 (donde los números más grandes corresponden a fuentes anchas) o una instancia de `GdFont` retornado por `imageloadfont`.

`x`  
X: coordenada de inicio.

`y`  
Y: coordenada de inicio.

`char`  
El carácter a dibujar.

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

Ejemplo con `imagecharup`

```
<?php

$im = imagecreate(100, 100);

$string = 'Notez que la première lettre est un N';

$bg = imagecolorallocate($im, 255, 255, 255);
$black = imagecolorallocate($im, 0, 0, 0);

// Muestra una "Z" negra sobre un fondo blanco
imagecharup($im, 3, 10, 10, $string, $black);

header('Content-type: image/png');
imagepng($im);

?>

    
```php

Resultado del ejemplo anterior es similar a:

![Visualización del ejemplo: imagecharup()](en/reference/image/figures/imagecharup.png)

## Véase también

imagechar

imageloadfont
