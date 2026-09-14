---
title: Imagick::selectiveBlurImage
description: Desenfoca selectivamente una imagen dentro de un umbral de contraste
source_url: https://www.php.net/manual/es/imagick.selectiveblurimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/selectiveblurimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 1ef9c7a76
order: 35030
---

Imagick::selectiveBlurImage

Desenfoca selectivamente una imagen dentro de un umbral de contraste

## Descripción

```php
public Imagick::selectiveBlurImage(float $radius, float $sigma, float $threshold, [int $channel]): bool
```php

Desenfoca selectivamente una imagen dentro de un umbral de contraste. Es similar al filtro de desenfoque que acentúa todo con un contraste superior a un cierto umbral.

## Parámetros

`radius`  

`sigma`  

`threshold`  

`channel`  
Proporciona una constante de canal válida para su modo de canal. Para aplicarlo a más de un canal, combínense las [constantes de canales](#imagick.constants.channel) utilizando un operador a nivel de bits. Por defecto, vale `Imagick::CHANNEL_DEFAULT`. Consúltese la lista de [constantes de canales](#imagick.constants.channel)

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`Imagick::selectiveBlurImage`

```
      
<?php
function selectiveBlurImage($imagePath, $radius, $sigma, $threshold, $channel) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->selectiveBlurImage($radius, $sigma, $threshold, $channel);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
