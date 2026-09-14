---
title: Imagick::motionBlurImage
description: Simula borrosidad en movimiento
source_url: https://www.php.net/manual/es/imagick.motionblurimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/motionblurimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34540
---

Imagick::motionBlurImage

Simula borrosidad en movimiento

## Descripción

```php
public Imagick::motionBlurImage(float $radius, float $sigma, float $angle, [int $channel]): bool
```php

Simula borrosidad en movimiento. Se convoluciona la imagen con un operador gaussiano del radio y la desviación estándar (sigma) dados. Para obtener resultados razonables, el radio debe ser mayor que sigma. Use un radio de 0 y MotionBlurImage() seleccionará un radio apropiado automáticamente. El ángulo da el ángulo del movimiento borroso.

## Parámetros

`radius`  
El radio gaussiano, en píxeles, sin contar el píxel central.

`sigma`  
La desviación estándar gaussiana, en píxeles.

`angle`  
Aplica el efecto a lo largo de este ángulo.

`channel`  
Proporcione cualquier constante de canal que sea válida para su modo de canal. Para aplicar más de un canal, combine las constantes channeltype usando operadores a nivel de bits. Consulte esta lista de [constantes de canal](#imagick.constants.channel). El argumento channel afecta sólo si Imagick es compilado con la versión 6.4.4 o superior de ImageMagick.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`Imagick::motionBlurImage`

```
      
<?php
function motionBlurImage($imagePath, $radius, $sigma, $angle, $channel) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->motionBlurImage($radius, $sigma, $angle, $channel);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
