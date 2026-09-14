---
title: Imagick::rollImage
description: Compensa una imagen
source_url: https://www.php.net/manual/es/imagick.rollimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/rollimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34960
---

Imagick::rollImage

Compensa una imagen

## Descripción

```php
public Imagick::rollImage(int $x, int $y): bool
```php

Compensa una imagen como está definido por x e y.

## Parámetros

`x`  
El índice X.

`y`  
El índice Y.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`Imagick::rollImage`

```
      
<?php
function rollImage($imagePath, $rollX, $rollY) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->rollimage($rollX, $rollY);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
