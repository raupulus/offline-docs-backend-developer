---
title: imagegd2
description: Genera una imagen en formato GD2, hacia el navegador o un fichero
source_url: https://www.php.net/manual/es/function.imagegd2.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagegd2.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 2a3e48b0e
order: 32100
---

imagegd2

Genera una imagen en formato GD2, hacia el navegador o un fichero

## Descripción

```php
imagegd2(GdImage $image, [string $file], [int $chunk_size], [int $mode]): bool
```php

Genera o guarda el fichero `file` en formato GD2.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`file`  
La ruta o un recurso de flujo abierto (que se cierra automáticamente después de que esta función retorne) donde guardar el fichero. Si no se define o es `null`, el flujo de imagen sin procesar se enviará directamente.

`chunk_size`  
Tamaño del fragmento.

`mode`  
Puede ser `IMG_GD2_RAW` o `IMG_GD2_COMPRESSED`. Por omisión, vale `IMG_GD2_RAW`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

> [!CAUTION]
> Sin embargo, si libgd no logra producir la imagen, esta función devuelve `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.3 | `file` ahora es nulo. |
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Mostrar una imagen GD2

```
<?php
// Creación de una imagen vacía y adición de texto
$im = imagecreatetruecolor(120, 20);
$text_color = imagecolorallocate($im, 233, 14, 91);
imagestring($im, 1, 5, 5,  "Un texto simple", $text_color);

// Mostrar la imagen
imagegd2($im);

?>

    
```php

Guardar una imagen GD2

```
<?php
// Creación de una imagen vacía y adición de texto
$im = imagecreatetruecolor(120, 20);
$text_color = imagecolorallocate($im, 233, 14, 91);
imagestring($im, 1, 5, 5,  "Un texto simple", $text_color);

// Guardar la imagen GD2
// El formato de fichero para imágenes GD2 es .gd2, ver http://www.libgd.org/GdFileFormats
imagegd2($im, 'simple.gd2');

?>

    
```php

## Notas

> [!NOTE]
> El formato GD2 se utiliza comúnmente para cargar rápidamente las partes de una imagen. Tenga en cuenta que el formato GD2 solo es utilizable en aplicaciones compatibles con GD2.

> [!WARNING]
> Los formatos de imagen GD y GD2 son formatos propietarios de libgd. Deben considerarse *obsoletos*, y solo deben utilizarse con fines de desarrollo y pruebas.

## Véase también

imagegd
