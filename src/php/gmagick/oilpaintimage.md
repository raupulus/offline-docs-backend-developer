---
title: Gmagick::oilpaintimage
description: Simula una pintura al óleo
source_url: https://www.php.net/manual/es/gmagick.oilpaintimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/oilpaintimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 27260
---

Gmagick::oilpaintimage

Simula una pintura al óleo

## Descripción

```php
public Gmagick::oilpaintimage(float $radius): Gmagick
```php

Aplica un filtro de efecto especial que simula una pintura al óleo. Cada píxel es reemplazado por el color más frecuente que suceda en una región circular definida por el radio.

## Parámetros

`radius`  
El radio de la zona inmediata circular.

## Valores devueltos

El objeto Gmagick si se tuvo éxito

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
