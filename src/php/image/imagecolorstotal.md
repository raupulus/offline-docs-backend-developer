---
title: imagecolorstotal
description: Calcula el número de colores de una paleta
source_url: https://www.php.net/manual/es/function.imagecolorstotal.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecolorstotal.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 9960a09a5
order: 31670
---

imagecolorstotal

Calcula el número de colores de una paleta

## Descripción

```php
imagecolorstotal(GdImage $image): int
```php

Devuelve el número de colores de la paleta de la imagen.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

## Valores devueltos

Devuelve el número de colores de la paleta para la imagen `image` o 0 para las imágenes truecolor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Obtención del número total de colores en una imagen utilizando la función `imagecolorstotal`

```
<?php
// Creación de una instancia de imagen
$im = imagecreatefromgif('php.gif');

echo 'Número total de colores en la imagen : ' . imagecolorstotal($im);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Número total de colores en la imagen : 128

## Véase también

imagecolorat

imagecolorsforindex

imageistruecolor
