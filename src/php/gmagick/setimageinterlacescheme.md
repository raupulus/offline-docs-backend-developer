---
title: Gmagick::setimageinterlacescheme
description: Define el esquema de entrelazado de la imagen
source_url: https://www.php.net/manual/es/gmagick.setimageinterlacescheme.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/setimageinterlacescheme.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 27650
---

Gmagick::setimageinterlacescheme

Define el esquema de entrelazado de la imagen

## Descripción

```php
public Gmagick::setimageinterlacescheme(int $interlace): Gmagick
```php

Define el esquema de entrelazado de la imagen.

## Parámetros

`interlace`  
Una de las constantes de los [esquemas de entrelazado de la imagen](#gmagick.constants.interlace) (`Gmagick::INTERLACE_*`).

## Valores devueltos

El objeto `Gmagick`.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
