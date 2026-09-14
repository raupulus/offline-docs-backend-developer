---
title: openal_source_stop
description: Detiene la reproducción de la fuente
source_url: https://www.php.net/manual/es/function.openal-source-stop.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openal/functions/openal-source-stop.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openal
translation_status: ready
translation_revision: c55b13c1a
order: 58910
---

openal_source_stop

Detiene la reproducción de la fuente

## Descripción

```php
openal_source_stop(resource $source): bool
```php

## Parámetros

`source`  
Un recurso [Open AL(Source)](#openal.resources) (previamente creado por `openal_source_create`).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

openal_source_play

openal_source_pause

openal_source_rewind
