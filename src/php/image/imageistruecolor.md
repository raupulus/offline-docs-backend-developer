---
title: imageistruecolor
description: Determina si una imagen es una imagen truecolor
source_url: https://www.php.net/manual/es/function.imageistruecolor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imageistruecolor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 9960a09a5
order: 32170
---

imageistruecolor

Determina si una imagen es una imagen truecolor

## Descripción

```php
imageistruecolor(GdImage $image): bool
```php

`imageistruecolor`determina si la imagen `image` es una imagen truecolor.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

## Valores devueltos

Devuelve `true` si la imagen es truecolor, `false` en caso contrario.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Detección simple de una imagen en truecolor con `imageistruecolor`

```
<?php
// $im es una instancia de imagen

// Verifica si la imagen es truecolor o no
if(!imageistruecolor($im))
{
    // Creación de una nueva imagen en truecolor
    $tc = imagecreatetruecolor(imagesx($im), imagesy($im));

    // Copia de los píxeles
    imagecopy($tc, $im, 0, 0, 0, 0, imagesx($im), imagesy($im));

    $im = $tc;
    $tc = NULL;

    // O utilice imagepalettetotruecolor()
}

// Se continúa trabajando con la instancia de la imagen
?>

    
```php

## Véase también

imagecreatetruecolor

imagepalettetotruecolor
