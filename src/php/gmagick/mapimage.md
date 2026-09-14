---
title: Gmagick::mapimage
description: Sustituye los colores de una imagen por los colores más cercanos de una
  imagen de referencia
source_url: https://www.php.net/manual/es/gmagick.mapimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/mapimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 27180
---

Gmagick::mapimage

Sustituye los colores de una imagen por los colores más cercanos de una imagen de referencia

## Descripción

```php
public Gmagick::mapimage(gmagick $gmagick, bool $dither): Gmagick
```php

Sustituye los colores de una imagen por los colores más cercanos de una imagen de referencia.

## Parámetros

`gmagick`  
La imagen de referencia.

`dither`  
Entero mayor que 0 para difuminar la imagen mapeada.

## Valores devueltos

El objeto `Gmagick`.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
