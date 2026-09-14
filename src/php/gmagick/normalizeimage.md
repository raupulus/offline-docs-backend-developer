---
title: Gmagick::normalizeimage
description: Mejora el contraste del color de la imagen
source_url: https://www.php.net/manual/es/gmagick.normalizeimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/normalizeimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 27250
---

Gmagick::normalizeimage

Mejora el contraste del color de la imagen

## Descripción

```php
public Gmagick::normalizeimage([int $channel]): Gmagick
```php

Mejora el contraste del color de la imagen ajustando el color de los píxeles para que correspondan al intervalo de colores disponibles.

## Parámetros

`channel`  
Canal a normalizar.

## Valores devueltos

El objeto `Gmagick`.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
