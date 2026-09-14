---
title: Imagick::rotationalBlurImage
description: Aplica un desenfoque rotacional a una imagen
source_url: https://www.php.net/manual/es/imagick.rotationalblurimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/rotationalblurimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 1ef9c7a76
order: 34980
---

Imagick::rotationalBlurImage

Aplica un desenfoque rotacional a una imagen

## Descripción

```php
public Imagick::rotationalBlurImage(float $angle, [int $channel]): bool
```php

Aplica un desenfoque rotacional a una imagen.

## Parámetros

`angle`  
El ángulo sobre el cual aplicar el desenfoque.

`channel`  
Proporciona una constante de canal válida para su modo de canal. Para aplicarlo a más de un canal, combínense las [constantes de canales](#imagick.constants.channel) utilizando un operador a nivel de bits. Por defecto, vale `Imagick::CHANNEL_DEFAULT`. Consúltese la lista de [constantes de canales](#imagick.constants.channel)

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`Imagick::rotationalBlurImage`

```
      
<?php
function rotationalBlurImage($imagePath) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->rotationalBlurImage(3);
    $imagick->rotationalBlurImage(5);
    $imagick->rotationalBlurImage(7);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
