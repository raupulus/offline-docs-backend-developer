---
title: imageellipse
description: Dibuja una elipse
source_url: https://www.php.net/manual/es/function.imageellipse.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imageellipse.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: fcd921429
order: 31950
---

imageellipse

Dibuja una elipse

## Descripción

```php
imageellipse(GdImage $image, int $center_x, int $center_y, int $width, int $height, int $color): true
```php

Dibuja una elipse centrada en el punto especificado.

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

`color`  
El color de la elipse. Un identificador de color creado con `imagecolorallocate`.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Ejemplo con `imageellipse`

```
<?php
// Creación de una imagen vacía
$image = imagecreatetruecolor(400, 300);

// Selección del color de fondo
$bg = imagecolorallocate($image, 0, 0, 0);

// Rellena el fondo con el color seleccionado
imagefill($image, 0, 0, $bg);

// Selección del color de la elipse
$col_ellipse = imagecolorallocate($image, 255, 255, 255);

// Dibuja la elipse
imageellipse($image, 200, 150, 300, 200, $col_ellipse);

// Muestra la imagen
header("Content-type: image/png");
imagepng($image);

?>

    
```php

Resultado del ejemplo anterior es similar a:

![Visualización del ejemplo: imageellipse()](en/reference/image/figures/imageellipse.png)

## Notas

> [!NOTE]
> `imageellipse` ignora `imagesetthickness`.

## Véase también

imagefilledellipse

imagearc
