---
title: imageresolution
description: Recupera o define la resolución de la imagen
source_url: https://www.php.net/manual/es/function.imageresolution.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imageresolution.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: 525aa5f19
order: 32280
---

imageresolution

Recupera o define la resolución de la imagen

## Descripción

```php
imageresolution(GdImage $image, [int $resolution_x], [int $resolution_y]): array
```php

`imageresolution` permite definir y recuperar la resolución de una imagen en DPI (puntos por pulgada). Si los parámetros opcionales son `null`, la resolución actual se devuelve en un array indexado. Si únicamente `resolution_x` no es `null`, la resolución horizontal y vertical se establece a este valor. Si ninguno de los parámetros opcionales es `null`, la resolución horizontal y vertical se establecen a estos valores respectivamente.

La resolución se utiliza únicamente como metadatos cuando las imágenes se leen y escriben en formatos que soportan este tipo de información (actualmente PNG y JPEG). Esto no afecta a las operaciones de dibujo. La resolución por defecto de las nuevas imágenes es de 96 DPI.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`resolution_x`  
La resolución horizontal en DPI/PPP.

`resolution_y`  
La resolución vertical en DPI/PPP.

## Valores devueltos

Cuando se utiliza como recuperador, esto devuelve un array indexado con las resoluciones horizontal y vertical en caso de éxito. Cuando se utiliza como definidor, siempre devuelve `true`.

## Historial de cambios

| Versión | Descripción                                         |
|---------|-----------------------------------------------------|
| 8.0.0   | `resolution_x` y `resolution_y` son ahora nullable. |

## Ejemplos

Definir y recuperar la resolución de una imagen

```
<?php
$im = imagecreatetruecolor(100, 100);
imageresolution($im, 200);
print_r(imageresolution($im));
imageresolution($im, 300, 72);
print_r(imageresolution($im));
?>

   
```php

El ejemplo anterior mostrará:

    Array
    (
        [0] => 200
        [1] => 200
    )
    Array
    (
        [0] => 300
        [1] => 72
    )
