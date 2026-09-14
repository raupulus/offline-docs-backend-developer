---
title: openal_source_get
description: Recupera una propiedad de una fuente del OpenAL
source_url: https://www.php.net/manual/es/function.openal-source-get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openal/functions/openal-source-get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openal
translation_status: ready
translation_revision: c55b13c1a
order: 58860
---

openal_source_get

Recupera una propiedad de una fuente del OpenAL

## Descripción

```php
openal_source_get(resource $source, int $property): mixed
```php

## Parámetros

`source`  
Un recurso [Open AL(Source)](#openal.resources) (previamente creado por `openal_source_create`).

`property`  
Propiedad para obtener, una de: `AL_SOURCE_RELATIVE` (int), `AL_SOURCE_STATE` (int), `AL_PITCH` (float), `AL_GAIN` (float), `AL_MIN_GAIN` (float), `AL_MAX_GAIN` (float), `AL_MAX_DISTANCE` (float), `AL_ROLLOFF_FACTOR` (float), `AL_CONE_OUTER_GAIN` (float), `AL_CONE_INNER_ANGLE` (float), `AL_CONE_OUTER_ANGLE` (float), `AL_REFERENCE_DISTANCE` (float), `AL_POSITION` (array(float,float,float)), `AL_VELOCITY` (array(float,float,float)), `AL_DIRECTION` (array(float,float,float)).

## Valores devueltos

Devuelve el tipo asociado con la propiedad que se recupera o `false` si ocurre un error.

## Véase también

openal_source_create

openal_source_set

openal_source_play
