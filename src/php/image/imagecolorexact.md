---
title: imagecolorexact
description: Devuelve el índice del color especificado
source_url: https://www.php.net/manual/es/function.imagecolorexact.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecolorexact.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 9960a09a5
order: 31600
---

imagecolorexact

Devuelve el índice del color especificado

## Descripción

```php
imagecolorexact(GdImage $image, int $red, int $green, int $blue): int
```php

Devuelve el índice del color especificado en la paleta de la imagen `image`.

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

Devuelve el índice del color especificado en la paleta, o -1 si el color no existe.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Obtención de los colores que componen el logo GD

```
<?php
// Define la imagen
$im = imagecreatefrompng('./gdlogo.png');

$colors   = Array();
$colors[] = imagecolorexact($im, 255, 0, 0);
$colors[] = imagecolorexact($im, 0, 0, 0);
$colors[] = imagecolorexact($im, 255, 255, 255);
$colors[] = imagecolorexact($im, 100, 255, 52);

print_r($colors);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => 16711680
        [1] => 0
        [2] => 16777215
        [3] => 6618932
    )

## Véase también

imagecolorclosest
