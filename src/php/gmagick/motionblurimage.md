---
title: Gmagick::motionblurimage
description: Simula un desenfoque cinético
source_url: https://www.php.net/manual/es/gmagick.motionblurimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/motionblurimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 27220
---

Gmagick::motionblurimage

Simula un desenfoque cinético

## Descripción

```php
public Gmagick::motionblurimage(float $radius, float $sigma, float $angle): Gmagick
```php

Simula un desenfoque cinético. La imagen es procesada con un operador Gaussiano de un radio dado y una desviación estándar (sigma). Para obtener buenos resultados, el radio debe ser mayor que el sigma. Utilice un radio de 0 y el método Gmagick::motionblurimage selecciona el mejor radio automáticamente. El argumento `angle` proporciona el ángulo del desenfoque cinético.

## Parámetros

`radius`  
El radio del Gaussiano, en píxeles, sin contar el píxel central.

`sigma`  
La desviación estándar del Gaussiano, en píxeles.

`angle`  
Aplica el efecto a lo largo del ángulo.

## Valores devueltos

El objeto `Gmagick`.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
