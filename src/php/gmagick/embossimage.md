---
title: Gmagick::embossimage
description: Devuelve una imagen en escala de grises con un efecto tridimensional
source_url: https://www.php.net/manual/es/gmagick.embossimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/embossimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_revision: 35752f072
order: 26650
---

Gmagick::embossimage

Devuelve una imagen en escala de grises con un efecto tridimensional

## Descripción

```php
public Gmagick::embossimage(float $radius, float $sigma): Gmagick
```php

Devuelve una imagen en escala de grises con un efecto tridimensional. Se convoluciona la imagen con un operador gaussiano del radio y desviación estándar (sigma) dados. Para obtener resultados razonables, el radio debería ser mayor que sigma. Use un radio de 0 y se elegirá un radio apropiado automáticamente.

## Parámetros

`radius`  
El radio del efecto.

`sigma`  
El valor sigma del efecto.

## Valores devueltos

El objeto `Gmagick` "repujado".

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
