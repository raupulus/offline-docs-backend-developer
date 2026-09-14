---
title: Imagick::fxImage
description: Evalúa una expresión por cada píxel de la imagen
source_url: https://www.php.net/manual/es/imagick.fximage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/fximage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 33320
---

Imagick::fxImage

Evalúa una expresión por cada píxel de la imagen

## Descripción

```php
public Imagick::fxImage(string $expression, [int $channel]): Imagick
```php

Evalúa una expresión por cada píxel de la imagen. Consulte [El Operador de Imagen de Efectos Especiales Fx](http://www.imagemagick.org/script/fx.php) para más información.

## Parámetros

`expression`  
La expresión.

`channel`  
Proporcione cualquier constante de canal que sea válida para su modo de canal. Para aplicar más de un canal, combine las constantes channeltype usando operadores a nivel de bits. Consulte esta lista de [constantes de canal](#imagick.constants.channel).

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

`Imagick::fxImage`

```
      
<?php
function fxImage() {
    $imagick = new \Imagick();
    $imagick->newPseudoImage(200, 200, "xc:white");

    $fx = 'xx=i-w/2; yy=j-h/2; rr=hypot(xx,yy); (.5-rr/140)*1.2+.5';
    $fxImage = $imagick->fxImage($fx);

    header("Content-Type: image/png");
    $fxImage->setimageformat('png');
    echo $fxImage->getImageBlob();
}

?>

      
```php
