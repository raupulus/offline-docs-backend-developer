---
title: Imagick::adaptiveThresholdImage
description: Selecciona un umbral para cada píxel basado en un rango de intensidad
source_url: https://www.php.net/manual/es/imagick.adaptivethresholdimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/adaptivethresholdimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: 0ffb9c9fc
order: 32630
---

Imagick::adaptiveThresholdImage

Selecciona un umbral para cada píxel basado en un rango de intensidad

## Descripción

```php
public Imagick::adaptiveThresholdImage(int $width, int $height, int $offset): bool
```php

Selecciona un umbral individual para cada píxel basado en un rango de valores de intensidad en su zona local. Esto permite establecer el umbral de una imagen cuyo histograma de intensidad global no contiene picos distintivos.

## Parámetros

`width`  
Ancho de la zona local.

`height`  
Alto de la zona local.

`offset`  
El índice medio

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`Imagick::adaptiveThresholdImage`

```
<?php
function adaptiveThresholdImage($imagePath, $width, $height, $adaptiveOffset) {
    $imagick = new \Imagick(realpath($imagePath));
    $adaptiveOffsetQuantum = intval($adaptiveOffset * \Imagick::getQuantum());
    $imagick->adaptiveThresholdImage($width, $height, $adaptiveOffsetQuantum);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

    
```php
