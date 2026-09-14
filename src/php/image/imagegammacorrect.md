---
title: imagegammacorrect
description: Aplica una corrección gamma a la imagen GD
source_url: https://www.php.net/manual/es/function.imagegammacorrect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagegammacorrect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: fcd921429
order: 32080
---

imagegammacorrect

Aplica una corrección gamma a la imagen GD

## Descripción

```php
imagegammacorrect(GdImage $image, float $input_gamma, float $output_gamma): true
```php

Aplica una corrección gamma a la imagen GD `image`.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`input_gamma`  
El factor gamma de entrada.

`output_gamma`  
El factor gamma de salida.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Ejemplo con `imagegammacorrect`

```
<?php
// Creación de una imagen
$im = imagecreatefromgif('php.gif');

// Corrección gamma, salida a 1.537
imagegammacorrect($im, 1.0, 1.537);

// Guardado y liberación de la memoria
imagegif($im, './php_gamma_corrected.gif');
?>

    
```php
