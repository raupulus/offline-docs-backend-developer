---
title: imagecreatetruecolor
description: Crea una nueva imagen en colores verdaderos
source_url: https://www.php.net/manual/es/function.imagecreatetruecolor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecreatetruecolor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 9960a09a5
order: 31900
---

imagecreatetruecolor

Crea una nueva imagen en colores verdaderos

## Descripción

```php
imagecreatetruecolor(int $width, int $height): GdImage
```php

`imagecreatetruecolor` devuelve un objeto que representa una imagen negra.

## Parámetros

`width`  
Ancho de la imagen.

`height`  
Alto de la imagen.

## Valores devueltos

Devuelve un objeto de imagen en caso de éxito, `false` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | En caso de éxito, esta función devuelve ahora una instancia de `GDImage` ; anteriormente, se devolvía un `resource`. |

## Ejemplos

Creación de un flujo de imagen GD y visualización

```
<?php
header ('Content-Type: image/png');
$im = @imagecreatetruecolor(120, 20)
      or die('Imposible crear un flujo de imagen GD');
$text_color = imagecolorallocate($im, 233, 14, 91);
imagestring($im, 1, 5, 5,  'Una simple cadena de texto', $text_color);
imagepng($im);
?>

    
```php

Resultado del ejemplo anterior es similar a:

![Visualización del ejemplo: Creación de un nuevo flujo de imagen GD y salida de una imagen.](en/reference/image/figures/imagecreatetruecolor.png)

## Véase también

imagedestroy

imagecreate
