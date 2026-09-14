---
title: Gmagick::resampleimage
description: Re-muestrea la imagen a la resolución deseada
source_url: https://www.php.net/manual/es/gmagick.resampleimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/resampleimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 27430
---

Gmagick::resampleimage

Re-muestrea la imagen a la resolución deseada

## Descripción

```php
public Gmagick::resampleimage(float $xResolution, float $yResolution, int $filter, float $blur): Gmagick
```php

Re-muestrea la imagen a la resolución deseada.

## Parámetros

`xResolution`  
La nueva resolución x de la imagen.

`yResolution`  
La nueva resolución x de la imagen.

`filter`  
El filtro de imagen a usar.

`blur`  
El factor de borrosidad donde mayor que que es borroso, menor que uno es nítido.

## Valores devueltos

El objeto Gmagick si se tuvo éxito

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
