---
title: imagefilltoborder
description: Rellena una región con un color específico
source_url: https://www.php.net/manual/es/function.imagefilltoborder.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagefilltoborder.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: 525aa5f19
order: 32010
---

imagefilltoborder

Rellena una región con un color específico

## Descripción

```php
imagefilltoborder(GdImage $image, int $x, int $y, int $border_color, int $color): true
```php

`imagefilltoborder` rellena con el color `color` toda la región dentro de la región limitada por el color `border_color`. El punto de partida es (`x`, `y`) (la esquina superior izquierda es el origen (0,0)) y el color de la región es `color`.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`x`  
X: coordenada de inicio.

`y`  
Y: coordenada de inicio.

`border_color`  
El color del borde. Un identificador de color creado con `imagecolorallocate`.

`color`  
El color de relleno. Un identificador de color creado con `imagecolorallocate`.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Relleno de una elipse con un color

```
<?php
// Creación de un gestor de imagen, luego define el color de fondo
// a blanco
$im = imagecreatetruecolor(100, 100);
imagefilledrectangle($im, 0, 0, 100, 100, imagecolorallocate($im, 255, 255, 255));

// Dibuja una elipse cuyos bordes serán negros
imageellipse($im, 50, 50, 50, 50, imagecolorallocate($im, 0, 0, 0));

// Define el borde y rellena la elipse del color elegido
$border = imagecolorallocate($im, 0, 0, 0);
$fill = imagecolorallocate($im, 255, 0, 0);

// Rellena la selección
imagefilltoborder($im, 50, 50, $border, $fill);

// Visualización y liberación de la memoria
header('Content-type: image/png');
imagepng($im);
?>

    
```php

Resultado del ejemplo anterior es similar a:

![Visualización del ejemplo: imagefilltoborder()](en/reference/image/figures/imagefilltoborder.png)

## Notas

El algoritmo no recuerda explícitamente qué píxeles ya han sido definidos, sino que lo infiere a partir del color del píxel, por lo que no puede distinguir entre un píxel que acaba de ser definido y un píxel que ya estaba presente. Esto significa que elegir cualquier color de relleno que ya esté presente en la imagen puede producir resultados no deseados.
