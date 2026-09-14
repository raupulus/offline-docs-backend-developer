---
title: imagefttext
description: Escribe texto en una imagen con la fuente actual FreeType 2
source_url: https://www.php.net/manual/es/function.imagefttext.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagefttext.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: 9960a09a5
order: 32070
---

imagefttext

Escribe texto en una imagen con la fuente actual FreeType 2

## Descripción

```php
imagefttext(GdImage $image, float $size, float $angle, int $x, int $y, int $color, string $font_filename, string $text, [array $options]): array
```php

> [!NOTE]
> Antes de PHP 8.0.0, `imagefttext` era una variante extendida de `imagettftext` que además soporta `extrainfo`. A partir de PHP 8.0.0, `imagefttext` es un alias de `imagettftext`.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`size`  
El tamaño de la fuente a utilizar, en número de puntos.

`angle`  
El ángulo, en grados; 0 grados para una lectura del texto de izquierda a derecha. Los grandes valores representan una rotación en el sentido de las agujas de un reloj. Por ejemplo, un valor de 90 tendrá como efecto leer el texto de abajo hacia arriba.

`x`  
Las coordenadas, proporcionadas por `x` y `y` definen el punto de inicio del primer carácter (y más precisamente, la esquina en la parte inferior izquierda del carácter). Este es un comportamiento diferente de la función `imagestring`, donde `x` y `y` definen la esquina superior, a la izquierda del primer carácter. Por ejemplo, en la parte superior izquierda vale 0, 0.

`y`  
La ordenada `y-ordinate`. Este parámetro configura la posición base de la fuente, y no la parte inferior de esta última.

`color`  
El índice del color deseado para el texto, ver la función `imagecolorexact`.

`font_filename`  
La ruta hacia la fuente TrueType a utilizar.

Dependiendo de la versión de GD utilizada por PHP, se buscarán los ficheros *que no comienzan con un '`/`', añadiendo la extensión '`.ttf`'*, y siguiendo la ruta de las fuentes definida por la biblioteca.

En la mayoría de los casos, cuando la fuente se encuentra en el mismo directorio que el script que intenta utilizarla, la siguiente solución permite evitar todos los problemas relativos a la inclusión.

```
<?php
// Define la variable de entorno para GD
putenv('GDFONTPATH=' . realpath('.'));

// Nombre de la fuente a utilizar (nota que no hay extensión .ttf)
$font = 'SomeFont';
?>

       
```php

`text`  
El texto a insertar en la imagen.

`options`  
| Clave         | Tipo    | Significado                                 |
|---------------|---------|---------------------------------------------|
| `linespacing` | `float` | Define el espaciado entre líneas al dibujar |

Índices posibles para el array `options`

## Valores devueltos

Esta función devuelve un array que define los 4 puntos de una caja, comenzando por la esquina inferior, a la izquierda, luego, los siguientes, en el sentido de las agujas de un reloj:

|     |                                                     |
|-----|-----------------------------------------------------|
| 0   | x : coordenada en la parte inferior, a la izquierda |
| 1   | y : coordenada en la parte inferior, a la izquierda |
| 2   | x : coordenada en la parte inferior, a la derecha   |
| 3   | y : coordenada en la parte inferior, a la derecha   |
| 4   | x : coordenada en la parte superior, a la derecha   |
| 5   | y : coordenada en la parte superior, a la derecha   |
| 6   | x : coordenada en la parte superior, a la izquierda |
| 7   | y : coordenada en la parte superior, a la izquierda |

En caso de error, `false` es devuelto.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Ejemplo con `imagefttext`

```
<?php
// Creación de una imagen de 300x100 píxeles
$im = imagecreatetruecolor(300, 100);
$red = imagecolorallocate($im, 0xFF, 0x00, 0x00);
$black = imagecolorallocate($im, 0x00, 0x00, 0x00);

// Define el fondo en rojo
imagefilledrectangle($im, 0, 0, 299, 99, $red);

// Ruta hacia nuestro fichero de fuente ttf
$font_file = './arial.ttf';

// Dibuja el texto 'PHP Manual' utilizando una fuente de tamaño 13
imagefttext($im, 13, 0, 105, 55, $black, $font_file, 'PHP Manual');

// Muestra la imagen en el navegador
header('Content-Type: image/png');

imagepng($im);
?>

    
```php

## Notas

> [!NOTE]
> Esta función solo está disponible si si PHP es compilado con soporte Freetype (`--with-freetype-dir=DIR`)

## Véase también

imageftbbox

imagettftext
