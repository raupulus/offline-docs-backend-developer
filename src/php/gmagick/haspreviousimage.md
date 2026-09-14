---
title: Gmagick::haspreviousimage
description: Verifica si el objeto tiene una imagen previa
source_url: https://www.php.net/manual/es/gmagick.haspreviousimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/haspreviousimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_revision: 35752f072
order: 27130
---

Gmagick::haspreviousimage

Verifica si el objeto tiene una imagen previa

## Descripción

```php
public Gmagick::haspreviousimage(): mixed
```php

Devuelve `true` si el objeto tiene más imágenes cuando se atraviesa la lista en la dirección opuesta

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si el objeto tiene más imágenes cuando se atraviesa la lista en la dirección opuesta, devuelve `false` si no hay ninguna.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
