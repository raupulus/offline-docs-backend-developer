---
title: Imagick::addNoiseImage
description: Añade ruido aleatorio a la imagen
source_url: https://www.php.net/manual/es/imagick.addnoiseimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/addnoiseimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: 0ffb9c9fc
order: 32650
---

Imagick::addNoiseImage

Añade ruido aleatorio a la imagen

## Descripción

```php
public Imagick::addNoiseImage(int $noise_type, [int $channel]): bool
```php

Añade ruido aleatorio a la imagen.

## Parámetros

`noise_type`  
El tipo de ruido. Consulte esta lista de [constantes de ruido](#imagick.constants.noise).

`channel`  
Proporciona una constante de canal válida para su modo de canal. Para aplicarlo a más de un canal, combínense las [constantes de canales](#imagick.constants.channel) utilizando un operador a nivel de bits. Por defecto, vale `Imagick::CHANNEL_DEFAULT`. Consúltese la lista de [constantes de canales](#imagick.constants.channel)

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`Imagick::addNoiseImage`

```
<?php
function addNoiseImage($noiseType, $imagePath, $channel) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->addNoiseImage($noiseType, $channel);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

    
```php
