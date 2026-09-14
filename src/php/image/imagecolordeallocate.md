---
title: imagecolordeallocate
description: Elimina un color de una imagen
source_url: https://www.php.net/manual/es/function.imagecolordeallocate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecolordeallocate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: fcd921429
order: 31590
---

imagecolordeallocate

Elimina un color de una imagen

## Descripción

```php
imagecolordeallocate(GdImage $image, int $color): true
```php

Elimina el color `color` previamente asignado con la función `imagecolorallocate`, para la imagen `image`.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`color`  
El identificador del color.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Ejemplo con `imagecolordeallocate`

```
<?php
$white = imagecolorallocate($im, 255, 255, 255);
imagecolordeallocate($im, $white);
?>

    
```php

## Véase también

imagecolorallocate

imagecolorallocatealpha
