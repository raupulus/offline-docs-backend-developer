---
title: imagebmp
description: Muestra o guarda una imagen BMP en el navegador o en un fichero
source_url: https://www.php.net/manual/es/function.imagebmp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagebmp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: 9960a09a5
order: 31500
---

imagebmp

Muestra o guarda una imagen BMP en el navegador o en un fichero

## Descripción

```php
imagebmp(GdImage $image, [resource $file], [bool $compressed]): bool
```php

Muestra o guarda una versión BMP de la `image` proporcionada.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`file`  
La ruta o un recurso de flujo abierto (que se cierra automáticamente después de que esta función retorne) donde guardar el fichero. Si no se define o es `null`, el flujo de imagen sin procesar se enviará directamente.

> [!NOTE]
> `null` no es válido si el argumento `compressed` no se utiliza.

`compressed`  
Si el BMP debe ser comprimido con `run-length encoding` (RLE), o no.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

> [!CAUTION]
> Sin embargo, si libgd no logra producir la imagen, esta función devuelve `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |
| 8.0.0 | El tipo de `compressed` es ahora `bool`; anteriormente era `int`. |

## Ejemplos

Guardar un fichero BMP

```
<?php
// Crear una imagen en blanco y añadir texto
$im = imagecreatetruecolor(120, 20);
$text_color = imagecolorallocate($im, 233, 14, 91);

imagestring($im, 1, 5, 5,  'BMP con PHP', $text_color);

// Guardar la imagen
imagebmp($im, 'php.bmp');
?>

    
```php
