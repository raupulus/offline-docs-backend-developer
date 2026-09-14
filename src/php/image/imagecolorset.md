---
title: imagecolorset
description: Cambia el color en una paleta en el índice dado
source_url: https://www.php.net/manual/es/function.imagecolorset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecolorset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: c21abf213
order: 31650
---

imagecolorset

Cambia el color en una paleta en el índice dado

## Descripción

```php
imagecolorset(GdImage $image, int $color, int $red, int $green, int $blue, [int $alpha]): false
```php

Permite asignar a un índice de una paleta un color específico. Es una función muy práctica para realizar relleno de color sin hacerlo realmente.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`color`  
Un índice de la paleta.

`red`  
Valor del componente rojo.

`green`  
Valor del componente verde.

`blue`  
Valor del componente azul.

`alpha`  
Valor del componente alpha.

## Valores devueltos

La función devuelve `null` en caso de éxito, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Ejemplo con `imagecolorset`

```
<?php
// Creación de una imagen de 300x100 píxeles
$im = imagecreate(300, 100);

// Define el color de fondo a rojo
imagecolorallocate($im, 255, 0, 0);

// Obtención del índice del color de fondo
$bg = imagecolorat($im, 0, 0);

// Define el color de fondo a azul
imagecolorset($im, $bg, 0, 0, 255);

// Muestra la imagen en el navegador
header('Content-Type: image/png');

imagepng($im);
?>

    
```php

## Véase también

imagecolorat
