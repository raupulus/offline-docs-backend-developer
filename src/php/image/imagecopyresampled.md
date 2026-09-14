---
title: imagecopyresampled
description: Copia, redimensiona y reinterpolación de una imagen
source_url: https://www.php.net/manual/es/function.imagecopyresampled.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecopyresampled.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 16b6c3466
order: 31730
---

imagecopyresampled

Copia, redimensiona y reinterpolación de una imagen

## Descripción

```php
imagecopyresampled(GdImage $dst_image, GdImage $src_image, int $dst_x, int $dst_y, int $src_x, int $src_y, int $dst_width, int $dst_height, int $src_width, int $src_height): true
```php

`imagecopyresampled` copia una zona rectangular de la imagen `src_im` hacia la imagen `dst_im`. Durante la copia, la zona es reinterpolada para mantener la claridad de la imagen durante una reducción.

En otras palabras, `imagecopyresampled` tomará una forma rectangular `src_image` de un ancho de `src_width` y una altura `src_height` en la posición (`src_x`,`src_y`) y la colocará en una zona rectangular `dst_image` de un ancho de `dst_width` y una altura de `dst_height` en la posición (`dst_x`,`dst_y`).

Si las alturas y anchos de origen y destino difieren, la imagen copiada será estirada de manera apropiada. Las coordenadas son las del ángulo superior izquierdo. `imagecopyresampled` puede usarse para copiar zonas de una imagen hacia sí misma, (si `dst_image` es la misma que `src_image`) pero si las regiones se superponen, los resultados son impredecibles.

## Parámetros

`dst_image`  
Recurso de imagen de destino.

`src_image`  
Recurso de imagen de origen.

`dst_x`  
X: coordenadas del punto de destino.

`dst_y`  
Y: coordenadas del punto de destino.

`src_x`  
X: coordenadas del punto origen.

`src_y`  
Y: coordenadas del punto origen.

`dst_width`  
Ancho del destino.

`dst_height`  
Altura del destino.

`src_width`  
Ancho de la fuente.

`src_height`  
Altura de la fuente.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | El tipo de retorno es ahora `true`; anteriormente, era `bool`. |
| 8.0.0 | `dst_image` y `src_image` ahora esperan instancias de `GdImage`; anteriormente, se esperaban `resource`s. |

## Ejemplos

Ejemplo simple

Este ejemplo redimensiona una imagen a la mitad de su tamaño original.

```
<?php
// El archivo
$filename = 'test.jpg';
$percent = 0.5;

// Tipo de contenido
header('Content-Type: image/jpeg');

// Cálculo de las nuevas dimensiones
list($width, $height) = getimagesize($filename);
$new_width = $width * $percent;
$new_height = $height * $percent;

// Redimensionamiento
$image_p = imagecreatetruecolor($new_width, $new_height);
$image = imagecreatefromjpeg($filename);
imagecopyresampled($image_p, $image, 0, 0, 0, 0, $new_width, $new_height, $width, $height);

// Mostrar
imagejpeg($image_p, null, 100);
?>

    
```php

Resultado del ejemplo anterior es similar a:

![](en/reference/image/figures/imagecopyresampled.jpg)

Redimensionamiento proporcional de una imagen

Este ejemplo mostrará una imagen con un ancho o altura máxima de 200 píxeles.

```
<?php
// El archivo
$filename = 'test.jpg';

// Definición del ancho y altura máxima
$width = 200;
$height = 200;

// Tipo de contenido
header('Content-Type: image/jpeg');

// Cálculo de las nuevas dimensiones
list($width_orig, $height_orig) = getimagesize($filename);

$ratio_orig = $width_orig/$height_orig;

if ($width/$height > $ratio_orig) {
   $width = $height*$ratio_orig;
} else {
   $height = $width/$ratio_orig;
}

// Redimensionamiento
$image_p = imagecreatetruecolor($width, $height);
$image = imagecreatefromjpeg($filename);
imagecopyresampled($image_p, $image, 0, 0, 0, 0, $width, $height, $width_orig, $height_orig);

// Mostrar
imagejpeg($image_p, null, 100);
?>

    
```php

Resultado del ejemplo anterior es similar a:

![Visualización del ejemplo: Reinterpolación de una imagen proporcionalmente](en/reference/image/figures/imagecopyresampled_2.jpg)

## Notas

> [!NOTE]
> Existe un problema debido a las limitaciones del tamaño de la paleta (255 + 1 colores diferentes). Filtrar o reinterpolar una imagen requiere más de 255 colores, entonces se usa una aproximación para calcular el nuevo número de colores. Con una paleta, si un nuevo color no puede ser asignado, se usa el color más cercano (en teoría). Esto no siempre es el color más cercano visualmente. Esto puede generar problemas extraños, como imágenes blancas. Para evitar este problema, convierta la imagen a TrueColor, como la generada por la función `imagecreatetruecolor`.

## Véase también

imagecopyresized

imagescale

imagecrop
