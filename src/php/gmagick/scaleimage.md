---
title: Gmagick::scaleimage
description: Redimensiona una imagen
source_url: https://www.php.net/manual/es/gmagick.scaleimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/scaleimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 27470
---

Gmagick::scaleimage

Redimensiona una imagen

## Descripción

```php
public Gmagick::scaleimage(int $width, int $height, [bool $fit]): Gmagick
```php

Redimensiona una imagen a las dimensiones proporcionadas. Los otros parámetros serán calculados si 0 es pasado como argumento.

## Parámetros

`width`  
El número de columnas en la imagen redimensionada.

`height`  
El número de líneas en la imagen redimensionada.

## Valores devueltos

El objeto `Gmagick`.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
