---
title: Imagick::polaroidImage
description: Simula una fotografía Polaroid
source_url: https://www.php.net/manual/es/imagick.polaroidimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/polaroidimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34700
---

Imagick::polaroidImage

Simula una fotografía Polaroid

## Descripción

```php
public Imagick::polaroidImage(ImagickDraw $properties, float $angle): bool
```php

Simula una fotografía Polaroid. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.2 o superior.

## Parámetros

`properties`  
Las propiedades de polaroid

`angle`  
El ángulo de polaroid

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Un ejemplo de `Imagick::polaroidImage`

Un ejemplo usando Imagick::polaroidImage()

```
<?php
/* Crear el objeto */
$imagen = new Imagick('fuente.png');

/* Establecer la opacidad */
$imagen->polaroidImage(new ImagickDraw(), 25);

/* Imprimir la imagen */
header('Content-type: image/png');
echo $imagen;

?>

    
```php
