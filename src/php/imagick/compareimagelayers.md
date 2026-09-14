---
title: Imagick::compareImageLayers
description: Devuelve la región circundante máxima entre imágenes
source_url: https://www.php.net/manual/es/imagick.compareimagelayers.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/compareimagelayers.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 32930
---

Imagick::compareImageLayers

Devuelve la región circundante máxima entre imágenes

## Descripción

```php
public Imagick::compareImageLayers(int $method): Imagick
```php

Compara cada imagen con la siguiente en una secuencia y devuelve la región circundante máxima de cualesquiera deferencias de píxeles que se descubra. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.2.9 o superior.

## Parámetros

`method`  
Una de las [constantes de método de capas](#imagick.constants.layermethod).

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Usar `Imagick::compareImageLayers`

Comparar las capas de la imagen

```
<?php
/* crear un nuevo objeto imagick */
$im = new Imagick("test.gif");

/* optimizar las capas de la imagen */
$resultado = $im->compareImageLayers(imagick::LAYERMETHOD_COALESCE);

/* trabajar sobre el $resultado */
?>

    
```php

## Véase también

`Imagick::optimizeImageLayers`, `Imagick::writeImages`, `Imagick::writeImage`
