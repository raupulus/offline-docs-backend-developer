---
title: Gmagick::setsize
description: Define el tamaño del objeto Gmagick
source_url: https://www.php.net/manual/es/gmagick.setsize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/setsize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 27760
---

Gmagick::setsize

Define el tamaño del objeto Gmagick

## Descripción

```php
public Gmagick::setsize(int $columns, int $rows): Gmagick
```php

Define el tamaño del objeto Gmagick. Defínase el tamaño antes de leer una imagen sin procesar en el formato `Gmagick::COLORSPACE_RGB`, `Gmagick::COLORSPACE_GRAY`, o `Gmagick::COLORSPACE_CMYK`.

## Parámetros

`columns`  
El ancho, en píxeles.

`rows`  
La altura, en píxeles.

## Valores devueltos

El objeto `Gmagick`.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
