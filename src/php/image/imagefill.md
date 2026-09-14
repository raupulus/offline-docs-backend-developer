---
title: imagefill
description: Relleno
source_url: https://www.php.net/manual/es/function.imagefill.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagefill.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: fcd921429
order: 31960
---

imagefill

Relleno

## Descripción

```php
imagefill(GdImage $image, int $x, int $y, int $color): true
```php

Realiza un relleno con el color `color`, en la imagen `image`, a partir del punto de coordenadas (`x`, `y`) (la esquina superior izquierda es el origen (0,0)).

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`x`  
X: coordenada del punto de inicio.

`y`  
Y: coordenada del punto de inicio.

`color`  
El color de relleno. Un identificador de color creado con `imagecolorallocate`.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Ejemplo con `imagefill`

```
<?php

$im = imagecreatetruecolor(100, 100);

// Establece el fondo rojo
$red = imagecolorallocate($im, 255, 0, 0);
imagefill($im, 0, 0, $red);

header('Content-type: image/png');
imagepng($im);
?>

    
```php

Resultado del ejemplo anterior es similar a:

![Visualización del ejemplo: imagefill()](en/reference/image/figures/imagefill.png)

## Véase también

imagecolorallocate
