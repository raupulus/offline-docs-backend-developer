---
title: imagecolorresolve
description: Devuelve el índice de la color dada, o la más cercana posible
source_url: https://www.php.net/manual/es/function.imagecolorresolve.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecolorresolve.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 9960a09a5
order: 31630
---

imagecolorresolve

Devuelve el índice de la color dada, o la más cercana posible

## Descripción

```php
imagecolorresolve(GdImage $image, int $red, int $green, int $blue): int
```php

`imagecolorresolve` devuelve un índice de color en todos los casos. O bien encuentra la color solicitada en la paleta, o bien encuentra la color más cercana.

Si la imagen fue creada a partir de un fichero, solo se resuelven los colores utilizados en la imagen. Los colores presentes únicamente en la paleta no se resuelven.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`red`  
Valor del componente rojo.

`green`  
Valor del componente verde.

`blue`  
Valor del componente azul.

## Valores devueltos

Devuelve un índice de color.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Ejemplo con `imagecoloresolve` para obtener las colores de una imagen

```
<?php
// Carga de una imagen
$im = imagecreatefromgif('phplogo.gif');

// Obtención de las colores más cercanas de la imagen
$colors = array();
$colors[] = imagecolorresolve($im, 255, 255, 255);
$colors[] = imagecolorresolve($im, 0, 0, 200)

// Mostrar
print_r($colors);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => 89
        [1] => 85
    )

## Véase también

imagecolorclosest
