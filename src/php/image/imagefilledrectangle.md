---
title: imagefilledrectangle
description: Dibuja un rectángulo relleno
source_url: https://www.php.net/manual/es/function.imagefilledrectangle.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagefilledrectangle.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: fcd921429
order: 32000
---

imagefilledrectangle

Dibuja un rectángulo relleno

## Descripción

```php
imagefilledrectangle(GdImage $image, int $x1, int $y1, int $x2, int $y2, int $color): true
```php

Dibuja un rectángulo de color `color` en la imagen `image`, comenzando por el vértice superior izquierdo (1) y finalizando en el vértice inferior derecho (2). La esquina superior izquierda es el origen (0, 0).

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`x1`  
X: coordenada del punto 1.

`y1`  
Y: coordenada del punto 1.

`x2`  
X: coordenada del punto 2.

`y2`  
Y: coordenada del punto 2.

`color`  
El color de relleno. Un identificador de color creado con `imagecolorallocate`.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Ejemplo con `imagefilledrectangle`

```
<?php
// Creación de una imagen de 55x30 píxeles
$im = imagecreatetruecolor(55, 30);
$white = imagecolorallocate($im, 255, 255, 255);

// Dibuja un rectángulo blanco
imagefilledrectangle($im, 4, 4, 50, 25, $white);

// Guarda la imagen
imagepng($im, './imagefilledrectangle.png');
?>

    
```php

Resultado del ejemplo anterior es similar a:

![Visualización del ejemplo: imagefilledrectangle()](en/reference/image/figures/imagefilledrectangle.png)
