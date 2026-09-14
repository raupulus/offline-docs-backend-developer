---
title: Imagick::haldClutImage
description: Reemplaza los colores de la imagen
source_url: https://www.php.net/manual/es/imagick.haldclutimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/haldclutimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 18dc6d0d4
order: 34300
---

Imagick::haldClutImage

Reemplaza los colores de la imagen

## Descripción

```php
public Imagick::haldClutImage(Imagick $clut, [int $channel]): bool
```php

Reemplaza los colores de la imagen usando una paleta Hald. Las imágenes Hald se pueden crear usando un codificador de color HALD.

## Parámetros

`clut`  
Objeto Imagick que contiene la paleta Hald.

`channel`  
Proporciona una constante de canal válida para su modo de canal. Para aplicarlo a más de un canal, combínense las [constantes de canales](#imagick.constants.channel) utilizando un operador a nivel de bits. Por defecto, vale `Imagick::CHANNEL_DEFAULT`. Consúltese la lista de [constantes de canales](#imagick.constants.channel)

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

`Imagick::haldClutImage`

```
      
<?php
function haldClutImage($imagePath) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagickPalette = new \Imagick(realpath("images/hald/hald_8.png"));
    $imagickPalette->sepiatoneImage(55);
    $imagick->haldClutImage($imagickPalette);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
