---
title: Gmagick::deconstructimages
description: Devuelve ciertas diferencias de píxeles entre imágenes
source_url: https://www.php.net/manual/es/gmagick.deconstructimages.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/deconstructimages.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_revision: 35752f072
order: 26600
---

Gmagick::deconstructimages

Devuelve ciertas diferencias de píxeles entre imágenes

## Descripción

```php
public Gmagick::deconstructimages(): Gmagick
```php

Compara cada imagen con la siguiente en una secuencia y devuelve la región circundante máxima de cualquier diferencia de píxeles que se descubra.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un nuevo objeto `Gmagick` en caso de éxito.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
