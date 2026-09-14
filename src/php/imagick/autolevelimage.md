---
title: Imagick::autoLevelImage
description: Ajusta el nivel de un canal de una imagen particular
source_url: https://www.php.net/manual/es/imagick.autolevelimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/autolevelimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 1ef9c7a76
order: 32700
---

Imagick::autoLevelImage

Ajusta el nivel de un canal de una imagen particular

## Descripción

```php
public Imagick::autoLevelImage([int $channel]): bool
```php

Ajusta el nivel de un canal de una imagen particular escalando los valores mínimos y máximos al rango cuántico completo.

## Parámetros

`channel`  
Qué canal debe ser utilizado para el auto-nivelado.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`Imagick::autoLevelImage`

```
      
<?php
function autoLevelImage($imagePath) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->autoLevelImage();
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
