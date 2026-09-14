---
title: imagecopyresized
description: Copia y redimensiona una parte de una imagen
source_url: https://www.php.net/manual/es/function.imagecopyresized.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecopyresized.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: fcd921429
order: 31740
---

imagecopyresized

Copia y redimensiona una parte de una imagen

## Descripción

```php
imagecopyresized(GdImage $dst_image, GdImage $src_image, int $dst_x, int $dst_y, int $src_x, int $src_y, int $dst_width, int $dst_height, int $src_width, int $src_height): true
```php

`imagecopyresized` copia una parte rectangular de una imagen en otra imagen de destino. `dst_image` es la imagen de destino, `src_image` es la imagen fuente.

En otras palabras, `imagecopyresized` tomará una forma rectangular `src_image` de un ancho de `src_width` y una altura `src_height` en la posición (`src_x`,`src_y`) y la colocará en una zona rectangular `dst_image` de un ancho de `dst_width` y una altura de `dst_height` en la posición (`dst_x`,`dst_y`).

Si las dimensiones de la fuente y el destino no son iguales, se realiza un estiramiento adecuado para hacer coincidir las dos. Las coordenadas proporcionadas se definen en relación con la esquina superior izquierda. Esta función puede ser utilizada para copiar regiones dentro de una misma imagen (si `dst_image` y `src_image` son idénticas), pero si las regiones se superponen, el resultado podría ser inconsistente.

## Parámetros

`dst_image`  
Recurso de imagen de destino.

`src_image`  
Recurso de imagen de origen.

`dst_x`  
X: coordenada del punto de destino.

`dst_y`  
Y: coordenada del punto de destino.

`src_x`  
X: coordenada del punto fuente.

`src_y`  
Y: coordenada del punto fuente.

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
| 8.0.0 | `dst_image` y `src_image` ahora esperan instancias de `GdImage`; anteriormente, se esperaban `resource`s. |

## Ejemplos

Redimensionamiento de una imagen

Este ejemplo mostrará la imagen redimensionada a la mitad de su tamaño original.

```
<?php
// Archivo y nuevo tamaño
$filename = 'test.jpg';
$percent = 0.5;

// Tipo de contenido
header('Content-Type: image/jpeg');

// Cálculo de las nuevas dimensiones
list($width, $height) = getimagesize($filename);
$newwidth = $width * $percent;
$newheight = $height * $percent;

// Carga
$thumb = imagecreatetruecolor($newwidth, $newheight);
$source = imagecreatefromjpeg($filename);

// Redimensionamiento
imagecopyresized($thumb, $source, 0, 0, 0, 0, $newwidth, $newheight, $width, $height);

// Mostrar
imagejpeg($thumb);
?>

    
```php

Resultado del ejemplo anterior es similar a:

![Visualización del ejemplo: imagecopyresized()](en/reference/image/figures/imagecopyresized.jpg)

La imagen mostrada tendrá la mitad del tamaño de la imagen original, pero una mejor calidad puede obtenerse utilizando la función `imagecopyresampled`.

## Notas

> [!NOTE]
> Existe un problema debido a las limitaciones del tamaño de la paleta (255 + 1 colores diferentes). Filtrar o reescalar una imagen requiere más de 255 colores, entonces se utiliza una aproximación para calcular el nuevo número de colores. Con una paleta, si un nuevo color no puede ser asignado, se utiliza el color más cercano (en teoría); esto no siempre es el más cercano visualmente. Esto puede generar problemas extraños, como imágenes blancas. Para evitar este problema, convierta a imágenes TrueColor, como las generadas por la función `imagecreatetruecolor`.

## Véase también

imagecopyresampled

imagescale

imagecrop
