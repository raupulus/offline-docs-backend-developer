---
title: imagecolorclosesthwb
description: Obtiene el índice de la color especificada con su tono, blanco y negro
source_url: https://www.php.net/manual/es/function.imagecolorclosesthwb.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagecolorclosesthwb.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 9960a09a5
order: 31580
---

imagecolorclosesthwb

Obtiene el índice de la color especificada con su tono, blanco y negro

## Descripción

```php
imagecolorclosesthwb(GdImage $image, int $red, int $green, int $blue): int
```php

Obtiene el índice de la color especificada con su tono, blanco y negro.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`red`  
Valor del componente rojo.

`green`  
Valor del componente verde.

`blue`  
Valor del componente azul.

## Valores devueltos

Devuelve un integer que representa el índice de la color.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Ejemplo con `imagecolorclosesthwb`

```
<?php
$im = imagecreatefromgif('php.gif');

echo 'HWB : ' . imagecolorclosesthwb($im, 116, 115, 152);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    HWB: 33

## Véase también

imagecolorclosest
