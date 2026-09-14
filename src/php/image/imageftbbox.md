---
title: imageftbbox
description: Calcula el rectángulo de delimitación para un texto, utilizando la fuente
  actual y freetype2
source_url: https://www.php.net/manual/es/function.imageftbbox.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imageftbbox.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: 525aa5f19
order: 32060
---

imageftbbox

Calcula el rectángulo de delimitación para un texto, utilizando la fuente actual y freetype2

## Descripción

```php
imageftbbox(float $size, float $angle, string $font_filename, string $string, [array $options]): array
```php

`imageftbbox` calcula el rectángulo de delimitación para el texto `text`, utilizando la fuente actual y freetype2.

> [!NOTE]
> Anterior a PHP 8.0.0, `imageftbbox` era una variante extendida de `imagettfbbox` que además soporta `extrainfo`. A partir de PHP 8.0.0, `imagettfbbox` es un alias de `imageftbbox`.

## Parámetros

`size`  
El tamaño de la fuente en puntos.

`angle`  
Ángulo, en grados, en el cual el parámetro `string` será medido.

`font_filename`  
El nombre del archivo de la fuente TrueType (puede ser una URL). Dependiendo de la versión de GD utilizada por PHP, se buscarán los archivos que no comiencen con un '/', añadiendo la extensión '.ttf', y siguiendo la ruta de fuentes definida por la biblioteca.

`string`  
La cadena a medir.

`options`  
| Clave         | Tipo    | Significado                                     |
|---------------|---------|-------------------------------------------------|
| `linespacing` | `float` | Representa el espaciado entre líneas al dibujar |

Índices posibles para el array `options`

## Valores devueltos

`imageftbbox` devuelve un array que contiene 8 elementos representando los 4 puntos del rectángulo que rodea el texto:

|     |                                           |
|-----|-------------------------------------------|
| 0   | Esquina inferior izquierda, posición en X |
| 1   | Esquina inferior izquierda, posición en Y |
| 2   | Esquina inferior derecha, posición en X   |
| 3   | Esquina inferior derecha, posición en Y   |
| 4   | Esquina superior derecha, posición en X   |
| 5   | Esquina superior derecha, posición en Y   |
| 6   | Esquina superior izquierda, posición en X |
| 7   | Esquina superior izquierda, posición en Y |

Los puntos son relativos al *texto* según el parámetro `angle`, por lo que "arriba a la izquierda" significa la esquina en la parte superior izquierda cuando se mira el texto horizontalmente.

En caso de error, se devuelve `false`.

## Ejemplos

Ejemplo con `imageftbbox`

```
<?php
// Creación de una imagen de 300x150 píxeles
$im = imagecreatetruecolor(300, 150);
$black = imagecolorallocate($im, 0, 0, 0);
$white = imagecolorallocate($im, 255, 255, 255);

// Define el fondo en blanco
imagefilledrectangle($im, 0, 0, 299, 299, $white);

// Ruta hacia nuestro archivo de fuente
$font = './arial.ttf';

// Primero, creamos un rectángulo que contenga nuestro texto
$bbox = imageftbbox(10, 0, $font, 'The PHP Documentation Group');

// Nuestras coordenadas en X y en Y
$x = $bbox[0] + (imagesx($im) / 2) - ($bbox[4] / 2) - 5;
$y = $bbox[1] + (imagesy($im) / 2) - ($bbox[5] / 2) - 5;

imagefttext($im, 10, 0, $x, $y, $black, $font, 'The PHP Documentation Group');

// Muestra hacia el navegador
header('Content-Type: image/png');

imagepng($im);
?>

    
```php

## Notas

> [!NOTE]
> Esta función solo está disponible si si PHP es compilado con soporte Freetype (`--with-freetype-dir=DIR`)

## Véase también

imagefttext

imagettfbbox
