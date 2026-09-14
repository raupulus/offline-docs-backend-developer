---
title: Imagick::subImageMatch
description: Busca una subimagen en la imagen actual y devuelve una imagen de similitud
source_url: https://www.php.net/manual/es/imagick.subimagematch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/subimagematch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 1ef9c7a76
order: 35900
---

Imagick::subImageMatch

Busca una subimagen en la imagen actual y devuelve una imagen de similitud

## Descripción

```php
public Imagick::subImageMatch(Imagick $Imagick, [array $offset], [float $similarity]): Imagick
```php

Busca una subimagen en la imagen actual y devuelve una imagen de similitud de tal manera que una posición de coincidencia exacta es completamente blanca y si ningún píxel coincide, negro, de lo contrario un cierto nivel de gris entre ambos. Asimismo, pueden pasarse los argumentos opcionales bestMatch y similarity. Tras llamar a la función, similarity será definido en el 'puntuación' de similitud entre la subimagen y la posición correspondiente en la imagen más grande, bestMatch contendrá un array asociativo con los elementos x, y, width, height que describen la región correspondiente.

## Parámetros

`Imagick`  

`offset`  

`similarity`  
Una nueva imagen que muestra la cantidad de similitud en cada píxel.

## Valores devueltos

## Ejemplos

`Imagick::subImageMatch`

```
      
<?php
function subImageMatch($imagePath) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick2 = clone $imagick;
    $imagick2->cropimage(40, 40, 250, 110);
    $imagick2->vignetteimage(0, 1, 3, 3);

    $similarity = null;
    $bestMatch = null;
    $comparison = $imagick->subImageMatch($imagick2, $bestMatch, $similarity);

    $comparison->setImageFormat('png');
    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

?>

      
```php
