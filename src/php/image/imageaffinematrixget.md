---
title: imageaffinematrixget
description: Obtener una matriz de transformación afín
source_url: https://www.php.net/manual/es/function.imageaffinematrixget.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imageaffinematrixget.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: 976425d4f
order: 31450
---

imageaffinematrixget

Obtener una matriz de transformación afín

## Descripción

```php
imageaffinematrixget(int $type, array $options): array
```php

Devuelve una matriz de transformación afín.

## Parámetros

`type`  
Una constante entre `IMG_AFFINE_*`.

`options`  
Si `type` es `IMG_AFFINE_TRANSLATE` o `IMG_AFFINE_SCALE`, `options` debe ser un `array` con las claves `x` y `y`, ambas con valores `float`.

Si `type` es `IMG_AFFINE_ROTATE`, `IMG_AFFINE_SHEAR_HORIZONTAL` o `IMG_AFFINE_SHEAR_VERTICAL`, `options` debe ser un valor `float` que especifique el ángulo.

## Valores devueltos

Una matriz de transformación afín (un array con claves de `0` a `5` y números decimales como valores). o `false` si ocurre un error.

## Ejemplos

Ejemplo para `imageaffinematrixget`

```
<?php
$matrix = imageaffinematrixget(IMG_AFFINE_TRANSLATE, array('x' => 2, 'y' => 3));
print_r($matrix);
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [0] => 1
        [1] => 0
        [2] => 0
        [3] => 1
        [4] => 2
        [5] => 3
    )

## Véase también

imageaffine

imageaffinematrixconcat
