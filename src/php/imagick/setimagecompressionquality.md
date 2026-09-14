---
title: Imagick::setImageCompressionQuality
description: Establece la calidad de compresión de una imagen
source_url: https://www.php.net/manual/es/imagick.setimagecompressionquality.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/setimagecompressionquality.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35300
---

Imagick::setImageCompressionQuality

Establece la calidad de compresión de una imagen

## Descripción

```php
public Imagick::setImageCompressionQuality(int $quality): bool
```php

Establece la calidad de compresión de una imagen.

## Parámetros

`quality`  
La calidad de compresión de la imagen como un integer

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

`Imagick::setImageCompressionQuality`

```
      
<?php
function setImageCompressionQuality($imagePath, $quality) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->setImageCompressionQuality($quality);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
