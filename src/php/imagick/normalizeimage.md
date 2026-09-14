---
title: Imagick::normalizeImage
description: Mejora el contraste de una imagen a color
source_url: https://www.php.net/manual/es/imagick.normalizeimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/normalizeimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34590
---

Imagick::normalizeImage

Mejora el contraste de una imagen a color

## Descripción

```php
public Imagick::normalizeImage([int $channel]): bool
```php

Mejora el contraste de una imagen a color ajustando los colores de los píxeles para abarcar el rango completo de colores disponibles.

## Parámetros

`channel`  
Proporcione cualquier constante de canal que sea válida para su modo de canal. Para aplicar más de un canal, combine las constantes channeltype usando operadores a nivel de bits. Consulte esta lista de [constantes de canal](#imagick.constants.channel).

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`Imagick::normalizeImage`

```
      
<?php
function normalizeImage($imagePath, $channel) {
    $imagick = new \Imagick(realpath($imagePath));
    $original = clone $imagick;
    $original->cropimage($original->getImageWidth() / 2, $original->getImageHeight(), 0, 0);
    $imagick->normalizeImage($channel);
    $imagick->compositeimage($original, \Imagick::COMPOSITE_ATOP, 0, 0);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
