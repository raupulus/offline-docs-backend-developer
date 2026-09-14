---
title: imagesetpixel
description: Dibuja un píxel
source_url: https://www.php.net/manual/es/function.imagesetpixel.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagesetpixel.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: fcd921429
order: 32350
---

imagesetpixel

Dibuja un píxel

## Descripción

```php
imagesetpixel(GdImage $image, int $x, int $y, int $color): true
```php

`imagesetpixel` dibuja un píxel en las coordenadas especificadas.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`x`  
X: coordenada.

`y`  
Y: coordenada.

`color`  
Un identificador de color creado con `imagecolorallocate`.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Ejemplo con `imagesetpixel`

Un dibujo aleatorio que termina con una imagen regular.

```
<?php

$x = 200;
$y = 200;

$gd = imagecreatetruecolor($x, $y);

$corners[0] = array('x' => 100, 'y' =>  10);
$corners[1] = array('x' =>   0, 'y' => 190);
$corners[2] = array('x' => 200, 'y' => 190);

$red = imagecolorallocate($gd, 255, 0, 0);

for ($i = 0; $i < 100000; $i++) {
  imagesetpixel($gd, round($x), round($y), $red);
  $a = rand(0, 2);
  $x = ($x + $corners[$a]['x']) / 2;
  $y = ($y + $corners[$a]['y']) / 2;
}

header('Content-Type: image/png');
imagepng($gd);

?>

    
```php

Resultado del ejemplo anterior es similar a:

![Visualización del ejemplo: imagesetpixel()](en/reference/image/figures/imagesetpixel.png)

## Véase también

imagecreatetruecolor

imagecolorallocate

imagecolorat
