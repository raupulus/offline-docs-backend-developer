---
title: imagerotate
description: Rota una imagen en un ángulo
source_url: https://www.php.net/manual/es/function.imagerotate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagerotate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: 9960a09a5
order: 32290
---

imagerotate

Rota una imagen en un ángulo

## Descripción

```php
imagerotate(GdImage $image, float $angle, int $background_color): GdImage
```php

`imagerotate` rota la imagen `image` en un ángulo de `angle`, en grados.

El centro de rotación es el centro de la imagen, y la imagen rotada puede tener dimensiones diferentes de la imagen original.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`angle`  
El ángulo de rotación, en grados. El ángulo de rotación es interpretado como el número de grados para rotar la imagen en sentido contrario a las agujas del reloj.

`background_color`  
Especifica el color de las zonas que serán descubiertas después de la rotación.

## Valores devueltos

Devuelve un objeto de imagen correspondiente a la imagen después de la rotación, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | El parámetro no utilizado `ignore_transparent` ha sido completamente eliminado. |
| 8.0.0 | En caso de éxito, esta función devuelve ahora una instancia de `GDImage` ; anteriormente, se devolvía un `resource`. |
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |
| 8.0.0 | El parámetro no utilizado `ignore_transparent` ahora espera un `bool` ; anteriormente esperaba un `int`. |

## Ejemplos

Rotación de una imagen de 180 grados

Este ejemplo rota una imagen de 180 grados - al revés.

```
<?php
// Archivo y grados de rotación
$filename = 'test.jpg';
$degrees = 180;

// Tipo de contenido
header('Content-type: image/jpeg');

// Carga
$source = imagecreatefromjpeg($filename);

// Rotación
$rotate = imagerotate($source, $degrees, 0);

// Mostrar
imagejpeg($rotate);

?>

    
```php

Resultado del ejemplo anterior es similar a:

![Visualización del ejemplo: Rotación de una imagen de 180 grados](en/reference/image/figures/imagerotate.jpg)

## Notas

> [!NOTE]
> Esta función es afectada por el método de interpolación, definido por la función `imagesetinterpolation`.

## Véase también

imagesetinterpolation
