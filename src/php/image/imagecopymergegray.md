---
title: imagecopymergegray
description: Copia y fusiona una parte de una imagen en niveles de gris
source_url: https://www.php.net/manual/es/function.imagecopymergegray.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecopymergegray.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 525aa5f19
order: 31720
---

imagecopymergegray

Copia y fusiona una parte de una imagen en niveles de gris

## Descripción

```php
imagecopymergegray(GdImage $dst_image, GdImage $src_image, int $dst_x, int $dst_y, int $src_x, int $src_y, int $src_width, int $src_height, int $pct): true
```php

`imagecopymergegray` copia una parte de la imagen `src_image` en la imagen de destino `dst_image` comenzando en las coordenadas (`src_x`, `src_y`), con el ancho `src_width` y la altura `src_height`. La zona de la imagen así definida será copiada en las coordenadas (`dst_x`, `dst_y`), en la imagen de destino.

`imagecopymergegray` es idéntica a la función `imagecopymerge`, excepto que durante la fusión, el "hue" de la imagen será conservado mediante la conversión de la zona en la imagen de destino a gris, antes de la operación de copia.

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
X: coordenada del punto origen.

`src_y`  
Y: coordenada del punto origen.

`src_width`  
Ancho de la fuente.

`src_height`  
Altura de la fuente.

`pct`  
El parámetro `src_image` será convertido a niveles de gris de acuerdo con el parámetro `pct` donde 0 corresponde a una conversión total a niveles de gris y 100 no modifica nada. Cuando `pct` = 100, esta función se comporta de la misma manera que la función `imagecopy` para las paletas, excepto por la ignorancia de los componentes alpha, mientras que implementa la transparencia alpha para las imágenes true colour.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `dst_image` y `src_image` ahora esperan instancias de `GdImage`; anteriormente, se esperaban `resource`s. |

## Ejemplos

Ejemplo con `imagecopymergegray`

```
<?php
// Creación de las instancias de imagen
$dest = imagecreatefromgif('php.gif');
$src = imagecreatefromgif('php.gif');

// Copia y fusiona - Gris = 20%
imagecopymergegray($dest, $src, 10, 10, 0, 0, 100, 47, 20);

// Muestra y libera la memoria
header('Content-Type: image/gif');
imagegif($dest);
?>

    
```php
