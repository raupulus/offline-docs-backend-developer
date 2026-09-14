---
title: Imagick::flipImage
description: Crea una imagen por espejo vertical
source_url: https://www.php.net/manual/es/imagick.flipimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/flipimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 29168cf80
order: 33260
---

Imagick::flipImage

Crea una imagen por espejo vertical

## Descripción

```php
public Imagick::flipImage(): bool
```php

Crea una imagen por espejo vertical, utilizando una simetría alrededor del eje de las abscisas.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Ejemplo con `Imagick::flipImage`

```
<?php
function flipImage($imagePath) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->flipImage();
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

     
```php

## Véase también

Imagick::flopimage
