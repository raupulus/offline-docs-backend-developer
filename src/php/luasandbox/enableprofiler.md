---
title: LuaSandbox::enableProfiler
description: Activa el perfilador
source_url: https://www.php.net/manual/es/luasandbox.enableprofiler.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/luasandbox/luasandbox/enableprofiler.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: luasandbox
translation_status: ready
translation_reviewed: false
translation_revision: 9c40251a8
order: 43930
---

LuaSandbox::enableProfiler

Activa el perfilador

## Descripción

```php
public LuaSandbox::enableProfiler([float $period]): bool
```php

Activa el perfilador. El perfilado comenzará cuando se ingrese código Lua.

El perfilador muestrea periódicamente el entorno Lua para registrar la función en ejecución. Las pruebas indican que, al menos en Linux, un período inferior a 1ms resultará en un número elevado de desbordamientos, pero sin problemas de rendimiento.

## Parámetros

`period`  
Muestreo en segundos.

## Valores devueltos

Devuelve un bool indicando si el perfilador está activado.

## Véase también

LuaSandbox::disableProfiler

LuaSandbox::getProfilerFunctionReport
