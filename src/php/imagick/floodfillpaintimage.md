---
title: Imagick::floodFillPaintImage
description: Cambia el valor del color de cualquier píxel que coincida con el objetivo
source_url: https://www.php.net/manual/es/imagick.floodfillpaintimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/floodfillpaintimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 33270
---

Imagick::floodFillPaintImage

Cambia el valor del color de cualquier píxel que coincida con el objetivo

## Descripción

```php
public Imagick::floodFillPaintImage(mixed $fill, float $fuzz, mixed $target, int $x, int $y, bool $invert, [int $channel]): bool
```php

Cambia el valor del color de cualquier píxel que coincida con el objetivo y esté en el área inmediata. Este método es un sustituto del método obsoleto `Imagick::paintFloodFillImage`. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.8 o superior.

## Parámetros

`fill`  
Objeto ImagickPixel o una cadena que contiene el color de relleno

`fuzz`  
La cantidad de polvo de papel. Por ejemplo, definir el polvo de papel a 10 y el color rojo a una intensidad de 100 y 102 no será interpretado como el mismo color.

`target`  
Objeto ImagickPixel o una cadena que contiene el color objetivo a dibujar

`x`  
Posición X del inicio del relleno

`y`  
Posición Y del inicio del relleno

`invert`  
Si es `true` se pinta cualquier píxel que no coincida con el color objetivo.

`channel`  
Proporciona una constante de canal válida para su modo de canal. Para aplicarlo a más de un canal, combínense las [constantes de canales](#imagick.constants.channel) utilizando un operador a nivel de bits. Por defecto, vale `Imagick::CHANNEL_DEFAULT`. Consúltese la lista de [constantes de canales](#imagick.constants.channel)

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Ejemplo de Imagick::floodfillPaintImage

```
<?php

/* Crear un nuevo objeto imagick */
$im = new Imagick();

/* Crear imágenes de color rojo, verde y azul */
$im->newImage(100, 50, "red");
$im->newImage(100, 50, "green");
$im->newImage(100, 50, "blue");

/* Añadir las imágenes para que sean una */
$im->resetIterator();
$combinado = $im->appendImages(true);

/* Guardar la imagen intermedia para la comparación */
$combinado->writeImage("floodfillpaint_intermedia.png");

/* El píxel objetivo a pintar */
$x = 1;
$y = 1;

/* Obtener el color con el que vamos a pintar */
$objetivo = $combinado->getImagePixelColor($x, $y);

/* Pinta el píxel en la posición 1,1 negro y todos los píxeles
   cercanos que coincidan con el color objetivo */
$combinado->floodfillPaintImage("black", 1, $objetivo, $x, $y, false);

/* Guardar el resultado */
$combinado->writeImage("floodfillpaint_resultado.png");
?>

    
```php

Resultado del ejemplo anterior es similar a:

![Salida del ejemplo : Imagick::floodfillPaintImage()](en/reference/imagick/figures/floodfillpaint_intermediate.png)
