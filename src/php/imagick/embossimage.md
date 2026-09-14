---
title: Imagick::embossImage
description: Devuelve una imagen en escala de grises con un efecto tridimensional
source_url: https://www.php.net/manual/es/imagick.embossimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/embossimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 33170
---

Imagick::embossImage

Devuelve una imagen en escala de grises con un efecto tridimensional

## Descripción

```php
public Imagick::embossImage(float $radius, float $sigma): bool
```php

Devuelve una imagen en escala de grises con un efecto tridimensional. Se convoluciona la imagen con un operador gaussiano del radio y desviación estándar (sigma) dados. Para obtener resultados razonables, el radio debería ser mayor que sigma. Use un radio de 0 y se elegirá un radio apropiado automáticamente.

## Parámetros

`radius`  
El radio de el efecto

`sigma`  
El valor sigma del efecto

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

`Imagick::embossImage`

```
      
<?php
function embossImage($imagePath, $radius, $sigma) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->embossImage($radius, $sigma);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
