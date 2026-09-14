---
title: exif_imagetype
description: Determinar el tipo de una imagen
source_url: https://www.php.net/manual/es/function.exif-imagetype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/exif/functions/exif-imagetype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: exif
translation_status: ready
translation_reviewed: false
translation_revision: f8bab1dfb
order: 20670
---

exif_imagetype

Determinar el tipo de una imagen

## Descripción

```php
exif_imagetype(string $filename): int
```php

`exif_imagetype` lee los primeros bytes de una imagen y verifica su firma.

`exif_imagetype` puede usarse para evitar llamadas a otras [funciones exif](#ref.exif) con tipos de fichero no soportados o en conjunto con `$_SERVER['HTTP_ACCEPT']` para verificar si el visor es capaz de mostrar una imagen específica en el navegador.

## Parámetros

`filename`  
La imagen que se está verificando.

## Valores devueltos

Cuando se encuentra una firma correcta, se devolverá el valor constante apropiado; de lo contrario, se devolverá `false`. El valor devuelto es el mismo que el que devuelve `getimagesize` en el índice 2, pero `exif_imagetype` es mucho más rápido.

Se definen las siguientes constantes, que representan los posibles valores de retorno de `exif_imagetype`:

| Valor | Constante                                     |
|-------|-----------------------------------------------|
| 1     | `IMAGETYPE_GIF`                               |
| 2     | `IMAGETYPE_JPEG`                              |
| 3     | `IMAGETYPE_PNG`                               |
| 4     | `IMAGETYPE_SWF`                               |
| 5     | `IMAGETYPE_PSD`                               |
| 6     | `IMAGETYPE_BMP`                               |
| 7     | `IMAGETYPE_TIFF_II` (orden de bytes Intel)    |
| 8     | `IMAGETYPE_TIFF_MM` (orden de bytes Motorola) |
| 9     | `IMAGETYPE_JPC`                               |
| 10    | `IMAGETYPE_JP2`                               |
| 11    | `IMAGETYPE_JPX`                               |
| 12    | `IMAGETYPE_JB2`                               |
| 13    | `IMAGETYPE_SWC`                               |
| 14    | `IMAGETYPE_IFF`                               |
| 15    | `IMAGETYPE_WBMP`                              |
| 16    | `IMAGETYPE_XBM`                               |
| 17    | `IMAGETYPE_ICO`                               |
| 18    | `IMAGETYPE_WEBP`                              |
| 19    | `IMAGETYPE_AVIF`                              |
| 20    | `IMAGETYPE_HEIF`                              |

Constantes de tipos de imagen

> [!NOTE]
> `exif_imagetype` emitirá una `E_NOTICE` y devolverá `false` si no puede leer suficientes bytes del fichero para determinar el tipo de imagen.

## Historial de cambios

| Versión | Descripción                  |
|---------|------------------------------|
| 7.1.0   | Se añadió soporte para WebP. |
| 8.1.0   | Se añadió soporte para AVIF. |
| 8.5.0   | Se añadió soporte para HEIF. |

## Ejemplos

Ejemplo de `exif_imagetype`

```
<?php
if (exif_imagetype('image.gif') != IMAGETYPE_GIF) {
    echo 'La imagen no es un gif';
}
?>

    
```php

## Véase también

image_type_to_mime_type

getimagesize
