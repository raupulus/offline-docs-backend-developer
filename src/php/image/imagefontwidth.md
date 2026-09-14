---
title: imagefontwidth
description: Devuelve el ancho de la fuente
source_url: https://www.php.net/manual/es/function.imagefontwidth.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagefontwidth.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: a7e5e563d
order: 32050
---

imagefontwidth

Devuelve el ancho de la fuente

## Descripción

```php
imagefontwidth(GdFont $font): int
```php

Devuelve el ancho de la fuente `font` en píxeles.

## Parámetros

`font`  
Puede ser 1, 2, 3, 4, 5 para las fuentes internas de codificación Latin2 (donde los números más grandes corresponden a fuentes anchas) o una instancia de `GdFont` retornado por `imageloadfont`.

## Valores devueltos

Devuelve el ancho de la fuente.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `font` ahora acepta una instancia de `GdFont` y un `int`; anteriormente solo un `int` era aceptado. |

## Ejemplos

Ejemplo con `imagefontwidth` y las fuentes internas

```
<?php
echo 'Ancho de la fuente : ' . imagefontwidth(4);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Ancho de la fuente : 8

Ejemplo con `imagefontwidth` y `imageloadfont`

```
<?php
// Carga de una fuente .gdf
$font = imageloadfont('anonymous.gdf');

echo 'Ancho de la fuente : ' . imagefontwidth($font);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Ancho de la fuente : 23

## Véase también

imagefontheight

imageloadfont
