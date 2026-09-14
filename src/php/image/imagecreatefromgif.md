---
title: imagecreatefromgif
description: Crear una nueva imagen a partir de un fichero o una URL
source_url: https://www.php.net/manual/es/function.imagecreatefromgif.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecreatefromgif.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 9960a09a5
order: 31810
---

imagecreatefromgif

Crear una nueva imagen a partir de un fichero o una URL

## Descripción

```php
imagecreatefromgif(string $filename): GdImage
```php

`imagecreatefromgif` devuelve un identificador de imagen que representa la imagen obtenida a partir del fichero cuyo nombre es dado por `filename`.

> [!CAUTION]
> Al leer en memoria ficheros GIF animados, solo el primer frame es devuelto por el objeto de la imagen. El tamaño de la imagen no es necesariamente el que se reporta mediante `getimagesize`.

> [!TIP]
> Puede utilizar una URL como nombre de archivo con esta función, si el [gestor fopen](#ini.allow-url-fopen) ha sido activado. Véase `fopen` para más detalles sobre cómo especificar el nombre del archivo. Consulte [???](#wrappers) para más información sobre las capacidades de los diferentes gestores, las notas sobre su uso, así como la información sobre las variables predefinidas que proporcionan.

## Parámetros

`filename`  
Ruta hacia la imagen GIF.

## Valores devueltos

Devuelve un objeto de imagen en caso de éxito, `false` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | En caso de éxito, esta función devuelve ahora una instancia de `GDImage` ; anteriormente, se devolvía un `resource`. |

## Ejemplos

Ejemplo de manejo de errores al cargar una imagen GIF

```
<?php
function LoadGif($imgname)
{
    /* Intenta abrir la imagen */
    $im = @imagecreatefromgif($imgname);

    /* Procesamiento si la apertura falló */
    if(!$im)
    {
        /* Creación de una imagen vacía */
        $im = imagecreatetruecolor (150, 30);
        $bgc = imagecolorallocate ($im, 255, 255, 255);
        $tc = imagecolorallocate ($im, 0, 0, 0);

        imagefilledrectangle ($im, 0, 0, 150, 30, $bgc);

        /* Muestra un mensaje de error en la imagen */
        imagestring ($im, 1, 5, 5, 'Error loading ' . $imgname, $tc);
    }

    return $im;
}

header('Content-Type: image/gif');

$img = LoadGif('bogus.image');

imagegif($img);
?>

   
```php

Resultado del ejemplo anterior es similar a:

![Visualización del ejemplo: imagecreatefromgif()](en/reference/image/figures/imagecreatefromgif.gif)
