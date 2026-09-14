---
title: imageavif
description: Enviar la imagen al navegador o a un fichero
source_url: https://www.php.net/manual/es/function.imageavif.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imageavif.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_revision: 24641aea6
order: 31490
---

imageavif

Enviar la imagen al navegador o a un fichero

## Descripción

```php
imageavif(GdImage $image, [resource $file], [int $quality], [int $speed]): bool
```php

Muestra o guarda una imagen en formato AVIF utilizando la `image` proporcionada.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`file`  
La ruta o un recurso de flujo abierto (que se cierra automáticamente después de que esta función retorne) donde guardar el fichero. Si no se define o es `null`, el flujo de imagen sin procesar se enviará directamente.

`quality`  
`quality` es un argumento opcional cuyo rango varía de 0 (peor calidad, archivo más pequeño) a 100 (mejor calidad, archivo más grande). Si se pasa `-1` como argumento, se utilizará el valor por omisión `52`.

`speed`  
`speed` es un argumento opcional cuyo rango varía de 0 (codificación lenta, archivo más pequeño) a 10 (codificación rápida, archivo más grande). Si se pasa `-1` como argumento, se utilizará el valor por omisión `6`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

> [!CAUTION]
> Sin embargo, si libgd no logra producir la imagen, esta función devuelve `true`.

## Errores/Excepciones

Genera una `ValueError` si `quality` o `speed` no es válido.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Genera ahora una `ValueError` si `quality` o `speed` no es válido. |

## Véase también

imagepng

imagewbmp

imagejpeg

imagetypes
