---
title: Imagick::spreadImage
description: Despalza aleatoriamente cada píxel en un bloque
source_url: https://www.php.net/manual/es/imagick.spreadimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/spreadimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35850
---

Imagick::spreadImage

Despalza aleatoriamente cada píxel en un bloque

## Descripción

```php
public Imagick::spreadImage(float $radius): bool
```php

Método de efecto especial que desplaza aleatoriamente cada píxel en un bloque definido por el parámetro radius (radio).

## Parámetros

`radius`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

`Imagick::spreadImage`

```
      
<?php
function spreadImage($imagePath, $radius) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->spreadImage($radius);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
