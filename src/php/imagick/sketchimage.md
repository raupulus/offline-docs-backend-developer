---
title: Imagick::sketchImage
description: Simula el bosquejo de un lapiz
source_url: https://www.php.net/manual/es/imagick.sketchimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/sketchimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35800
---

Imagick::sketchImage

Simula el bosquejo de un lapiz

## Descripción

```php
public Imagick::sketchImage(float $radius, float $sigma, float $angle): bool
```php

Simula el bosquejo de un lapiz. Se convoluciona la imagen con un operador gaussiano del radio y la desviación estándar (sigma) dados. Para obtener resultados razonables, el radio debería ser mayor que sigma. Use un radio de 0 y Imagick::sketchImage() seleccionará un radio apropiado automáticamente. El ángulo da el ángulo del movimiento borroso. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.2.9 o superior.

## Parámetros

`radius`  
El radio gaussiano, en píxeles, sin contar el píxel central.

`sigma`  
La desviación estándar gaussiana, en píxeles.

`angle`  
Aplica el efecto a lo largo de este ángulo.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`Imagick::sketchImage`

```
      
<?php
function sketchImage($imagePath, $radius, $sigma, $angle) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->sketchimage($radius, $sigma, $angle);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
