---
title: openal_listener_set
description: Establece una propiedad de oyente
source_url: https://www.php.net/manual/es/function.openal-listener-set.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openal/functions/openal-listener-set.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openal
translation_status: ready
translation_revision: c55b13c1a
order: 58830
---

openal_listener_set

Establece una propiedad de oyente

## Descripción

```php
openal_listener_set(int $property, mixed $setting): bool
```php

## Parámetros

`property`  
Propiedad a establecer, una de: `AL_GAIN` (float), `AL_POSITION` (array(float,float,float)), `AL_VELOCITY` (array(float,float,float)) y `AL_ORIENTATION` (array(float,float,float)).

`setting`  
Valor a establecer, ya sea flotante, o un arreglo de flotantes como apropiado.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

openal_listener_get
