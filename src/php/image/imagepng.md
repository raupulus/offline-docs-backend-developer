---
title: imagepng
description: Envía una imagen PNG a un navegador o a un fichero
source_url: https://www.php.net/manual/es/function.imagepng.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagepng.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: 9960a09a5
order: 32250
---

imagepng

Envía una imagen PNG a un navegador o a un fichero

## Descripción

```php
imagepng(GdImage $image, [resource $file], [int $quality], [int $filters]): bool
```php

`imagepng` muestra o guarda una imagen en formato PNG utilizando la imagen `image`.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`file`  
La ruta o un recurso de flujo abierto (que se cierra automáticamente después de que esta función retorne) donde guardar el fichero. Si no se define o es `null`, el flujo de imagen sin procesar se enviará directamente.

> [!NOTE]
> El valor `null` es inválido si el argumento `quality` y el argumento `filters` no son utilizados.

`quality`  
Grado de compresión: desde 0 (ninguna compresión) hasta 9. El valor por omisión (`-1`) utiliza la compresión por omisión de zlib. Para más información ver el [manual zlib](http://www.zlib.net/manual.html).

`filters`  
Permite la reducción del tamaño del fichero PNG. Es una máscara que puede ser definida por una combinación de las constantes `PNG_FILTER_*`. `PNG_NO_FILTER` o `PNG_ALL_FILTERS` pueden ser utilizados para, respectivamente, desactivar o activar todos los filtros. El valor por omisión (`-1`) desactiva el filtrado.

> [!CAUTION]
> El argumento `filters` es ignorado por la libgd del sistema.

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

```
<?php
$im = imagecreatefrompng("test.png");

header('Content-Type: image/png');

imagepng($im);
?>

    
```php

## Véase también

imagegif

imagewbmp

imagejpeg

imagetypes

imagesavealpha
