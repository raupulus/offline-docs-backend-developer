---
title: openal_context_create
description: Crea un contexto de procesamiento de audio
source_url: https://www.php.net/manual/es/function.openal-context-create.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openal/functions/openal-context-create.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openal
translation_status: ready
translation_revision: c55b13c1a
order: 58750
---

openal_context_create

Crea un contexto de procesamiento de audio

## Descripción

```php
openal_context_create(resource $device): resource
```php

## Parámetros

`device`  
Un recurso [Open AL(Device)](#openal.resources) (previamente creado por `openal_device_open`).

## Valores devueltos

Devuelve un recurso [Open AL(Context)](#openal.resources) en éxito o `false` en fallo.

## Véase también

openal_device_open

openal_context_destroy
