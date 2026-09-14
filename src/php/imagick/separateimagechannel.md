---
title: Imagick::separateImageChannel
description: Separa un canal de la imagen
source_url: https://www.php.net/manual/es/imagick.separateimagechannel.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/separateimagechannel.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35040
---

Imagick::separateImageChannel

Separa un canal de la imagen

## Descripción

```php
public Imagick::separateImageChannel(int $channel): bool
```php

Separa un canal de la imagen y devuelve una imagen en escala de grises. Un canal es un componente de color en particular de cada píxel de la imagen.

## Parámetros

`channel`  
Qué 'canal' devolver. Para espacios de color distintos del RGB, aún se pueden utilizar las constantes CHANNEL_RED, CHANNEL_GREEN, CHANNEL_BLUE para indicar el primer, segundo y tercer canal.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

`Imagick::separateImageChannel`

```
      
<?php
function separateImageChannel($imagePath, $channel) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->separateimagechannel($channel);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

separateImageChannel($imagePath, \Imagick::CHANNEL_GREEN);

?>

      
```php
