---
title: openal_stream
description: Inicia el streaming de una fuente
source_url: https://www.php.net/manual/es/function.openal-stream.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openal/functions/openal-stream.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openal
translation_status: ready
translation_reviewed: false
translation_revision: c55b13c1a
order: 58920
---

openal_stream

Inicia el streaming de una fuente

## Descripción

```php
openal_stream(resource $source, int $format, int $rate): resource
```php

## Parámetros

`source`  
Un recurso [Open AL(Source)](#openal.resources) (previamente creado por `openal_source_create`).

`format`  
El formato del argumento `data`, uno de los siguientes: `AL_FORMAT_MONO8`, `AL_FORMAT_MONO16`, `AL_FORMAT_STEREO8` y `AL_FORMAT_STEREO16`.

`rate`  
La frecuencia de los datos a streamear, en Hz.

## Valores devueltos

Devuelve un recurso de streaming o `false` si ocurre un error.

## Véase también

openal_source_create

fwrite
