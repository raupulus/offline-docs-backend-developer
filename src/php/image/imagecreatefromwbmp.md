---
title: imagecreatefromwbmp
description: Crear una nueva imagen a partir de un fichero o una URL
source_url: https://www.php.net/manual/es/function.imagecreatefromwbmp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecreatefromwbmp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 9960a09a5
order: 31860
---

imagecreatefromwbmp

Crear una nueva imagen a partir de un fichero o una URL

## Descripción

```php
imagecreatefromwbmp(string $filename): GdImage
```php

`imagecreatefromwbmp` devuelve un recurso de imagen PHP, que representa la imagen `filename`.

> [!NOTE]
> Las imágenes WBMP son Wireless Bitmaps, y no Windows Bitmaps. Estas últimas pueden cargarse mediante `imagecreatefrombmp`.

> [!TIP]
> Puede utilizar una URL como nombre de archivo con esta función, si el [gestor fopen](#ini.allow-url-fopen) ha sido activado. Véase `fopen` para más detalles sobre cómo especificar el nombre del archivo. Consulte [???](#wrappers) para más información sobre las capacidades de los diferentes gestores, las notas sobre su uso, así como la información sobre las variables predefinidas que proporcionan.

## Parámetros

`filename`  
Ruta de acceso a la imagen WBMP.

## Valores devueltos

Devuelve un objeto de imagen en caso de éxito, `false` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | En caso de éxito, esta función devuelve ahora una instancia de `GDImage` ; anteriormente, se devolvía un `resource`. |

## Ejemplos

Ejemplo de gestión de un error al cargar una imagen WBMP

```
<?php
function LoadWBMP($imgname)
{
    /* Intento de abrir la imagen */
    $im = @imagecreatefromwbmp($imgname);

    /* Procesamiento en caso de fallo */
    if(!$im)
    {
        /* Creación de una imagen vacía */
        $im  = imagecreatetruecolor(150, 30);
        $bgc = imagecolorallocate($im, 255, 255, 255);
        $tc  = imagecolorallocate($im, 0, 0, 0);

        imagefilledrectangle($im, 0, 0, 150, 30, $bgc);

        /* Se muestra un mensaje de error */
        imagestring($im, 1, 5, 5, 'Error de carga ' . $imgname, $tc);
    }

    return $im;
}

header('Content-Type: image/vnd.wap.wbmp');

$img = LoadWBMP('bogus.image');

imagewbmp($img);
?>

   
```php
