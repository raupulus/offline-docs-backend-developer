---
title: Imagick::gaussianBlurImage
description: Hace borrosa una imagen
source_url: https://www.php.net/manual/es/imagick.gaussianblurimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/gaussianblurimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 33340
---

Imagick::gaussianBlurImage

Hace borrosa una imagen

## Descripción

```php
public Imagick::gaussianBlurImage(float $radius, float $sigma, [int $channel]): bool
```php

Hace borrosa una imagen. Se convoluciona la imagen con un operador gaussiano del radio y la desviación estándar (sigma) dados. Para obtener resultados razonables, el radio debería ser mayor que sigma. Use un radio de 0 y se seleccionará un radio adecuado automáticamente.

## Parámetros

`radius`  
El radio gaussiano, en píxeles, sin contar el píxel central.

`sigma`  
La desviación estándar gaussiana, en píxeles.

`channel`  
Proporcione cualquier constante de canal que sea válida para su modo de canal. Para aplicar más de un canal, combine las constantes channeltype usando operadores a nivel de bits. Consulte esta lista de [constantes de canal](#imagick.constants.channel).

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

`Imagick::gaussianBlurImage`

```
      
<?php
function gaussianBlurImage($imagePath, $radius, $sigma, $channel) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->gaussianBlurImage($radius, $sigma, $channel);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
