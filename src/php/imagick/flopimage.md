---
title: Imagick::flopImage
description: Crea una imagen por espejo horizontal
source_url: https://www.php.net/manual/es/imagick.flopimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/flopimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 29168cf80
order: 33280
---

Imagick::flopImage

Crea una imagen por espejo horizontal

## Descripción

```php
public Imagick::flopImage(): bool
```php

Crea una imagen por espejo horizontal, utilizando una simetría alrededor del eje de las ordenadas.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Ejemplo con `Imagick::flopImage`

```
<?php
function flopImage($imagePath) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->flopImage();
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

     
```php

## Véase también

Imagick::flipimage
