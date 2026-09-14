---
title: sapi_windows_cp_get
description: Devuelve la página de código actual
source_url: https://www.php.net/manual/es/function.sapi-windows-cp-get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/misc/functions/sapi-windows-cp-get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: misc
translation_status: ready
translation_reviewed: true
translation_revision: 7f99d5e48
order: 47170
---

sapi_windows_cp_get

Devuelve la página de código actual

## Descripción

```php
sapi_windows_cp_get([string $kind]): int
```php

Devuelve la página de código actual.

## Parámetros

`kind`  
El tipo de página de código del sistema operativo a obtener, ya sea `'ansi'` o `'oem'`. Cualquier otro valor hace referencia a la página de código actual del proceso.

## Valores devueltos

Si `kind` es `'ansi'`, se devuelve la página de código ANSI actual del sistema operativo. Si `kind` es `'oem'`, se devuelve la página de código OEM actual del sistema operativo. En caso contrario, se devuelve la página de código actual del proceso.

## Véase también

sapi_windows_cp_set
