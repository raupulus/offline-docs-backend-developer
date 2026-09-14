---
title: runkit7_function_remove
description: Elimina una definición de función
source_url: https://www.php.net/manual/es/function.runkit7-function-remove.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/runkit7/functions/runkit7-function-remove.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: runkit7
translation_status: ready
translation_reviewed: true
translation_revision: c4625323f
order: 72900
---

runkit7_function_remove

Elimina una definición de función

## Descripción

```php
runkit7_function_remove(string $function_name): bool
```php

> [!NOTE]
> Por defecto, solo las funciones definidas por el usuario pueden ser eliminadas, renombradas o modificadas. Para sobrescribir funciones internas, se debe activar la configuración `runkit.internal_override` en el archivo `php.ini` del sistema entero.

## Parámetros

`function_name`  
El nombre de la función a eliminar

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

runkit7_function_add

runkit7_function_copy

runkit7_function_redefine

runkit7_function_rename
