---
title: imagealphablending
description: Modifica el modo de mezcla de una imagen
source_url: https://www.php.net/manual/es/function.imagealphablending.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagealphablending.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: fcd921429
order: 31460
---

imagealphablending

Modifica el modo de mezcla de una imagen

## Descripción

```php
imagealphablending(GdImage $image, bool $enable): true
```php

`imagealphablending` proporciona dos modos de dibujo para imágenes en colores verdaderos (truecolors). En modo "mezcla", el canal alpha de cada color es proporcionado a cada función de dibujo, de modo que `imagesetpixel` pueda determinar su transparencia. GD mezcla entonces automáticamente el color en ese punto y almacena el resultado en la imagen. El píxel resultante es entonces opaco. En modo no mezclante, el color es copiado literalmente con sus informaciones de canal alpha, y reemplaza el píxel de destino. La mezcla no está disponible con imágenes de paleta.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`enable`  
Si se debe activar el modo de mezcla o no. En imágenes de colores verdaderos, el valor por omisión es `true`, de lo contrario, el valor por omisión es `false`.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Ejemplo con `imagealphablending`

```
<?php
// Creación de una imagen
$im = imagecreatetruecolor(100, 100);

// Define el alphablending a on
imagealphablending($im, true);

// Dibuja un rectángulo
imagefilledrectangle($im, 30, 30, 70, 70, imagecolorallocate($im, 255, 0, 0));

// Mostrar
header('Content-Type: image/png');

imagepng($im);
?>

   
```php
