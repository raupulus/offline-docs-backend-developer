---
title: Imagick::statisticImage
description: Modifica una imagen utilizando una función estadística
source_url: https://www.php.net/manual/es/imagick.statisticimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/statisticimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 85278ca11
order: 35860
---

Imagick::statisticImage

Modifica una imagen utilizando una función estadística

## Descripción

```php
public Imagick::statisticImage(int $type, int $width, int $height, [int $channel]): bool
```php

Cada píxel es reemplazado por la estadística correspondiente del vecindario de la anchura y altura especificadas.

## Parámetros

`type`  

`width`  

`height`  

`channel`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`Imagick::statisticImage`

```
      
<?php
function statisticImage($imagePath, $statisticType, $width, $height, $channel) {
    $imagick = new \Imagick(realpath($imagePath));

    $imagick->statisticImage(
        $statisticType,
        $width,
        $height,
        $channel
    );

    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

statisticImage($imagePath, \Imagick::STATISTIC_MEDIAN, 5, 5, \Imagick::CHANNEL_DEFAULT);

?>

      
```php
