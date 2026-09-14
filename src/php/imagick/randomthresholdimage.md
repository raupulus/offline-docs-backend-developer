---
title: Imagick::randomThresholdImage
description: Crea una imagen de alto contraste y dos colores
source_url: https://www.php.net/manual/es/imagick.randomthresholdimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/randomthresholdimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34820
---

Imagick::randomThresholdImage

Crea una imagen de alto contraste y dos colores

## Descripción

```php
public Imagick::randomThresholdImage(float $low, float $high, [int $channel]): bool
```php

Cambia el valor de píxeles individuales basados en la instensidad de cada píxel comparado con el umbral. El resultado es una imagen de alto contraste y dos colores. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.2.9 o superior.

## Parámetros

`low`  
El punto bajo

`high`  
El punto alto

`channel`  
Proporcione cualquier constante de canal que sea válida para su modo de canal. Para aplicar más de un canal, combine las constantes channeltype usando operadores a nivel de bits. Consulte esta lista de [constantes de canal](#imagick.constants.channel).

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`Imagick::randomThresholdImage`

```
      
<?php
function randomThresholdimage($imagePath, $lowThreshold, $highThreshold, $channel) {
    $imagick = new \Imagick(realpath($imagePath));

    $imagick->randomThresholdimage(
        $lowThreshold * \Imagick::getQuantum(),
        $highThreshold * \Imagick::getQuantum(),
        $channel
    );
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
