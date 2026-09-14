---
title: Imagick::getIteratorIndex
description: Lee el índice de la imagen activa actual
source_url: https://www.php.net/manual/es/imagick.getiteratorindex.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/getiteratorindex.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 65c4446ab
order: 34110
---

Imagick::getIteratorIndex

Lee el índice de la imagen activa actual

## Descripción

```php
public Imagick::getIteratorIndex(): int
```php

Lee el índice de la imagen activa actual en el objeto Imagick. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.2.9 o superior.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un entero que representa el índice de la imagen en la cola.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Ejemplo con `Imagick::getIteratorIndex`

Crea imágenes, define y recupera el índice del iterador.

```
<?php
$im = new Imagick();
$im->newImage(100, 100, new ImagickPixel("red"));
$im->newImage(100, 100, new ImagickPixel("green"));
$im->newImage(100, 100, new ImagickPixel("blue"));

$im->setIteratorIndex(1);
echo $im->getIteratorIndex();
?>

    
```php

## Véase también

`Imagick::setIteratorIndex`, `Imagick::getImageIndex`, `Imagick::setImageIndex`
