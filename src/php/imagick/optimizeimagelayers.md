---
title: Imagick::optimizeImageLayers
description: Elimina las porciones recurrentes de imágenes a optimizar
source_url: https://www.php.net/manual/es/imagick.optimizeimagelayers.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/optimizeimagelayers.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 65c4446ab
order: 34620
---

Imagick::optimizeImageLayers

Elimina las porciones recurrentes de imágenes a optimizar

## Descripción

```php
public Imagick::optimizeImageLayers(): bool
```php

Compara cada imagen GIF con la anterior en la secuencia. A partir de ahí, el método intenta seleccionar la parte más pequeña de la imagen a reemplazar en cada imagen, manteniendo los resultados de la animación. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.2.9 o superior.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Ejemplo con `Imagick::optimizeImageLayers`

Lectura, optimización y escritura de una imagen GIF

```
<?php
/* creación de un nuevo objeto imagick */
$im = new Imagick("test.gif");

/* optimización de las capas */
$im->optimizeImageLayers();

/* escritura de la imagen */
$im->writeImages("test_optimized.gif", true);
?>

    
```php

## Véase también

`Imagick::compareImageLayers`, `Imagick::writeImages`, `Imagick::writeImage`
