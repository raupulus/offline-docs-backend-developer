---
title: Gmagick::resizeimage
description: Redimensiona una imagen
source_url: https://www.php.net/manual/es/gmagick.resizeimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/resizeimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 27440
---

Gmagick::resizeimage

Redimensiona una imagen

## Descripción

```php
public Gmagick::resizeimage(int $width, int $height, int $filter, float $blur, [bool $fit]): Gmagick
```php

Redimensiona una imagen a las dimensiones deseadas, con un filtro.

## Parámetros

`width`  
El número de columnas en la imagen redimensionada.

`height`  
El número de líneas en la imagen redimensionada.

`filter`  
El filtro de la imagen a utilizar.

`blur`  
El factor de desenfoque, donde los valores superiores a 1 corresponden a completamente desenfocado, y los valores inferiores a 1, lo contrario.

## Valores devueltos

El objeto `Gmagick`.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
