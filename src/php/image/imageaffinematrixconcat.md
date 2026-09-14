---
title: imageaffinematrixconcat
description: Concatena dos matrices de transformación afín
source_url: https://www.php.net/manual/es/function.imageaffinematrixconcat.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imageaffinematrixconcat.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: 73fae4ee5
order: 31440
---

imageaffinematrixconcat

Concatena dos matrices de transformación afín

## Descripción

```php
imageaffinematrixconcat(array $matrix1, array $matrix2): array
```php

Devuelve la concatenación de dos matrices de transformación afín, lo cual es útil si varias transformaciones deben aplicarse a la misma imagen en una sola vez.

## Parámetros

`matrix1`  
Una matriz de transformación afín (un array con claves de `0` a `5` y números decimales como valores).

`matrix2`  
Una matriz de transformación afín (un array con claves de `0` a `5` y números decimales como valores).

## Valores devueltos

Una matriz de transformación afín (un array con claves de `0` a `5` y números decimales como valores). o `false` si ocurre un error.

## Ejemplos

Ejemplo para `imageaffinematrixconcat`

```
<?php
$m1 = imageaffinematrixget(IMG_AFFINE_TRANSLATE, array('x' => 2, 'y' => 3));
$m2 = imageaffinematrixget(IMG_AFFINE_SCALE, array('x' => 4, 'y' => 5));
$matrix = imageaffinematrixconcat($m1, $m2);
print_r($matrix);
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [0] => 4
        [1] => 0
        [2] => 0
        [3] => 5
        [4] => 8
        [5] => 15
    )

## Véase también

imageaffine

imageaffinematrixget
