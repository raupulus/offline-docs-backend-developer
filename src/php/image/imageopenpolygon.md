---
title: imageopenpolygon
description: Dibuja un polígono abierto
source_url: https://www.php.net/manual/es/function.imageopenpolygon.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imageopenpolygon.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: 9960a09a5
order: 32220
---

imageopenpolygon

Dibuja un polígono abierto

## Descripción

Firma disponible a partir de PHP 8.0.0 (no soportada con argumentos nombrados)

```php
imageopenpolygon(GdImage $image, array $points, int $color): bool
```php

Firma alternativa (obsoleta a partir de PHP 8.1.0)

```php
imageopenpolygon(GdImage $image, array $points, int $num_points, int $color): bool
```

`imageopenpolygon` dibuja un polígono abierto en la `image`. A diferencia de `imagepolygon`, no se dibuja ninguna línea entre el último y el primer punto.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`points`  
Un array que contiene los vértices del polígono, por ejemplo:

|             |      |
|-------------|------|
| points\[0\] | = x0 |
| points\[1\] | = y0 |
| points\[2\] | = x1 |
| points\[3\] | = y1 |

`num_points`  
Número total de puntos (vértices), que deben ser al menos 3.

Si este parámetro se omite conforme a la segunda firma, `points` debe tener un número par de elementos, y `num_points` se asume que es `count($points)/2`.

`color`  
Un identificador de color creado con `imagecolorallocate`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `num_points` ha sido declarado obsoleto. |
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Ejemplo con `imageopenpolygon`

```php
<?php
// Crear una imagen vacía
$image = imagecreatetruecolor(400, 300);

// Asignar un color para el polígono
$col_poly = imagecolorallocate($image, 255, 255, 255);

// Dibujar el polígono
imageopenpolygon($image, array(
        0,   0,
        100, 200,
        300, 200
    ),
    $col_poly);

// Mostrar la imagen en el navegador
header('Content-type: image/png');

imagepng($image);
?>

    
```

Resultado del ejemplo anterior es similar a:

![Salida del ejemplo: imageopenpolygon()](en/reference/image/figures/imageopenpolygon.png)

## Véase también

imagepolygon
