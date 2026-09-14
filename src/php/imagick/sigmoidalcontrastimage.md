---
title: Imagick::sigmoidalContrastImage
description: Ajusta el contraste de la imagen
source_url: https://www.php.net/manual/es/imagick.sigmoidalcontrastimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/sigmoidalcontrastimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 6047c10c1
order: 35790
---

Imagick::sigmoidalContrastImage

Ajusta el contraste de la imagen

## Descripción

```php
public Imagick::sigmoidalContrastImage(bool $sharpen, float $alpha, float $beta, [int $channel]): bool
```php

Ajusta el contraste de la imagen con un algoritmo de contraste sigmoide no lineal. Aumenta el contraste de la imagen utilizando una función de transferencia sigmoide sin saturar las luces altas y las sombras. El contraste indica cuánto debe aumentarse (0 para no hacer nada, 3 es un valor típico, 20 es un valor alto); el punto medio indica dónde estarán los tonos medios en la imagen resultante (0 corresponde a blanco, 50 a gris y 100 a negro). Establezca el parámetro `sharpen` en `true` para aumentar el contraste de la imagen; de lo contrario, el contraste se reducirá.

Consulte también los [ejemplos de ImageMagick V6 - Transformaciones de imágenes - Contraste no lineal](https://usage.imagemagick.org/color_mods/#sigmoidal)

## Parámetros

`sharpen`  
Si es `true`, el contraste aumentará; de lo contrario, el contraste disminuirá.

`alpha`  
La cantidad de contraste a aplicar. -1 representa una cantidad muy pequeña, 5 una cantidad significativa y 20 el máximo.

`beta`  
Dónde debe situarse el punto medio del gradiente. Este valor debe estar en el intervalo 0-1, multiplicado por el valor del quantum para ImageMagick.

`channel`  
Canales de color sobre los cuales debe aplicarse el contraste.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Crea un degradado de imagen utilizando el método `Imagick::sigmoidalContrastImage` para mezclar dos imágenes suavemente, donde la mezcla está definida por las variables \$contrast y \$midpoint.

```
<?php

function generateBlendImage($width, $height, $contrast = 10, $midpoint = 0.5) {
    $imagick = new Imagick();
    $imagick->newPseudoImage($width, $height, 'gradient:black-white');
    $quanta = $imagick->getQuantumRange();
    $imagick->sigmoidalContrastImage(true, $contrast, $midpoint * $quanta["quantumRangeLong"]);

    return $imagick;
}

?>

    
```php
