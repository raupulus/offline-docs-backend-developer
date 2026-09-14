---
title: imageinterlace
description: Activa o desactiva el entrelazado
source_url: https://www.php.net/manual/es/function.imageinterlace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imageinterlace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: c6fb604f3
order: 32160
---

imageinterlace

Activa o desactiva el entrelazado

## Descripción

```php
imageinterlace(GdImage $image, [bool $enable]): bool
```php

`imageinterlace` activa o desactiva el bit de entrelazado.

Si el entrelazado es 1 y la imagen es JPEG, la imagen creada será un JPEG progresivo.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`enable`  
Si `true`, la imagen será entrelazada, si `false` el bit de entrelazado es desactivado. Pasar `null` hará que el comportamiento de entrelazado no sea cambiado.

## Valores devueltos

Retorna `true` si el entrelazado está activado para la imagen, `false` en caso contrario.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.5 | `imageinterlace` ahora retorna un `bool`; anteriormente se retornaba un `int` (no-cero para imágenes entrelazadas, cero en caso contrario). |
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |
| 8.0.0 | `enable` ahora espera un `bool`; anteriormente esperaba un `int`. |

## Ejemplos

Activación del entrelazado utilizando la función `imageinterlace`

```
<?php
// Creación de una imagen
$im = imagecreatefromgif('php.gif');

// Activación del entrelazado
imageinterlace($im, true);

// Guardado de la imagen
imagegif($im, './php_interlaced.gif');
?>

    
```php
