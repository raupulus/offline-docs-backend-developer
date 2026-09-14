---
title: Imagick::magnifyImage
description: Duplica el tamaño de una imagen, proporcionalmente
source_url: https://www.php.net/manual/es/imagick.magnifyimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/magnifyimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: 65c4446ab
order: 34430
---

Imagick::magnifyImage

Duplica el tamaño de una imagen, proporcionalmente

## Descripción

```php
public Imagick::magnifyImage(): bool
```php

Este método es un atajo para duplicar el tamaño de una imagen.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Ejemplo con `Imagick::magnifyImage`

```
<?php
function magnifyImage($imagePath) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->magnifyImage();
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

     
```php
