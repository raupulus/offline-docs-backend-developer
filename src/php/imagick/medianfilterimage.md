---
title: Imagick::medianFilterImage
description: Aplica un filtro digital
source_url: https://www.php.net/manual/es/imagick.medianfilterimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/medianfilterimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34460
---

Imagick::medianFilterImage

Aplica un filtro digital

> [!WARNING]
> Esta función está *DEPRECADA* a partir de Imagick 3.4.4. Depender de esta funcionalidad está fuertemente desaconsejado.

## Descripción

```php
public Imagick::medianFilterImage(float $radius): bool
```php

Aplica un filtro digital que mejora la calidad de una imagen con ruido. Cada píxel es reemplazado por la media en un conjunto de píxeles inmediatos como está definido por el radio.

## Parámetros

`radius`  
El radio de la zona inmediata de los píxeles.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

`Imagick::medianFilterImage`

```
      
<?php
function medianFilterImage($radius, $imagePath) {
    $imagick = new \Imagick(realpath($imagePath));
    @$imagick->medianFilterImage($radius);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
