---
title: Imagick::negateImage
description: Invierte los colores en la imagen de referencia
source_url: https://www.php.net/manual/es/imagick.negateimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/negateimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34550
---

Imagick::negateImage

Invierte los colores en la imagen de referencia

## Descripción

```php
public Imagick::negateImage(bool $gray, [int $channel]): bool
```php

Invierte los colores en la imagen de referencia. La opción de escala de grises significa que sólo los valores de la escala de grises dentro de la imagen se inverten.

## Parámetros

`gray`  
Si sólo se invierten los píxeles de la escala de grises dentro de la imagen.

`channel`  
Proporcione cualquier constante de canal que sea válida para su modo de canal. Para aplicar más de un canal, combine las constantes channeltype usando operadores a nivel de bits. Consulte esta lista de [constantes de canal](#imagick.constants.channel).

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

`Imagick::negateImage`

```
      
<?php
function negateImage($imagePath, $grayOnly, $channel) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->negateImage($grayOnly, $channel);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
