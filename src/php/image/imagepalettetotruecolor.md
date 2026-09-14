---
title: imagepalettetotruecolor
description: Convierte una imagen basada en una paleta a color verdadero
source_url: https://www.php.net/manual/es/function.imagepalettetotruecolor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagepalettetotruecolor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: 525aa5f19
order: 32240
---

imagepalettetotruecolor

Convierte una imagen basada en una paleta a color verdadero

## Descripción

```php
imagepalettetotruecolor(GdImage $image): bool
```php

Convierte una imagen basada en una paleta, creada por una función como `imagecreate`, en una imagen en color verdadero, como `imagecreatetruecolor`.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

## Valores devueltos

Devuelve `true` si la conversión ha sido exitosa, o si la imagen de origen ya es de color verdadero, en caso contrario, devuelve `false`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Convierte cualquier objeto imagen a color verdadero

```
<?php
// Compatibilidad ascendente
if(!function_exists('imagepalettetotruecolor'))
{
    function imagepalettetotruecolor(&$src)
    {
        if(imageistruecolor($src))
        {
            return(true);
        }

        $dst = imagecreatetruecolor(imagesx($src), imagesy($src));

        imagecopy($dst, $src, 0, 0, 0, 0, imagesx($src), imagesy($src));

        $src = $dst;

        return(true);
    }
}

// Utilización de una Closure
$typeof = function() use($im)
{
    echo 'typeof($im) = ' . (imageistruecolor($im) ? 'true color' : 'palette'), PHP_EOL;
};

// Crea una imagen basada en una paleta
$im = imagecreate(100, 100);
$typeof();

// La convierte a color verdadero
imagepalettetotruecolor($im);
$typeof();

?>

    
```php

El ejemplo anterior mostrará:

    typeof($im) = palette
    typeof($im) = true color

## Véase también

imagecreatetruecolor

imageistruecolor
