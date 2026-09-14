---
title: imagecolorat
description: Devuelve el índice del color de un píxel dado
source_url: https://www.php.net/manual/es/function.imagecolorat.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecolorat.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 593ea510e
order: 31550
---

imagecolorat

Devuelve el índice del color de un píxel dado

## Descripción

```php
imagecolorat(GdImage $image, int $x, int $y): int
```php

Devuelve el índice del color del píxel situado en las coordenadas especificadas, en la imagen `image`.

Si la imagen es una imagen en TrueColor, esta función devuelve el valor RGB del píxel, en forma de un entero. Utilizar los operadores a nivel de bits y los máscaras para distinguir el rojo, del verde y del azul :

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`x`  
X : coordenada del punto.

`y`  
Y : coordenada del punto.

## Valores devueltos

Devuelve el índice del color o `false` si ocurre un error.

> [!WARNING]
> Esta función puede retornar `false`, pero también puede retornar un valor equivalente a `false`. Por favor, lea la sección sobre los [booleanos](#language.types.boolean) para más información. Utilice el [operador ===](#language.operators.comparison) para probar el valor de retorno exacto de esta función.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Acceso a los valores RGB

```
<?php
$im = imagecreatefrompng("php.png");
$rgb = imagecolorat($im, 10, 15);
$r = ($rgb >> 16) & 0xFF;
$g = ($rgb >> 8) & 0xFF;
$b = $rgb & 0xFF;
var_dump($r, $g, $b);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    int(119)
    int(123)
    int(180)

Valores RVB legibles utilizando la función `imagecolorsforindex`

```
<?php
$im = imagecreatefrompng("php.png");
$rgb = imagecolorat($im, 10, 15);

$colors = imagecolorsforindex($im, $rgb);

var_dump($colors);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    array(4) {
      ["red"]=>
      int(119)
      ["green"]=>
      int(123)
      ["blue"]=>
      int(180)
      ["alpha"]=>
      int(127)
    }

## Véase también

imagecolorset

imagecolorsforindex

imagesetpixel
