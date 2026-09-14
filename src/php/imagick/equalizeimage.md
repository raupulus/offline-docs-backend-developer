---
title: Imagick::equalizeImage
description: Iguala el histograma de una imagen
source_url: https://www.php.net/manual/es/imagick.equalizeimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/equalizeimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: 65c4446ab
order: 33200
---

Imagick::equalizeImage

Iguala el histograma de una imagen

## Descripción

```php
public Imagick::equalizeImage(): bool
```php

Iguala el histograma de una imagen.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Ejemplo con `Imagick::equalizeImage`

```
<?php
function equalizeImage($imagePath) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->equalizeImage();
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

     
```php
