---
title: Gmagick::blurimage
description: Añade un filtro de borrosidad a la imagen
source_url: https://www.php.net/manual/es/gmagick.blurimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/blurimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_revision: 35752f072
order: 26480
---

Gmagick::blurimage

Añade un filtro de borrosidad a la imagen

## Descripción

```php
public Gmagick::blurimage(float $radius, float $sigma, [int $channel]): Gmagick
```php

Añade un filtro de borrosidad a la imagen.

## Parámetros

`radius`  
Radio de borrosidad

`sigma`  
Desviación estándar

## Valores devueltos

El objeto `Gmagick` borroso

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
