---
title: imagejpeg
description: Enviar la imagen al navegador o a un fichero
source_url: https://www.php.net/manual/es/function.imagejpeg.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagejpeg.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 9960a09a5
order: 32180
---

imagejpeg

Enviar la imagen al navegador o a un fichero

## Descripción

```php
imagejpeg(GdImage $image, [resource $file], [int $quality]): bool
```php

`imagejpeg` crea un fichero JPEG a partir de la imagen proporcionada.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`file`  
La ruta o un recurso de flujo abierto (que se cierra automáticamente después de que esta función retorne) donde guardar el fichero. Si no se define o es `null`, el flujo de imagen sin procesar se enviará directamente.

`quality`  
`quality` es opcional, y toma valores en el intervalo 0 (peor calidad, fichero pequeño) a 100 (mejor calidad, fichero grande). Por omisión (`-1`), se utiliza el valor de calidad IJG por defecto (aproximadamente 75).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

> [!CAUTION]
> Sin embargo, si libgd no logra producir la imagen, esta función devuelve `true`.

## Errores/Excepciones

Se genera una `ValueError` si `quality` es inválido.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Ahora se genera una `ValueError` si `quality` es inválido. |
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Mostrar una imagen JPEG hacia el navegador

```
<?php
// Creación de una imagen vacía y adición de texto
$im = imagecreatetruecolor(120, 20);
$text_color = imagecolorallocate($im, 233, 14, 91);
imagestring($im, 1, 5, 5,  'A Simple Text String', $text_color);

// Define el contenido del encabezado - en este caso, image/jpeg
header('Content-Type: image/jpeg');

// Mostrar la imagen
imagejpeg($im);

?>

    
```php

Resultado del ejemplo anterior es similar a:

![Visualización del ejemplo: imagejpeg()](en/reference/image/figures/imagejpeg.jpg)

Guardar una imagen JPEG en un fichero

```
<?php
// Creación de una imagen vacía y adición de texto
$im = imagecreatetruecolor(120, 20);
$text_color = imagecolorallocate($im, 233, 14, 91);
imagestring($im, 1, 5, 5,  'Un texto simple', $text_color);

// Guardar la imagen con el nombre 'simpletext.jpg'
imagejpeg($im, 'simpletext.jpg');

?>

    
```php

Mostrar la imagen con una calidad del 75% hacia el navegador

```
<?php
// Creación de una imagen vacía y adición de texto
$im = imagecreatetruecolor(120, 20);
$text_color = imagecolorallocate($im, 233, 14, 91);
imagestring($im, 1, 5, 5,  'Un texto simple', $text_color);

// Define el contenido del encabezado - en este caso, image/jpeg
header('Content-Type: image/jpeg');

// No se proporciona el nombre del fichero (se utiliza el valor NULL),
// luego, se define la calidad a 75%
imagejpeg($im, NULL, 75);

?>

    
```php

## Notas

> [!NOTE]
> Si se desea generar imágenes JPEG progresivas, es necesario activar el entrelazado utilizando la función `imageinterlace`.

## Véase también

imagepng

imagegif

imagewbmp

imageinterlace

imagetypes
