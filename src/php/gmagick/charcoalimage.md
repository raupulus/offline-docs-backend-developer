---
title: Gmagick::charcoalimage
description: Simula un dibujo a carboncillo
source_url: https://www.php.net/manual/es/gmagick.charcoalimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/charcoalimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_revision: 35752f072
order: 26500
---

Gmagick::charcoalimage

Simula un dibujo a carboncillo

## Descripción

```php
public Gmagick::charcoalimage(float $radius, float $sigma): Gmagick
```php

Simula un dibujo a carboncillo.

## Parámetros

`radius`  
El radio gaussiano, en píxeles, sin contar el píxel central.

`sigma`  
La desviación estándar gaussiana, en píxeles.

## Valores devueltos

El objeto `Gmagick` con la simulación de carboncillo

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
