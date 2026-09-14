---
title: imagegif
description: Enviar la imagen al navegador o a un fichero
source_url: https://www.php.net/manual/es/function.imagegif.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagegif.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 9960a09a5
order: 32130
---

imagegif

Enviar la imagen al navegador o a un fichero

## Descripción

```php
imagegif(GdImage $image, [resource $file]): bool
```php

`imagegif` crea un fichero de imagen GIF en `file` a partir de la imagen `image`. El argumento `image` es un identificador válido devuelto por la función `imagecreate` o las funciones `imagecreatefrom*`.

El formato de la imagen será GIF87a, a menos que la imagen tenga un color transparente (establecido mediante la función `imagecolortransparent`), lo que hará que sea en formato GIF89a.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`file`  
La ruta o un recurso de flujo abierto (que se cierra automáticamente después de que esta función retorne) donde guardar el fichero. Si no se define o es `null`, el flujo de imagen sin procesar se enviará directamente.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

> [!CAUTION]
> Sin embargo, si libgd no logra producir la imagen, esta función devuelve `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Visualización de una imagen utilizando `imagegif`

```
<?php
// Creación de una imagen
$im = imagecreatetruecolor(100, 100);

// Define el fondo como blanco
imagefilledrectangle($im, 0, 0, 99, 99, 0xFFFFFF);

// Dibuja texto en la imagen
imagestring($im, 3, 40, 20, 'GD Library', 0xFFBA00);

// Muestra la imagen en el navegador
header('Content-Type: image/gif');

imagegif($im);
?>

    
```php

Conversión de una imagen PNG a GIF, utilizando `imagegif`

```
<?php
// Carga de la imagen PNG
$png = imagecreatefrompng('./php.png');

// Guardado de la imagen como GIF
imagegif($png, './php.gif');

// ¡Listo!
echo 'Conversión exitosa de la imagen PNG a GIF !';
?>

    
```php

## Notas

> [!NOTE]
> El siguiente código permite escribir scripts PHP más portables: el tipo de GD se detecta automáticamente. Reemplaza la secuencia `header ("Content-Type: image/gif"); ImageGif($im);` por un código más flexible:
>
> <div class="informalexample">
>
> ```
> <?php
> // Creación de una imagen
> $im = imagecreatetruecolor(100, 100);
>
> // Se realizan algunas operaciones en la imagen aquí...
>
> // Manejo de la visualización
> if(function_exists('imagegif'))
> {
>     // Para GIF
>     header('Content-Type: image/gif');
>
>     imagegif($im);
> }
> elseif(function_exists('imagejpeg'))
> {
>     // Para JPEG
>     header('Content-Type: image/jpeg');
>
>     imagejpeg($im, NULL, 100);
> }
> elseif(function_exists('imagepng'))
> {
>     // Para PNG
>     header('Content-Type: image/png');
>
>     imagepng($im);
> }
> elseif(function_exists('imagewbmp'))
> {
>     // Para WBMP
>     header('Content-Type: image/vnd.wap.wbmp');
>
>     imagewbmp($im);
> }
> else
> {
>     die('No se encontró soporte para ningún formato de imagen en este servidor PHP');
> }
>
> ?>
>
>      
> ```
>
> </div>

> [!NOTE]
> Puede utilizarse la función `imagetypes` en lugar de `function_exists` para verificar la presencia de los diferentes formatos de imagen soportados:
>
> <div class="informalexample">
>
> ```
> <?php
> if(imagetypes() & IMG_GIF)
> {
>     header('Content-Type: image/gif');
>     imagegif($im);
> }
> elseif(imagetypes() & IMG_JPG)
> {
>     /* ... etc. */
> }
> ?>
>
>      
> ```
>
> </div>

## Véase también

imagepng

imagewbmp

imagejpeg

imagetypes
