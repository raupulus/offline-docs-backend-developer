---
title: imagettfbbox
description: Devuelve el rectángulo que rodea un texto dibujado con una fuente TrueType
source_url: https://www.php.net/manual/es/function.imagettfbbox.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagettfbbox.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: 525aa5f19
order: 32440
---

imagettfbbox

Devuelve el rectángulo que rodea un texto dibujado con una fuente TrueType

## Descripción

```php
imagettfbbox(float $size, float $angle, string $font_filename, string $string, [array $options]): array
```php

Calcula y devuelve el rectángulo que rodea el texto `text`, escrito con una fuente TrueType.

> [!NOTE]
> Antes de PHP 8.0.0, `imageftbbox` era una variante extendida de `imagettfbbox` que además soporta `extrainfo`. A partir de PHP 8.0.0, `imagettfbbox` es un alias de `imageftbbox`.

## Parámetros

`size`  
El tamaño de la fuente en puntos.

`angle`  
El ángulo, en grados, en el que el parámetro `string` será medido.

`fontfile`  
La ruta de acceso al fichero de la fuente TrueType que desea utilizar.

Dependiendo de qué versión de la biblioteca GD esté utilizando PHP, *cuando `fontfile` no comienza con una barra diagonal inicial `/` entonces `.ttf` será añadido* al nombre del fichero y la biblioteca intentará buscar ese nombre de fichero a lo largo de una ruta de acceso de fuentes definida por la biblioteca.

Al utilizar versiones de la biblioteca GD inferiores a 2.0.18, un carácter `espacio`, en lugar de un punto y coma, se utilizaba como 'separador de rutas' para diferentes ficheros de fuentes. El uso no intencional de esta característica resultará en el mensaje de advertencia: `Advertencia: No se pudo encontrar/abrir la fuente`. Para estas versiones afectadas, la única solución es mover la fuente a una ruta que no contenga espacios.

En muchos casos donde una fuente reside en el mismo directorio que el script que la utiliza, el siguiente truco aliviará cualquier problema de inclusión.

```
<?php
// Set the environment variable for GD
putenv('GDFONTPATH=' . realpath('.'));

// Name the font to be used (note the lack of the .ttf extension)
$font = 'SomeFont';
?>

       
```php

> [!NOTE]
> Tenga en cuenta que [open_basedir](#ini.open-basedir) no *aplica* a `fontfile`.

`string`  
La cadena a medir.

`options`  
Similar a `imagettftext`.

## Valores devueltos

`imagettfbbox` devuelve un array con 8 elementos representando los 4 vértices del rectángulo en caso de éxito, `false` si ocurre un error.

| Clave | Significado                          |
|-------|--------------------------------------|
| 0     | Esquina inferior izquierda, abscisa  |
| 1     | Esquina inferior izquierda, ordenada |
| 2     | Esquina inferior derecha, abscisa    |
| 3     | Esquina inferior derecha, ordenada   |
| 4     | Esquina superior derecha, abscisa    |
| 5     | Esquina superior derecha, ordenada   |
| 6     | Esquina superior izquierda, abscisa  |
| 7     | Esquina superior izquierda, ordenada |

Las posiciones de los puntos son relativas al texto *text*, independientemente del ángulo: esquina superior izquierda hace referencia a la esquina superior izquierda del texto escrito horizontalmente.

## Historial de cambios

| Versión | Descripción                             |
|---------|-----------------------------------------|
| 8.0.0   | El parámetro `options` ha sido añadido. |

## Ejemplos

Ejemplo con `imagettfbbox`

```
<?php
// Creación de una imagen de 300x150 píxeles
$im = imagecreatetruecolor(300, 150);
$black = imagecolorallocate($im, 0, 0, 0);
$white = imagecolorallocate($im, 255, 255, 255);

// Define el fondo en blanco
imagefilledrectangle($im, 0, 0, 299, 299, $white);

// Ruta al archivo de la fuente
$font = './arial.ttf';

// Primero, creamos nuestro rectángulo que rodea nuestro primer texto
$bbox = imagettfbbox(10, 45, $font, 'Powered by PHP ' . phpversion());

// Nuestras coordenadas en X y en Y
$x = $bbox[0] + (imagesx($im) / 2) - ($bbox[4] / 2) - 25;
$y = $bbox[1] + (imagesy($im) / 2) - ($bbox[5] / 2) - 5;

// Dibujo del texto
imagettftext($im, 10, 45, $x, $y, $black, $font, 'Powered by PHP ' . phpversion());

// Creamos nuestro rectángulo que rodea nuestro segundo texto
$bbox = imagettfbbox(10, 45, $font, 'and Zend Engine ' . zend_version());

// Define las coordenadas para que el segundo texto siga al primero
$x = $bbox[0] + (imagesx($im) / 2) - ($bbox[4] / 2) + 10;
$y = $bbox[1] + (imagesy($im) / 2) - ($bbox[5] / 2) - 5;

// Dibujo del texto
imagettftext($im, 10, 45, $x, $y, $black, $font, 'and Zend Engine ' . zend_version());

// Envío al navegador
header('Content-Type: image/png');

imagepng($im);
?>

    
```php

## Notas

> [!NOTE]
> Esta función solo está disponible si si PHP es compilado con soporte Freetype (`--with-freetype-dir=DIR`)

## Véase también

imagettftext

imageftbbox
