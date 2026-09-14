---
title: Imagick::enhanceImage
description: Mejora la calidad de una imagen ruidosa
source_url: https://www.php.net/manual/es/imagick.enhanceimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/enhanceimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: 65c4446ab
order: 33190
---

Imagick::enhanceImage

Mejora la calidad de una imagen ruidosa

## Descripción

```php
public Imagick::enhanceImage(): bool
```php

Mejora la calidad de una imagen ruidosa con un filtro digital.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Ejemplo con `Imagick::enhanceImage`

```
<?php
function enhanceImage($imagePath) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->enhanceImage();
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

     
```php
