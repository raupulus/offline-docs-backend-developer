---
title: imagecreatefromxpm
description: Crear una nueva imagen a partir de un fichero o una URL
source_url: https://www.php.net/manual/es/function.imagecreatefromxpm.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecreatefromxpm.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 9960a09a5
order: 31890
---

imagecreatefromxpm

Crear una nueva imagen a partir de un fichero o una URL

## Descripción

```php
imagecreatefromxpm(string $filename): GdImage
```php

`imagecreatefromxpm` devuelve un identificador de imagen que representa la imagen obtenida a partir del archivo `filename`.

> [!TIP]
> Puede utilizar una URL como nombre de archivo con esta función, si el [gestor fopen](#ini.allow-url-fopen) ha sido activado. Véase `fopen` para más detalles sobre cómo especificar el nombre del archivo. Consulte [???](#wrappers) para más información sobre las capacidades de los diferentes gestores, las notas sobre su uso, así como la información sobre las variables predefinidas que proporcionan.

## Parámetros

`filename`  
Ruta de acceso a la imagen XPM.

## Valores devueltos

Devuelve un objeto de imagen en caso de éxito, `false` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | En caso de éxito, esta función devuelve ahora una instancia de `GDImage` ; anteriormente, se devolvía un `resource`. |

## Ejemplos

Creación de una instancia de imagen utilizando la función `imagecreatefromxpm`

```
<?php
// Verifica el soporte XPM
if(!(imagetypes() & IMG_XPM))
{
    die('El soporte XPM no ha podido ser verificado !');
}

// Creación de la instancia de una imagen
$xpm = imagecreatefromxpm('./example.xpm');

// Algunas operaciones sobre la imagen aquí

// PHP no tiene soporte para la escritura de imágenes XPM
// por lo tanto, en este caso, se guarda la imagen en un archivo JPEG
// con una calidad del 100%
imagejpeg($xpm, './example.jpg', 100);
?>

    
```php
