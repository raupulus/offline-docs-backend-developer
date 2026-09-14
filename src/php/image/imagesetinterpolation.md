---
title: imagesetinterpolation
description: Define el método de interpolación
source_url: https://www.php.net/manual/es/function.imagesetinterpolation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagesetinterpolation.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: 593ea510e
order: 32340
---

imagesetinterpolation

Define el método de interpolación

## Descripción

```php
imagesetinterpolation(GdImage $image, [int $method]): bool
```php

Define el método de interpolación; el hecho de definir un método de interpolación afecta el rendimiento de varias funciones en GD, como por ejemplo la función `imagerotate`.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`method`  
El método de interpolación, que puede ser uno de los siguientes:

- `IMG_BELL`: filtro Bell.

- `IMG_BESSEL`: filtro Bessel.

- `IMG_BICUBIC`: interpolación bicúbica.

- `IMG_BICUBIC_FIXED`: implementación de punto fijo de una interpolación bicúbica.

- `IMG_BILINEAR_FIXED`: implementación de punto fijo de una interpolación bilineal (`por defecto (incluyendo para la creación de imágenes)`).

- `IMG_BLACKMAN`: función de ventana Blackman.

- `IMG_BOX`: filtro de desenfoque Box.

- `IMG_BSPLINE`: interpolación Spline.

- `IMG_CATMULLROM`: interpolación cubica Hermite spline.

- `IMG_GAUSSIAN`: función Gaussiana.

- `IMG_GENERALIZED_CUBIC`: interpolación fractal cubica generalizada spline.

- `IMG_HERMITE`: interpolación Hermite.

- `IMG_HAMMING`: filtro Hamming.

- `IMG_HANNING`: filtro Hanning.

- `IMG_MITCHELL`: filtro Mitchell.

- `IMG_POWER`: interpolación Power.

- `IMG_QUADRATIC`: interpolación cuadrática inversa.

- `IMG_SINC`: función Sinc.

- `IMG_NEAREST_NEIGHBOUR`: interpolación del vecino más cercano.

- `IMG_WEIGHTED4`: filtro Weighting.

- `IMG_TRIANGLE`: interpolación Triangle.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Ejemplo con `imagesetinterpolation`

```
<?php
// Carga de la imagen
$im = imagecreate(500, 500);

// Por defecto, la interpolación es IMG_BILINEAR_FIXED; se utiliza en su lugar
// el filtro 'Mitchell':
imagesetinterpolation($im, IMG_MITCHELL);

// Se continúa trabajando con $im...
?>

    
```php

## Notas

La modificación del método de interpolación afecta a las siguientes funciones durante el rendimiento:

- `imageaffine`

- `imagerotate`

## Véase también

imagegetinterpolation
