---
title: imagecreate
description: Crea una nueva imagen con paleta
source_url: https://www.php.net/manual/es/function.imagecreate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecreate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 9960a09a5
order: 31750
---

imagecreate

Crea una nueva imagen con paleta

## Descripción

```php
imagecreate(int $width, int $height): GdImage
```php

`imagecreate` devuelve un identificador de imagen que representa una imagen vacía.

En general, se recomienda el uso de la función `imagecreatetruecolor` en lugar de la función `imagecreate` para que las operaciones sobre la imagen se realicen con la mayor calidad posible. Si se desea utilizar una paleta, entonces la función `imagetruecolortopalette` debe ser llamada inmediatamente antes de guardar la imagen con la función `imagepng` o la función `imagegif`.

## Parámetros

`width`  
El ancho de la imagen.

`height`  
La altura de la imagen.

## Valores devueltos

Devuelve un objeto de imagen en caso de éxito, `false` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | En caso de éxito, esta función devuelve ahora una instancia de `GDImage` ; anteriormente, se devolvía un `resource`. |

## Ejemplos

Creación de una imagen GD y visualización de esta imagen

```
<?php
header("Content-Type: image/png");
$im = @imagecreate(110, 20)
    or die("Imposible inicializar la biblioteca GD");
$background_color = imagecolorallocate($im, 0, 0, 0);
$text_color = imagecolorallocate($im, 233, 14, 91);
imagestring($im, 1, 5, 5,  "A Simple Text String", $text_color);
imagepng($im);
?>

    
```php

Resultado del ejemplo anterior es similar a:

![Visualización del ejemplo : imagecreate()](en/reference/image/figures/imagecreate.png)

## Véase también

imagedestroy

imagecreatetruecolor
