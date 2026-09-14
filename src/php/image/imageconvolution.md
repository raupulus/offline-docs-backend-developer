---
title: imageconvolution
description: Aplica una matriz de convolución 3x3, utilizando el coeficiente y el
  desplazamiento
source_url: https://www.php.net/manual/es/function.imageconvolution.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imageconvolution.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 213fbd944
order: 31690
---

imageconvolution

Aplica una matriz de convolución 3x3, utilizando el coeficiente y el desplazamiento

## Descripción

```php
imageconvolution(GdImage $image, array $matrix, float $divisor, float $offset): bool
```php

`imageconvolution` aplica una matriz de convolución 3x3, utilizando el coeficiente `div` y el desplazamiento `offset`.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`matrix`  
Una matriz 3x3: un array que contiene tres arrays de tres números de punto flotante.

`divisor`  
El divisor del resultado de la convolución, utilizado para la normalización.

`offset`  
La posición del color.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Impresión del logo PHP.net con `imageconvolution`

```
<?php
$image = imagecreatefromgif('http://www.php.net/images/php.gif');

$emboss = array(array(2, 0, 0), array(0, -1, 0), array(0, 0, -1));
imageconvolution($image, $emboss, 1, 127);

header('Content-Type: image/png');
imagepng($image, null, 9);
?>

    
```php

El ejemplo anterior mostrará:

![](en/reference/image/figures/imageconvolution_emboss.png)

Desenfoque gaussiano con `imageconvolution`

```
<?php
$image = imagecreatetruecolor(180,40);

// Escribe el texto y aplica un desenfoque gaussiano a la imagen
imagestring($image, 5, 10, 8, 'Texto desenfocado gaussiano', 0x00ff00);
$gaussian = array(array(1.0, 2.0, 1.0), array(2.0, 4.0, 2.0), array(1.0, 2.0, 1.0));
imageconvolution($image, $gaussian, 16, 0);

// Reescribe el texto para la comparación
imagestring($image, 5, 10, 18, 'Texto desenfocado gaussiano', 0x00ff00);

header('Content-Type: image/png');
imagepng($image, null, 9);
?>

    
```php

El ejemplo anterior mostrará:

![Visualización del ejemplo: Desenfoque gaussiano](en/reference/image/figures/imageconvolution_gaussian.png)

## Véase también

imagefilter
