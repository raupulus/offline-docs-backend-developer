---
title: imagexbm
description: Genera una imagen en formato XBM
source_url: https://www.php.net/manual/es/function.imagexbm.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagexbm.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 9960a09a5
order: 32490
---

imagexbm

Genera una imagen en formato XBM

## Descripción

```php
imagexbm(GdImage $image, string $filename, [int $foreground_color]): bool
```php

Muestra o guarda una versión XBM de la imagen `image`.

> [!NOTE]
> `imagexbm` no aplica relleno, por lo que el ancho de la imagen debe ser un múltiplo de 8. Esta restricción ya no se aplica a partir de PHP 7.0.9, respectivamente.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`filename`  
Ruta de acceso donde se guardará el fichero, en forma de `string`. Si no está definido, el flujo de imágenes RAW se mostrará directamente en la salida estándar.

El nombre de fichero `filename` (sin la extensión .xbm) también se utiliza para los identificadores C del XBM, en cuyo caso los caracteres no alfanuméricos de la configuración local actual son reemplazados por subrayados. Si `filename` tiene el valor null, `image` se utiliza para generar los identificadores C.

`foreground_color`  
Puede definirse el primer plano con este parámetro definiendo un identificador obtenido desde la función `imagecolorallocate`. Por omisión, el color del primer plano es negro. Todas las demás colores se tratan como fondo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

> [!CAUTION]
> Sin embargo, si libgd no logra producir la imagen, esta función devuelve `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |
| 8.0.0 | `foreground_color` ahora es nullable. |
| 8.0.0 | El cuarto parámetro, que no se utilizaba, ha sido eliminado. |

## Ejemplos

Guardar un fichero XBM

```
<?php
// Creación de una imagen vacía y adición de texto
$im = imagecreatetruecolor(120, 20);
$text_color = imagecolorallocate($im, 233, 14, 91);
imagestring($im, 1, 5, 5,  'Un texto simple', $text_color);

// Guardar la imagen
imagexbm($im, 'simpletext.xbm');

?>

    
```php

Guardar un fichero XBM con un color de primer plano diferente

```
<?php
// Creación de una imagen vacía y adición de texto
$im = imagecreatetruecolor(120, 20);
$text_color = imagecolorallocate($im, 233, 14, 91);
imagestring($im, 1, 5, 5,  'Un texto simple', $text_color);

// Definir el color de primer plano
$foreground_color = imagecolorallocate($im, 255, 0, 0);

// Guardar la imagen
imagexbm($im, NULL, $foreground_color);

?>

    
```php
