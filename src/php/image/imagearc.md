---
title: imagearc
description: Dibuja una elipse parcial
source_url: https://www.php.net/manual/es/function.imagearc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagearc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: fcd921429
order: 31480
---

imagearc

Dibuja una elipse parcial

## Descripción

```php
imagearc(GdImage $image, int $center_x, int $center_y, int $width, int $height, int $start_angle, int $end_angle, int $color): true
```php

`imagearc` dibuja una elipse parcial, centrada en las coordenadas proporcionadas.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`center_x`  
X: coordenada del centro.

`center_y`  
Y: coordenada del centro.

`width`  
El ancho de la elipse.

`height`  
La altura de la elipse.

`start_angle`  
El ángulo de inicio de la elipse, en grados.

`end_angle`  
El ángulo de fin de la elipse, en grados. 0° corresponde a la posición "tres horas" y la elipse es dibujada en el sentido de las agujas de un reloj.

`color`  
Un identificador de color creado con `imagecolorallocate`.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Dibujar un círculo con `imagearc`

```
<?php

// Creación de una imagen 200*200
$img = imagecreatetruecolor(200, 200);

// Asignación de colores
$white = imagecolorallocate($img, 255, 255, 255);
$red   = imagecolorallocate($img, 255,   0,   0);
$green = imagecolorallocate($img,   0, 255,   0);
$blue  = imagecolorallocate($img,   0,   0, 255);

// Dibujar la cabeza
imagearc($img, 100, 100, 200, 200,  0, 360, $white);
// La boca
imagearc($img, 100, 100, 150, 150, 25, 155, $red);
// Los ojos izquierdo y derecho
imagearc($img,  60,  75,  50,  50,  0, 360, $green);
imagearc($img, 140,  75,  50,  50,  0, 360, $blue);

// Mostrar en el navegador
header("Content-type: image/png");
imagepng($img);

?>

    
```php

Resultado del ejemplo anterior es similar a:

![Visualización del ejemplo: Dibujar un círculo con imagearc()](en/reference/image/figures/imagearc.png)

## Véase también

imagefilledarc

imageellipse

imagefilledellipse
