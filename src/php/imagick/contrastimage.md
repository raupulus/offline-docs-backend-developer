---
title: Imagick::contrastImage
description: Cambia el contraste de una imagen
source_url: https://www.php.net/manual/es/imagick.contrastimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/contrastimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 32970
---

Imagick::contrastImage

Cambia el contraste de una imagen

## Descripción

```php
public Imagick::contrastImage(bool $sharpen): bool
```php

Mejora la diferencias de intensidad entre elementos claros y oscuros de la imagen. Establezca la agudización a un valor que no sea 0 para aumentar el contraste de la imagen, de otro modo el contraste se reduce.

## Parámetros

`sharpen`  
El valor de la agudización

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

`Imagick::contrastImage`

```
      
<?php
function contrastImage($imagePath, $contrastType) {
    $imagick = new \Imagick(realpath($imagePath));
    if ($contrastType != 2) {
        $imagick->contrastImage($contrastType);
    }

    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
