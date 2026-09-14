---
title: Gmagick::setsamplingfactors
description: Define los factores de muestreo de la imagen
source_url: https://www.php.net/manual/es/gmagick.setsamplingfactors.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/setsamplingfactors.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 27750
---

Gmagick::setsamplingfactors

Define los factores de muestreo de la imagen

## Descripción

```php
public Gmagick::setsamplingfactors(array $factors): Gmagick
```php

Define los factores de muestreo de la imagen.

## Parámetros

`factors`  
Un array de `float`s, representando el factor de muestreo para cada componente de color (en el orden RGB).

## Valores devueltos

El objeto `Gmagick`.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
