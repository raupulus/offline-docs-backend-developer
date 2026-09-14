---
title: Imagick::setIteratorIndex
description: Establece la posición del iterador
source_url: https://www.php.net/manual/es/imagick.setiteratorindex.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/setiteratorindex.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35610
---

Imagick::setIteratorIndex

Establece la posición del iterador

## Descripción

```php
public Imagick::setIteratorIndex(int $index): bool
```php

Establece el iterador a la posición en la lista de imágenes definida por el parámtro index. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.2.9 o superior.

## Parámetros

`index`  
La posición donde se va a establecer el iterador

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Usar `Imagick::setIteratorIndex`:

Crear imágenes, establecer y obtener el índice del iterador

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

`Imagick::getIteratorIndex`, `Imagick::getImageIndex`, `Imagick::setImageIndex`
