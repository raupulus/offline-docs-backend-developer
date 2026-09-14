---
title: Imagick::thresholdImage
description: Cambia el valor de píexeles individuales basdos en un umbral
source_url: https://www.php.net/manual/es/imagick.thresholdimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/thresholdimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35930
---

Imagick::thresholdImage

Cambia el valor de píexeles individuales basdos en un umbral

## Descripción

```php
public Imagick::thresholdImage(float $threshold, [int $channel]): bool
```php

Cambia el valor de píxeles individuales basados en la inatensidad de cada píxel comparado con el umbral. El resultado es una imagen de alto contraste de dos colores.

## Parámetros

`threshold`  

`channel`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`Imagick::thresholdImage`

```
      
<?php
function thresholdimage($imagePath, $threshold, $channel) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->thresholdimage($threshold * \Imagick::getQuantum(), $channel);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
