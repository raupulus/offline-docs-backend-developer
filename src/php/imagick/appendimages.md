---
title: Imagick::appendImages
description: Añade un conjunto de imágenes
source_url: https://www.php.net/manual/es/imagick.appendimages.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/appendimages.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 32690
---

Imagick::appendImages

Añade un conjunto de imágenes

## Descripción

```php
public Imagick::appendImages(bool $stack): Imagick
```php

Añade un conjunto de imágenes en una imagen más grande.

## Parámetros

`stack`  
Para apilar las imágenes verticalmente. Por defecto (o si `false` se especifica) las imágenes se apilan de izquierda a derecha. Si `stack` es `true`, las imágenes se apilan de arriba hacia abajo.

## Valores devueltos

Devuelve una instancia Imagick si se tuvo éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Ejemplo de Imagick::appendImages

```
<?php

/* Crear un nuevo objeto Imagick */
$im = new Imagick();

/* Crear imágenes de color rojo, verde y azul */
$im->newImage(100, 50, "red");
$im->newImage(100, 50, "green");
$im->newImage(100, 50, "blue");

/* Añadir las imágenes en una sola */
$im->resetIterator();
$combined = $im->appendImages(true);

/* Imprimir la imagen */
$combined->setImageFormat("png");
header("Content-Type: image/png");
echo $combined;
?>

    
```php

Resultado del ejemplo anterior es similar a:

![Salida de ejemplo : Imagick::appendImages()](en/reference/imagick/figures/floodfillpaint_intermediate.png)
