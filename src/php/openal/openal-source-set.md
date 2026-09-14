---
title: openal_source_set
description: Establece la propiedad de la fuente
source_url: https://www.php.net/manual/es/function.openal-source-set.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openal/functions/openal-source-set.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openal
translation_status: ready
translation_revision: c55b13c1a
order: 58900
---

openal_source_set

Establece la propiedad de la fuente

## Descripción

```php
openal_source_set(resource $source, int $property, mixed $setting): bool
```php

## Parámetros

`source`  
Un recurso [Open AL(Source)](#openal.resources) (previamente creado por `openal_source_create`).

`property`  
Propiedad para establecer, una de: `AL_BUFFER` (OpenAL(Source)), `AL_LOOPING` (bool), `AL_SOURCE_RELATIVE` (int), `AL_SOURCE_STATE` (int), `AL_PITCH` (float), `AL_GAIN` (float), `AL_MIN_GAIN` (float), `AL_MAX_GAIN` (float), `AL_MAX_DISTANCE` (float), `AL_ROLLOFF_FACTOR` (float), `AL_CONE_OUTER_GAIN` (float), `AL_CONE_INNER_ANGLE` (float), `AL_CONE_OUTER_ANGLE` (float), `AL_REFERENCE_DISTANCE` (float), `AL_POSITION` (array(float,float,float)), `AL_VELOCITY` (array(float,float,float)), `AL_DIRECTION` (array(float,float,float)).

`setting`  
El valor para asignar a la `property` especifica. Consulta la descripción de la `property` para una descripción de el valor(es) esperando.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

openal_source_create

openal_source_get

openal_source_play
