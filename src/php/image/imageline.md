---
title: imageline
description: Dibuja una línea
source_url: https://www.php.net/manual/es/function.imageline.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imageline.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: fcd921429
order: 32200
---

imageline

Dibuja una línea

## Descripción

```php
imageline(GdImage $image, int $x1, int $y1, int $x2, int $y2, int $color): true
```php

Dibuja una línea entre dos puntos proporcionados.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`x1`  
X: coordenada del primer punto.

`y1`  
Y: coordenada del primer punto.

`x2`  
X: coordenada del segundo punto.

`y2`  
Y: coordenada del segundo punto.

`color`  
El color de relleno. Un identificador de color creado con `imagecolorallocate`.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Dibuja una línea fina

```
<?php

function imagelinethick($image, $x1, $y1, $x2, $y2, $color, $thick = 1)
{
    /* de esta manera, solo funciona bien para líneas ortogonales
    imagesetthickness($image, $thick);
    return imageline($image, $x1, $y1, $x2, $y2, $color);
    */
    if ($thick == 1) {
        return imageline($image, $x1, $y1, $x2, $y2, $color);
    }
    $t = $thick / 2 - 0.5;
    if ($x1 == $x2 || $y1 == $y2) {
        return imagefilledrectangle($image, round(min($x1, $x2) - $t), round(min($y1, $y2) - $t), round(max($x1, $x2) + $t), round(max($y1, $y2) + $t), $color);
    }
    $k = ($y2 - $y1) / ($x2 - $x1); //y = kx + q
    $a = $t / sqrt(1 + pow($k, 2));
    $points = array(
        round($x1 - (1+$k)*$a), round($y1 + (1-$k)*$a),
        round($x1 - (1-$k)*$a), round($y1 - (1+$k)*$a),
        round($x2 + (1+$k)*$a), round($y2 - (1-$k)*$a),
        round($x2 + (1-$k)*$a), round($y2 + (1+$k)*$a),
    );
    imagefilledpolygon($image, $points, 4, $color);
    return imagepolygon($image, $points, 4, $color);
}

?>

    
```php

## Véase también

imagecreatetruecolor

imagecolorallocate
