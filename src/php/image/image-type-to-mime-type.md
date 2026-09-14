---
title: image_type_to_mime_type
description: Obtiene el tipo MIME para el tipo de imagen devuelto por getimagesize,
  exif_read_data, exif_thumbnail, exif_imagetype
source_url: https://www.php.net/manual/es/function.image-type-to-mime-type.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/image-type-to-mime-type.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: f8bab1dfb
order: 31410
---

image_type_to_mime_type

Obtiene el tipo MIME para el tipo de imagen devuelto por getimagesize, exif_read_data, exif_thumbnail, exif_imagetype

## Descripción

```php
image_type_to_mime_type(int $image_type): string
```php

La función `image_type_to_mime_type` determina el tipo MIME para una constante IMAGETYPE.

## Parámetros

`image_type`  
Una de las constantes `IMAGETYPE_*`.

## Valores devueltos

Los valores devueltos son los siguientes:

| `image_type` | Valor devuelto |
|----|----|
| `IMAGETYPE_GIF` | `image/gif` |
| `IMAGETYPE_JPEG` | `image/jpeg` |
| `IMAGETYPE_PNG` | `image/png` |
| `IMAGETYPE_SWF` | `application/x-shockwave-flash` |
| `IMAGETYPE_PSD` | `image/psd` |
| `IMAGETYPE_BMP` | `image/bmp` |
| `IMAGETYPE_TIFF_II` (orden de bytes intel) | `image/tiff` |
| `IMAGETYPE_TIFF_MM` (orden de bytes motorola) | `image/tiff` |
| `IMAGETYPE_JPC` | `application/octet-stream` |
| `IMAGETYPE_JP2` | `image/jp2` |
| `IMAGETYPE_JPX` | `application/octet-stream` |
| `IMAGETYPE_JB2` | `application/octet-stream` |
| `IMAGETYPE_SWC` | `application/x-shockwave-flash` |
| `IMAGETYPE_IFF` | `image/iff` |
| `IMAGETYPE_WBMP` | `image/vnd.wap.wbmp` |
| `IMAGETYPE_XBM` | `image/xbm` |
| `IMAGETYPE_ICO` | `image/vnd.microsoft.icon` |
| `IMAGETYPE_WEBP` | `image/webp` |
| `IMAGETYPE_AVIF` | `image/avif` |
| `IMAGETYPE_HEIF` | `image/heif` |

Valores constantes devueltos

## Ejemplos

Ejemplo de `image_type_to_mime_type`

```
<?php
header("Content-type: " . image_type_to_mime_type(IMAGETYPE_PNG));
?>

    
```php

## Notas

> [!NOTE]
> Esta función no requiere la biblioteca GD.

## Véase también

getimagesize

exif_imagetype

exif_read_data

exif_thumbnail
