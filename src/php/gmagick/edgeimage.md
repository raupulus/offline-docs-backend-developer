---
title: Gmagick::edgeimage
description: Mejora los bordes dentro de una imagen
source_url: https://www.php.net/manual/es/gmagick.edgeimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/edgeimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_revision: 35752f072
order: 26640
---

Gmagick::edgeimage

Mejora los bordes dentro de una imagen

## Descripción

```php
public Gmagick::edgeimage(float $radius): Gmagick
```php

Mejora los bordes dentro de una imagen con un filtro de convolución del radio dado. Use un radio de 0 y éste será seleccionado automáticamente.

## Parámetros

`radius`  
El radio de la operación.

## Valores devueltos

El objeto `Gmagick` con los bordes mejorados.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
