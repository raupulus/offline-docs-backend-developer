---
title: imagefilledpolygon
description: Dibuja un polígono relleno
source_url: https://www.php.net/manual/es/function.imagefilledpolygon.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagefilledpolygon.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 9960a09a5
order: 31990
---

imagefilledpolygon

Dibuja un polígono relleno

## Descripción

Firma a partir de PHP 8.0.0 (no soportada con argumentos nombrados)

```php
imagefilledpolygon(GdImage $image, array $points, int $color): bool
```php

Firma alternativa (obsoleta a partir de PHP 8.1.0)

```php
imagefilledpolygon(GdImage $image, array $points, int $num_points, int $color): bool
```

`imagefilledpolygon` dibuja un polígono relleno en la imagen `image`.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`points`  
Un array que contiene las coordenadas `x` y `y` del vértice de los polígonos.

`num_points`  
Número total de puntos (vértices), que deben ser al menos 3.

Si este parámetro es omitido conforme a la segunda firma, `points` debe tener un número par de elementos, y `num_points` se asume como `count($points)/2`.

`color`  
Un identificador de color creado con `imagecolorallocate`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `num_points` ha sido marcado como obsoleto. |
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Ejemplo con `imagefilledpolygon`

```php
<?php
// Definición del array de puntos para el polígono
$values = array(
            40,  50,  // Punto 1 (x, y)
            20,  240, // Punto 2 (x, y)
            60,  60,  // Punto 3 (x, y)
            240, 20,  // Punto 4 (x, y)
            50,  40,  // Punto 5 (x, y)
            10,  10   // Punto 6 (x, y)
            );

// Creación de una imagen
$image = imagecreatetruecolor(250, 250);

// Asignación de algunos colores
$bg   = imagecolorallocate($image, 0, 0, 0);
$blue = imagecolorallocate($image, 0, 0, 255);

// Relleno del fondo
imagefilledrectangle($image, 0, 0, 249, 249, $bg);

// Dibujo del polígono
imagefilledpolygon($image, $values, $blue);

// Visualización de la imagen
header('Content-type: image/png');
imagepng($image);
?>

    
```

Resultado del ejemplo anterior es similar a:

![Visualización del ejemplo: imagefilledpolygon()](en/reference/image/figures/imagefilledpolygon.png)

## Véase también

imagepolygon
