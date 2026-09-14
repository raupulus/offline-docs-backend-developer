---
title: Imagick::solarizeImage
description: Aplica un efecto de solarización a la imagen
source_url: https://www.php.net/manual/es/imagick.solarizeimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/solarizeimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35820
---

Imagick::solarizeImage

Aplica un efecto de solarización a la imagen

## Descripción

```php
public Imagick::solarizeImage(int $threshold): bool
```php

Aplica un efecto especial a la imagen, similar al efecto conseguido en un cuarto oscuro fotográfico exponiendo selectivamente áreas del papel sensible fotográfico a la luz. Los rangos de umbral van desde 0 al de QuantumRange y es una medida de la extensión de la solarización.

## Parámetros

`threshold`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`Imagick::solarizeImage`

```
      
<?php
function solarizeImage($imagePath, $solarizeThreshold) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->solarizeImage($solarizeThreshold * \Imagick::getQuantum());
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
