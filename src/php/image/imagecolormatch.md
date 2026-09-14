---
title: imagecolormatch
description: Hace que las colores de la versión palette de una imagen coincidan más
  con las de su versión truecolor
source_url: https://www.php.net/manual/es/function.imagecolormatch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecolormatch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: fcd921429
order: 31620
---

imagecolormatch

Hace que las colores de la versión palette de una imagen coincidan más con las de su versión truecolor

## Descripción

```php
imagecolormatch(GdImage $image1, GdImage $image2): true
```php

Hace que las colores de la versión palette de una imagen coincidan más con las de su versión truecolor.

## Parámetros

`image1`  
Un objeto de imagen truecolor.

`image2`  
Un objeto de imagen palette que apunta a una imagen que tiene el mismo tamaño que `image1`.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image1` y `image2` ahora requieren instancias de `GdImage`; anteriormente se esperaban `resource`s |

## Ejemplos

Ejemplo con `imagecolormatch`

```
<?php
// Define la imagen true color y la palette
$im1 = imagecreatefrompng('./gdlogo.png');
$im2 = imagecreate(imagesx($im1), imagesy($im1));

// Añade algunas colores a $im2
$colors   = Array();
$colors[] = imagecolorallocate($im2, 255, 36, 74);
$colors[] = imagecolorallocate($im2, 40, 0, 240);
$colors[] = imagecolorallocate($im2, 82, 100, 255);
$colors[] = imagecolorallocate($im2, 84, 63, 44);

// Hace que estas colores coincidan con la imagen true color
imagecolormatch($im1, $im2);
?>

   
```php

## Véase también

imagecreatetruecolor
