---
title: Gmagick::setimagecolorspace
description: Define el espacio de colores de la imagen
source_url: https://www.php.net/manual/es/gmagick.setimagecolorspace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/setimagecolorspace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 27550
---

Gmagick::setimagecolorspace

Define el espacio de colores de la imagen

## Descripción

```php
public Gmagick::setimagecolorspace(int $colorspace): Gmagick
```php

Define el espacio de colores de la imagen.

## Parámetros

`colorspace`  
Una de las constantes de [espacio de colores de la imagen](#gmagick.constants.colorspace) (`Gmagick::COLORSPACE_*`).

## Valores devueltos

El objeto `Gmagick`.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
