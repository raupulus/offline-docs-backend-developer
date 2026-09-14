---
title: Imagick::sepiaToneImage
description: Pone una imagen en tono sepia
source_url: https://www.php.net/manual/es/imagick.sepiatoneimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/sepiatoneimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35050
---

Imagick::sepiaToneImage

Pone una imagen en tono sepia

## Descripción

```php
public Imagick::sepiaToneImage(float $threshold): bool
```php

Aplica un efecto especial a la imagen, similar al efecto logrado en un cuarto oscuro fotográfico aplicando un tono sepia. El umbral tiene un rango desde 0 hasta el de QuantumRange y es una medida de la extensión del tono sepia. Un umbral de 80 es un buen punto de partida para un tono razonable.

## Parámetros

`threshold`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

`Imagick::sepiaToneImage`

```
      
<?php
function sepiaToneImage($imagePath, $sepia) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->sepiaToneImage($sepia);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
