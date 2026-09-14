---
title: imagepalettecopy
description: Copia la paleta de una imagen a otra
source_url: https://www.php.net/manual/es/function.imagepalettecopy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagepalettecopy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 9960a09a5
order: 32230
---

imagepalettecopy

Copia la paleta de una imagen a otra

## Descripción

```php
imagepalettecopy(GdImage $dst, GdImage $src): void
```php

`imagepalettecopy` copia la paleta de la imagen `src` a la imagen `dst`.

## Parámetros

`dst`  
El objeto de la imagen de destino.

`src`  
El objeto de la imagen fuente.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `dst` y `src` ahora esperan instancias de `GdImage` ; anteriormente, se esperaban `resource`s. |

## Ejemplos

Ejemplo con `imagepalettecopy`

```
<?php
// Creación de 2 paletas
$palette1 = imagecreate(100, 100);
$palette2 = imagecreate(100, 100);

// Define el fondo en verde
// para la primera
$green = imagecolorallocate($palette1, 0, 255, 0);

// Copia la primera paleta a la segunda
imagepalettecopy($palette2, $palette1);

// Sabiendo que la paleta ahora está copiada, se puede
// usar el color verde asignado a la primera paleta
// sin necesidad de usar de nuevo la función imagecolorallocate()
imagefilledrectangle($palette2, 0, 0, 99, 99, $green);

// Muestra la imagen en el navegador
header('Content-type: image/png');

imagepng($palette2);
?>

    
```php
