---
title: Imagick::setImageOrientation
description: Establece la orientación de la imagen
source_url: https://www.php.net/manual/es/imagick.setimageorientation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/setimageorientation.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35470
---

Imagick::setImageOrientation

Establece la orientación de la imagen

## Descripción

```php
public Imagick::setImageOrientation(int $orientation): bool
```php

Establece la orientación de la imagen.

## Parámetros

`orientation`  
Una de las [constantes de orientación](#imagick.constants.orientation)

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`Imagick::setImageOrientation`

```
      
<?php
//Doesn't appear to do anything
function setImageOrientation($imagePath, $orientationType) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->setImageOrientation($orientationType);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
