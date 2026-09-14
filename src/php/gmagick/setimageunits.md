---
title: Gmagick::setimageunits
description: Define las unidades a utilizar para la resolución de la imagen
source_url: https://www.php.net/manual/es/gmagick.setimageunits.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/setimageunits.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 27730
---

Gmagick::setimageunits

Define las unidades a utilizar para la resolución de la imagen

## Descripción

```php
public Gmagick::setimageunits(int $resolution): Gmagick
```php

Define las unidades a utilizar para la resolución de la imagen.

## Parámetros

`resolution`  
Una de las constantes de [resolución](#gmagick.constants.resolution) (`Gmagick::RESOLUTION_*`).

## Valores devueltos

El objeto `Gmagick`.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
