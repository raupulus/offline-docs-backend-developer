---
title: imagecopymerge
description: Copia y fusiona una parte de una imagen
source_url: https://www.php.net/manual/es/function.imagecopymerge.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecopymerge.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 525aa5f19
order: 31710
---

imagecopymerge

Copia y fusiona una parte de una imagen

## Descripción

```php
imagecopymerge(GdImage $dst_image, GdImage $src_image, int $dst_x, int $dst_y, int $src_x, int $src_y, int $src_width, int $src_height, int $pct): true
```php

Copia una parte de la imagen `src_image` en la imagen de destino `dst_image` comenzando en las coordenadas (`src_x`, `src_y`), con el ancho `src_width` y la altura `src_height`. La zona de la imagen así definida será copiada en las coordenadas (`dst_x`, `dst_y`), en la imagen de destino.

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
Las dos imágenes serán fusionadas según el argumento `pct`, que puede valer de 0 a 100. Si `pct` = 0, no se realiza ninguna acción, mientras que si `pct` = 100, `imagecopymerge` se comporta exactamente como `imagecopy` para las imágenes de paleta, excepto por la ignorancia de los componentes alpha, mientras que implementa la transparencia alpha para las imágenes en color verdadero.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `dst_image` y `src_image` ahora esperan instancias de `GdImage`; anteriormente, se esperaban `resource`s. |

## Ejemplos

Fusiona 2 copias del logo PHP.net con 75% de transparencia

```
<?php
// Creación de las instancias de imagen
$dest = imagecreatefromgif('php.gif');
$src = imagecreatefromgif('php.gif');

// Copia y fusiona
imagecopymerge($dest, $src, 10, 10, 0, 0, 100, 47, 75);

// Mostrar y liberar la memoria
header('Content-Type: image/gif');
imagegif($dest);
?>

    
```php
