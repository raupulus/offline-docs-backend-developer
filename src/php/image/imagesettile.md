---
title: imagesettile
description: Modifica la imagen utilizada para el mosaico
source_url: https://www.php.net/manual/es/function.imagesettile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagesettile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: fcd921429
order: 32380
---

imagesettile

Modifica la imagen utilizada para el mosaico

## Descripción

```php
imagesettile(GdImage $image, GdImage $tile): true
```php

`imagesettile` reemplaza la imagen de pavimentación actual por la imagen `tile`, a utilizar en todos los rellenos (como con las funciones `imagefill` y `imagefilledpolygon`) durante los rellenos con la opción `IMG_COLOR_TILED`.

Una imagen de mosaico es una imagen utilizada para rellenar una zona, de manera repetitiva. *Cualquier imagen GD* puede servir como imagen de relleno. El uso de la transparencia (gestionada con la función `imagecolortransparent`) permite que ciertas zonas aparezcan a través del mosaico.

> [!CAUTION]
> No hay nada que hacer cuando se ha terminado con un pincel, pero si se destruye la imagen del pincel (o se deja que PHP lo destruya), ya no DEBE utilizarse la opción `IMG_COLOR_TILED` de las funciones `imagefill` y `imagefilledpolygon`, antes de crear un nuevo pincel.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`tile`  
El objeto de la imagen a utilizar como mosaico.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` y `tile` ahora esperan instancias de `GdImage` ; anteriormente, se esperaban `resource`s. |

## Ejemplos

Ejemplo con `imagesettile`

```
<?php
// Carga de una imagen externa
$zend = imagecreatefromgif('./zend.gif');

// Creación de una imagen de 200x200 píxeles
$im = imagecreatetruecolor(200, 200);

// Definición del mosaico
imagesettile($im, $zend);

// Repetición de la imagen
imagefilledrectangle($im, 0, 0, 199, 199, IMG_COLOR_TILED);

// Visualización en el navegador
header('Content-Type: image/png');

imagepng($im);
?>

    
```php

Resultado del ejemplo anterior es similar a:

![Visualización del ejemplo: imagesettile()](en/reference/image/figures/imagesettile.png)
