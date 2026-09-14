---
title: imagewbmp
description: Enviar la imagen al navegador o a un fichero
source_url: https://www.php.net/manual/es/function.imagewbmp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagewbmp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 9960a09a5
order: 32470
---

imagewbmp

Enviar la imagen al navegador o a un fichero

## Descripción

```php
imagewbmp(GdImage $image, [resource $file], [int $foreground_color]): bool
```php

`imagewbmp` muestra o guarda una versión WBMP de la imagen `image`.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`file`  
La ruta o un recurso de flujo abierto (que se cierra automáticamente después de que esta función retorne) donde guardar el fichero. Si no se define o es `null`, el flujo de imagen sin procesar se enviará directamente.

`foreground_color`  
Puede seleccionarse el color de primer plano con este argumento. Utilice el identificador devuelto por `imagecolorallocate` como valor de este argumento. El color de primer plano por omisión es negro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

> [!CAUTION]
> Sin embargo, si libgd no logra producir la imagen, esta función devuelve `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |
| 8.0.0 | `foreground_color` ahora es nullable. |

## Ejemplos

Mostrar una imagen WBMP

```
<?php
// Creación de una imagen vacía y adición de texto
$im = imagecreatetruecolor(120, 20);
$text_color = imagecolorallocate($im, 233, 14, 91);
imagestring($im, 1, 5, 5,  'Un texto simple', $text_color);

// Define el contenido del encabezado - en este caso, image/vnd.wap.wbmp
// Sugerencia: ver image_type_to_mime_type() para tipos de contenido
header('Content-Type: image/vnd.wap.wbmp');

// Mostrar la imagen
imagewbmp($im);

?>

    
```php

Guardar la imagen WBMP

```
<?php
// Creación de una imagen vacía y adición de texto
$im = imagecreatetruecolor(120, 20);
$text_color = imagecolorallocate($im, 233, 14, 91);
imagestring($im, 1, 5, 5,  'Un texto simple', $text_color);

// Guardar la imagen
imagewbmp($im, 'simpletext.wbmp');

?>

    
```php

Mostrar la imagen con un primer plano diferente

```
<?php
// Creación de una imagen vacía y adición de texto
$im = imagecreatetruecolor(120, 20);
$text_color = imagecolorallocate($im, 233, 14, 91);
imagestring($im, 1, 5, 5,  'Un texto simple', $text_color);

// Define el contenido del encabezado - en este caso, image/vnd.wap.wbmp
// Sugerencia: ver la función image_type_to_mime_type() para tipos de contenido
header('Content-type: image/vnd.wap.wbmp');

// Define un primer plano
$foreground_color = imagecolorallocate($im, 255, 0, 0);

imagewbmp($im, NULL, $foreground_color);

?>

    
```php

## Véase también

image2wbmp

imagepng

imagegif

imagejpeg

imagetypes
