---
title: Imagick::importImagePixels
description: Importa los píxeles de una imagen
source_url: https://www.php.net/manual/es/imagick.importimagepixels.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/importimagepixels.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 04a0c156e
order: 34360
---

Imagick::importImagePixels

Importa los píxeles de una imagen

## Descripción

```php
public Imagick::importImagePixels(int $x, int $y, int $width, int $height, string $map, int $storage, array $pixels): bool
```php

Importa los píxeles desde una matriz a un imagen. El mapa `map` normalmete es 'RGB'. Este método impone las siguientes limitaciones para los parámetros: la cantidad de píxeles en la matriz debe coincidir con `width` x `height` x longitud del mapa. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.5 o superior.

## Parámetros

`x`  
La posición x de la imagen

`y`  
La posición y de la imagen

`width`  
El ancho de la imagen

`height`  
El alto de la imagen

`map`  
Mapa de píxeles ordenados, como una cadena. Esto puede ser por ejemplo `RGB`. El valor puede ser cualquier combinación u orden de R = rojo, G = verde, B = azul, A = alfa (0 es transparente), O = opacidad (0 es opaco), C = cian, Y = amarillo, M = magenta, K = negro, I = intensidad (para escala de grises), P = relleno.

`storage`  
El método de almacenamiento de los píxeles. Consulte esta lista de [constantes de píxel](#imagick.constants.pixel).

`pixels`  
La matriz de píxeles

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Ejemplo deImagick::importImagePixels

```
<?php

/* Generar una matriz de píxeles. 2000 píxeles por raya de color */
$cuenta = 2000 * 3;

$píxeles =
   array_merge(array_pad(array(), $cuenta, 0),
               array_pad(array(), $cuenta, 255),
               array_pad(array(), $cuenta, 0),
               array_pad(array(), $cuenta, 255),
               array_pad(array(), $cuenta, 0));

/* Ancho y alto. El área es la cantidad de píxeles dividido
   por tres. Tres viene de 'RGB', tres valores por píxel */
$ancho = $alto = pow((count($píxeles) / 3), 0.5);

/* Crear una imagen vacía */
$im = new Imagick();
$im->newImage($ancho, $alto, 'gray');

/* Importar los píxeles a la imagen.
   ancho * alto * strlen("RGB") debe coincidir con count($píxeles) */
$im->importImagePixels(0, 0, $ancho, $alto, "RGB", Imagick::PIXEL_CHAR, $píxeles);

/* Imprimir como una imagen jpeg */
$im->setImageFormat('jpg');
header("Content-Type: image/jpg");
echo $im;

?>

    
```php

Resultado del ejemplo anterior es similar a:

![Salida del ejemplo : Imagick::importImagePixels()](en/reference/imagick/figures/importimagepixels.jpg)
