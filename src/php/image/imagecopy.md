---
title: imagecopy
description: Copia una parte de una imagen
source_url: https://www.php.net/manual/es/function.imagecopy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecopy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: fcd921429
order: 31700
---

imagecopy

Copia una parte de una imagen

## Descripción

```php
imagecopy(GdImage $dst_image, GdImage $src_image, int $dst_x, int $dst_y, int $src_x, int $src_y, int $src_width, int $src_height): true
```php

Copia una parte de la imagen `src_image` a la imagen de destino `dst_image`, comenzando en las coordenadas `src_x`, `src_y` y con un ancho de `src_width` y una altura de `src_height`. La porción así definida será copiada y colocada en las coordenadas `dst_x` y `dst_y`.

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

`src_width`  
Ancho de la fuente.

`src_height`  
Altura de la fuente.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `dst_image` y `src_image` ahora requieren instancias de `GdImage`; anteriormente se esperaban `resource`s. |

## Ejemplos

Se recorta el logo PHP.net

```
<?php
// Creación de las instancias de imagen
$src = imagecreatefromgif('php.gif');
$dest = imagecreatetruecolor(80, 40);

// Copia
imagecopy($dest, $src, 0, 0, 20, 13, 80, 40);

// Visualización y liberación de la memoria
header('Content-Type: image/gif');
imagegif($dest);
?>

   
```php

Resultado del ejemplo anterior es similar a:

![Visualización del ejemplo: Copia una parte del logo PHP.net](en/reference/image/figures/imagecopy.gif)

## Véase también

imagecrop
