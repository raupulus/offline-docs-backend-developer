---
title: Gmagick::reducenoiseimage
description: Suaviza los contornos de la imagen
source_url: https://www.php.net/manual/es/gmagick.reducenoiseimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/reducenoiseimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 27400
---

Gmagick::reducenoiseimage

Suaviza los contornos de la imagen

## Descripción

```php
public Gmagick::reducenoiseimage(float $radius): Gmagick
```php

Suaviza los contornos de la imagen manteniendo la información de las esquinas. El algoritmo funciona reemplazando cada píxel con su vecino más cercano en valor. Un vecino se define por su radio. Utilizar un radio de 0 y el método Gmagick::reducenoiseimage seleccionará un radio apropiado automáticamente.

## Parámetros

`radius`  
El radio del píxel vecino.

## Valores devueltos

El objeto `Gmagick`.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
