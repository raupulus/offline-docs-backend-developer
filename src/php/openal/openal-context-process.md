---
title: openal_context_process
description: Procesa un contexto especificado
source_url: https://www.php.net/manual/es/function.openal-context-process.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openal/functions/openal-context-process.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openal
translation_status: ready
translation_revision: c55b13c1a
order: 58780
---

openal_context_process

Procesa un contexto especificado

## Descripción

```php
openal_context_process(resource $context): bool
```php

## Parámetros

`context`  
Un recurso [Open AL(Context)](#openal.resources) (previamente creado por `openal_context_create`).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

openal_context_create

openal_context_current

openal_context_suspend
