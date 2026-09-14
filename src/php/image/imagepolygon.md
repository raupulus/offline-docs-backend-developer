---
title: imagepolygon
description: Dibuja un polígono
source_url: https://www.php.net/manual/es/function.imagepolygon.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagepolygon.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: 9960a09a5
order: 32260
---

imagepolygon

Dibuja un polígono

## Descripción

Firma disponible a partir de PHP 8.0.0 (no soportada con argumentos nombrados)

```php
imagepolygon(GdImage $image, array $points, int $color): bool
```php

Firma alternativa (deprecada a partir de PHP 8.1.0)

```php
imagepolygon(GdImage $image, array $points, int $num_points, int $color): bool
```

`imagepolygon` dibuja un polígono en la imagen `image`.

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

Si este argumento es omitido conforme a la segunda firma, `points` debe tener un número par de elementos, y `num_points` se asume como `count($points)/2`.

`color`  
Un identificador de color creado con `imagecolorallocate`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El argumento `num_points` ha sido deprecado. |
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Ejemplo con `imagepolygon`

```php
<?php
// Creación de una imagen vacía
$image = imagecreatetruecolor(400, 300);

// Asigna un color para el polígono
$col_poly = imagecolorallocate($image, 255, 255, 255);

// Dibuja el polígono
imagepolygon($image, array(
        0,   0,
        100, 200,
        300, 200
    ),
    $col_poly);

// Muestra la imagen en el navegador
header('Content-type: image/png');

imagepng($image);
?>

    
```

Resultado del ejemplo anterior es similar a:

![Visualización del ejemplo: imagepolygon()](en/reference/image/figures/imagepolygon.png)

## Véase también

imagefilledpolygon

imageopenpolygon

imagecreate

imagecreatetruecolor
