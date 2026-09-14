---
title: imagefilledarc
description: Dibuja un arco parcial y lo rellena
source_url: https://www.php.net/manual/es/function.imagefilledarc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagefilledarc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: fcd921429
order: 31970
---

imagefilledarc

Dibuja un arco parcial y lo rellena

## Descripción

```php
imagefilledarc(GdImage $image, int $center_x, int $center_y, int $width, int $height, int $start_angle, int $end_angle, int $color, int $style): true
```php

Dibuja un arco parcial, centrado en las coordenadas especificadas en la imagen proporcionada.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`center_x`  
X: coordenada del centro.

`center_y`  
Y: coordenada del centro.

`width`  
El ancho del arco.

`height`  
La altura del arco.

`start_angle`  
El ángulo de inicio del arco, en grados.

`end_angle`  
El ángulo de fin del arco, en grados. 0° se encuentra en la posición de las 3 en punto en un reloj, y el arco se dibuja en el sentido de las agujas del reloj.

`color`  
Un identificador de color creado con `imagecolorallocate`.

`style`  
Un campo de bytes, combinado con el operador OR:

1.  `IMG_ARC_PIE`

2.  `IMG_ARC_CHORD`

3.  `IMG_ARC_NOFILL`

4.  `IMG_ARC_EDGED`

`IMG_ARC_PIE` y `IMG_ARC_CHORD` son mutuamente excluyentes; `IMG_ARC_CHORD` solo conecta los ángulos de inicio y fin con una línea recta, mientras que `IMG_ARC_PIE` produce una línea curva. `IMG_ARC_NOFILL` indica que el arco (o cuerda) debe ser dibujado pero no rellenado. `IMG_ARC_EDGED`, usado junto con `IMG_ARC_NOFILL`, indica que los ángulos de inicio y fin deben ser conectados al centro. Esta función es recomendada para crear gráficos de tipo pastel.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Creación de un gráfico de pastel en 3D

```
<?php

// Creación de la imagen
$image = imagecreatetruecolor(100, 100);

// Asignación de algunas colores
$white    = imagecolorallocate($image, 0xFF, 0xFF, 0xFF);
$gray     = imagecolorallocate($image, 0xC0, 0xC0, 0xC0);
$darkgray = imagecolorallocate($image, 0x90, 0x90, 0x90);
$navy     = imagecolorallocate($image, 0x00, 0x00, 0x80);
$darknavy = imagecolorallocate($image, 0x00, 0x00, 0x50);
$red      = imagecolorallocate($image, 0xFF, 0x00, 0x00);
$darkred  = imagecolorallocate($image, 0x90, 0x00, 0x00);

// Creación del efecto 3D
for ($i = 60; $i > 50; $i--) {
   imagefilledarc($image, 50, $i, 100, 50, 0, 45, $darknavy, IMG_ARC_PIE);
   imagefilledarc($image, 50, $i, 100, 50, 45, 75 , $darkgray, IMG_ARC_PIE);
   imagefilledarc($image, 50, $i, 100, 50, 75, 360 , $darkred, IMG_ARC_PIE);
}

imagefilledarc($image, 50, 50, 100, 50, 0, 45, $navy, IMG_ARC_PIE);
imagefilledarc($image, 50, 50, 100, 50, 45, 75 , $gray, IMG_ARC_PIE);
imagefilledarc($image, 50, 50, 100, 50, 75, 360 , $red, IMG_ARC_PIE);

// Mostrar la imagen
header('Content-type: image/png');
imagepng($image);
?>

    
```php

Resultado del ejemplo anterior es similar a:

![Visualización del ejemplo: Creación de un gráfico 3D](en/reference/image/figures/imagefilledarc.png)
