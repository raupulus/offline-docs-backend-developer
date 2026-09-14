---
title: imagecrop
description: Recorta una imagen en el rectángulo dado
source_url: https://www.php.net/manual/es/function.imagecrop.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecrop.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: 9960a09a5
order: 31910
---

imagecrop

Recorta una imagen en el rectángulo dado

## Descripción

```php
imagecrop(GdImage $image, array $rectangle): GdImage
```php

Recorta una imagen en la zona rectangular dada y devuelve la imagen resultante. La `image` no se modifica.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`rectangle`  
`array` que contiene las claves `x`, `y`, `width` y `height`.

## Valores devueltos

Devuelve el objeto de la imagen recortada en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |
| 8.0.0 | En caso de éxito, esta función devuelve ahora una instancia de `GDImage`; anteriormente, se devolvía un `resource`. |

## Ejemplos

Ejemplo con `imagecrop`

Este ejemplo muestra cómo recortar una imagen en una zona cuadrada.

```
<?php
$im = imagecreatefrompng('example.png');
$size = min(imagesx($im), imagesy($im));
$im2 = imagecrop($im, ['x' => 0, 'y' => 0, 'width' => $size, 'height' => $size]);
if ($im2 !== FALSE) {
    imagepng($im2, 'example-cropped.png');
}
?>

   
```php

## Véase también

imagecropauto
