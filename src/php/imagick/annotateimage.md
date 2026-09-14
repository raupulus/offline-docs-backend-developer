---
title: Imagick::annotateImage
description: Anota una imagen con texto
source_url: https://www.php.net/manual/es/imagick.annotateimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/annotateimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 32680
---

Imagick::annotateImage

Anota una imagen con texto

## Descripción

```php
public Imagick::annotateImage(ImagickDraw $draw_settings, float $x, float $y, float $angle, string $text): bool
```php

Anota una imagen con texto.

## Parámetros

`draw_settings`  
El objeto ImagickDraw que contiene la configuración para el dibujo de texto

`x`  
El índice horizontal en píxeles a la izquierda del texto

`y`  
El índice vertical en píxeles de la línea base del texto

`angle`  
El ángulo en el que se escribe el texto

`text`  
La cadena a dibujar

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Usar `Imagick::annotateImage`:

Anotar texto en una imagen vacía

```
<?php
/* Crear algunos objetos */
$imagen = new Imagick();
$dibujo = new ImagickDraw();
$píxel = new ImagickPixel( 'gray' );

/* Nueva imagen */
$imagen->newImage(800, 75, $píxel);

/* Texto negro */
$dibujo->setColor('black');

/* Propiedades de la fuente */
$dibujo->setFont('Bookman-DemiItalic');
$dibujo->setFontSize( 30 );

/* Crear texto */
$imagen->annotateImage($dibujo, 10, 45, 0, 'The quick brown fox jumps over the lazy dog');

/* Dar a la imagen un formato */
$imagen->setImageFormat('png');

/* Imprimir la imagen con cabeceras */
header('Content-type: image/png');
echo $imagen;

?>

    
```php

## Véase también

`ImagickDraw::annotation`, `ImagickDraw::setFont`
