---
title: Imagick::swirlImage
description: Arremolina los píxeles desde el centro de la imagen
source_url: https://www.php.net/manual/es/imagick.swirlimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/swirlimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35910
---

Imagick::swirlImage

Arremolina los píxeles desde el centro de la imagen

## Descripción

```php
Imagick::swirlImage(float $degrees): bool
```php

Arremolina los píxeles desde el centro de la imagen, donde los grados indican el alcance del arco a través del cuál cada píxel es movido. Se puede obtener un efecto más dramático moviendo los grados desde 1 a 360.

## Parámetros

`degrees`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

`Imagick::swirlImage`

```
      
<?php
function swirlImage($imagePath, $swirl) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->swirlImage($swirl);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
