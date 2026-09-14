---
title: Imagick::convolveImage
description: Aplica una semilla de convolución a medida a la imagen
source_url: https://www.php.net/manual/es/imagick.convolveimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/convolveimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 32990
---

Imagick::convolveImage

Aplica una semilla de convolución a medida a la imagen

## Descripción

```php
public Imagick::convolveImage(array $kernel, [int $channel]): bool
```php

Aplica una semilla de convolución a medida a la imagen.

## Parámetros

`kernel`  
La semilla de convolución

`channel`  
Proporcione cualquier constante de canal que sea válida para su modo de canal. Para aplicar más de un canal, combine las constantes channeltype usando operadores a nivel de bits. Consulte esta lista de [constantes de canal](#imagick.constants.channel).

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

`Imagick::convolveImage`

```
      
<?php
function convolveImage($imagePath, $bias, $kernelMatrix) {
    $imagick = new \Imagick(realpath($imagePath));
    //$edgeFindingKernel = [-1, -1, -1, -1, 8, -1, -1, -1, -1,];
    $imagick->setImageBias($bias * \Imagick::getQuantum());
    $imagick->convolveImage($kernelMatrix);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
