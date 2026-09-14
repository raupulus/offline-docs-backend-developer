---
title: Gmagick::medianfilterimage
description: Aplica un filtro digital
source_url: https://www.php.net/manual/es/gmagick.medianfilterimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/medianfilterimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 27190
---

Gmagick::medianfilterimage

Aplica un filtro digital

## Descripción

```php
public Gmagick::medianfilterimage(float $radius): void
```php

Aplica un filtro digital que mejora la calidad del ruido de una imagen. Cada píxel es reemplazado por la mediana en un conjunto de píxeles vecinos tal como se define por el radio.

## Parámetros

`radius`  
El radio de los píxeles vecinos.

## Valores devueltos

El objeto `Gmagick` al cual se le aplicó el filtro.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
