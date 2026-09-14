---
title: openal_buffer_data
description: Carga un buffer con datos
source_url: https://www.php.net/manual/es/function.openal-buffer-data.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openal/functions/openal-buffer-data.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openal
translation_status: ready
translation_revision: c55b13c1a
order: 58710
---

openal_buffer_data

Carga un buffer con datos

## Descripción

```php
openal_buffer_data(resource $buffer, int $format, string $data, int $freq): bool
```php

## Parámetros

`buffer`  
Un recurso [Open AL(Buffer)](#openal.resources) (previamente creado por `openal_buffer_create`).

`format`  
Formato de `data`, uno de: `AL_FORMAT_MONO8`, `AL_FORMAT_MONO16`, `AL_FORMAT_STEREO8` y `AL_FORMAT_STEREO16`

`data`  
Bloque de datos de audio binario en el `format` y el `freq` especificado.

`freq`  
Frecuencia de `data` dados en Hz.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

openal_buffer_loadwav

openal_stream
