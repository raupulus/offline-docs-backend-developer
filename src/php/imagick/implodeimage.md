---
title: Imagick::implodeImage
description: Crea una nueva imagen como una copia
source_url: https://www.php.net/manual/es/imagick.implodeimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/implodeimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34350
---

Imagick::implodeImage

Crea una nueva imagen como una copia

## Descripción

```php
public Imagick::implodeImage(float $radius): bool
```php

Crea una nueva imagen que es una copia de una existente con los píxeles de la imagen "implosionados" por el porcentaje especificado.

## Parámetros

`radius`  
El radio de la implosión

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

`Imagick::implodeImage`

```
      
<?php
function implodeImage($imagePath) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->implodeImage(0.0001);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();

}

?>

      
```php
