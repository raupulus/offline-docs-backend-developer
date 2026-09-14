---
title: imagelayereffect
description: Activa la opción de mezcla alfa para utilizar los efectos de libgd
source_url: https://www.php.net/manual/es/function.imagelayereffect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagelayereffect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: fcd921429
order: 32190
---

imagelayereffect

Activa la opción de mezcla alfa para utilizar los efectos de libgd

## Descripción

```php
imagelayereffect(GdImage $image, int $effect): true
```php

Activa la opción de mezcla alfa para utilizar los efectos de libgd.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`effect`  
Una de las constantes siguientes:

`IMG_EFFECT_REPLACE`  
Utiliza el reemplazo de píxeles (equivalente a pasar `true` a la función `imagealphablending`)

`IMG_EFFECT_ALPHABLEND`  
Utiliza la mezcla normal de píxeles (equivalente a pasar `false` a la función `imagealphablending`)

`IMG_EFFECT_NORMAL`  
Idéntico a la constante `IMG_EFFECT_ALPHABLEND`.

`IMG_EFFECT_OVERLAY`  
El overlay tiene como efecto que los píxeles negros del fondo permanecerán negros, los blancos del fondo permanecerán blancos, pero los grises del fondo tomarán el color del píxel del primer plano.

`IMG_EFFECT_MULTIPLY`  
Overlay con un efecto de multiplicación.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |
| 7.2.0 | Añadida la constante `IMG_EFFECT_MULTIPLY` (requiere la libgd del sistema \>= 2.1.1 o la libgd integrada). |

## Ejemplos

Ejemplo con `imagelayereffect`

```
<?php
// Creación de una imagen
$im = imagecreatetruecolor(100, 100);

// Define el fondo
imagefilledrectangle($im, 0, 0, 100, 100, imagecolorallocate($im, 220, 220, 220));

// Aplica el overlay
imagelayereffect($im, IMG_EFFECT_OVERLAY);

// Dibuja 2 elipses grises
imagefilledellipse($im, 50, 50, 40, 40, imagecolorallocate($im, 100, 255, 100));
imagefilledellipse($im, 50, 50, 50, 80, imagecolorallocate($im, 100, 100, 255));
imagefilledellipse($im, 50, 50, 80, 50, imagecolorallocate($im, 255, 100, 100));

// Visualización
header('Content-type: image/png');

imagepng($im);
?>

   
```php

Resultado del ejemplo anterior es similar a:

![Visualización del ejemplo: imagelayereffect()](en/reference/image/figures/imagelayereffect.png)
