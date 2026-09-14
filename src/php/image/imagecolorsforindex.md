---
title: imagecolorsforindex
description: Retorna el color asociado a un índice
source_url: https://www.php.net/manual/es/function.imagecolorsforindex.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecolorsforindex.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 0773339dc
order: 31660
---

imagecolorsforindex

Retorna el color asociado a un índice

## Descripción

```php
imagecolorsforindex(GdImage $image, int $color): array
```php

Retorna el color asociado a un índice especificado.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`color`  
El índice del color.

## Valores devueltos

Retorna un array asociativo con las claves `"red"`, `"green"`, `"blue"` y `"alpha"` que contienen los valores para el índice del color especificado.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |
| 8.0.0 | La función `imagecolorsforindex` ahora lanza una excepción `ValueError` si `color` está fuera de rango; anteriormente, se retornaba `false` en su lugar. |

## Ejemplos

Ejemplo con `imagecolorsforindex`

```
<?php

// se abre una imagen
$im = imagecreatefrompng('nexen.png');

// se obtiene un color
$start_x = 40;
$start_y = 50;
$color_index = imagecolorat($im, $start_x, $start_y);

// se lo hace legible
$color_tran = imagecolorsforindex($im, $color_index);

// ¿Cuál es?
print_r($color_tran);

?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
       [red] => 226
       [green] => 222
       [blue] => 252
       [alpha] => 0
    )

## Véase también

imagecolorat

imagecolorexact
