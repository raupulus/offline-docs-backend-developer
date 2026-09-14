---
title: exif_thumbnail
description: Recupera la miniatura de una imagen
source_url: https://www.php.net/manual/es/function.exif-thumbnail.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/exif/functions/exif-thumbnail.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: exif
translation_status: ready
translation_reviewed: true
translation_revision: 6a08181be
order: 20700
---

exif_thumbnail

Recupera la miniatura de una imagen

## Descripción

```php
exif_thumbnail(resource $file, [int $width], [int $height], [int $image_type]): string
```php

`exif_thumbnail` lee la miniatura de la imagen.

Si se desea mostrar miniaturas con esta función, debe enviarse el tipo MIME adecuado con la función `header`.

Es posible que la función `exif_thumbnail` no logre crear la imagen pero pueda determinar su tamaño. En este caso, la función devuelve `false` pero los parámetros `width` y `height` están definidos.

## Parámetros

`file`  
Ubicación del fichero de imagen. Puede tratarse de una ruta de acceso al fichero o de un flujo `resource`.

`width`  
El ancho devuelto de la miniatura devuelta.

`height`  
La altura devuelta de la miniatura devuelta.

`image_type`  
El tipo de imagen devuelto de la miniatura devuelta. Puede ser TIFF o JPEG.

## Valores devueltos

Devuelve la miniatura integrada o `false` si la imagen no contiene miniatura.

## Historial de cambios

| Versión | Descripción                                                       |
|---------|-------------------------------------------------------------------|
| 7.2.0   | El parámetro `file` soporta ficheros locales o recursos de flujo. |

## Ejemplos

Ejemplo con `exif_thumbnail`

```
<?php
if (array_key_exists('file', $_REQUEST)) {
    $image = exif_thumbnail($_REQUEST['file'], $width, $height, $type);
} else {
    $image = false;
}
if ($image!==false) {
    header('Content-type: ' .image_type_to_mime_type($type));
    echo $image;
    exit;
} else {
    // no hay miniatura disponible, tratamiento del error aquí
    echo 'No hay miniatura disponible';
}
?>

   
```php

## Notas

> [!NOTE]
> Si el parámetro `file` se utiliza para pasar un flujo a la función, entonces el flujo debe ser reposicionable. Tenga en cuenta que la posición del puntero de un fichero no se modifica después del retorno de esta función.

## Véase también

exif_read_data

image_type_to_mime_type
