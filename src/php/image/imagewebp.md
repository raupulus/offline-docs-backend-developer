---
title: imagewebp
description: Muestra una imagen WebP hacia un navegador o un fichero
source_url: https://www.php.net/manual/es/function.imagewebp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagewebp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: 8f76f001f
order: 32480
---

imagewebp

Muestra una imagen WebP hacia un navegador o un fichero

## Descripción

```php
imagewebp(GdImage $image, [resource $file], [int $quality]): bool
```php

Muestra o guarda una versión WebP de la `image` proporcionada.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`file`  
La ruta o un recurso de flujo abierto (que se cierra automáticamente después de que esta función retorne) donde guardar el fichero. Si no se define o es `null`, el flujo de imagen sin procesar se enviará directamente.

`quality`  
`quality` rango de 0 (la peor calidad, fichero más pequeño) a 100 (mejor calidad, fichero más grande). Si se proporciona el valor `-1`, se utiliza el valor por omisión `80`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

> [!CAUTION]
> Sin embargo, si libgd no logra producir la imagen, esta función devuelve `true`.

## Errores/Excepciones

Genera una `ValueError` si `quality` es inválido.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Genera ahora una `ValueError` si `quality` es inválido. |
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Guardado de un fichero WebP

```
<?php
// Crea una imagen vacía y se añade texto
$im = imagecreatetruecolor(120, 20);
$text_color = imagecolorallocate($im, 233, 14, 91);

imagestring($im, 1, 5, 5,  'WebP con PHP', $text_color);

// Guardado de la imagen
imagewebp($im, 'php.webp');

?>

    
```php
