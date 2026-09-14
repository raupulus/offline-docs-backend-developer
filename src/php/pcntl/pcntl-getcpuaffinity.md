---
title: pcntl_getcpuaffinity
description: Devuelve la afinidad de CPU de un proceso
source_url: https://www.php.net/manual/es/function.pcntl-getcpuaffinity.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/functions/pcntl-getcpuaffinity.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_reviewed: true
translation_revision: aa120f36c
order: 61260
---

pcntl_getcpuaffinity

Devuelve la afinidad de CPU de un proceso

## Descripción

```php
pcntl_getcpuaffinity([int $process_id]): array
```php

Devuelve la afinidad de CPU del `process_id`.

## Parámetros

`process_id`  
Si `null`, se utiliza el identificador del proceso actual.

## Valores devueltos

Devuelve la máscara de afinidad de CPU del proceso, o `false` si ocurre un error.

> [!WARNING]
> Esta función puede retornar `false`, pero también puede retornar un valor equivalente a `false`. Por favor, lea la sección sobre los [booleanos](#language.types.boolean) para más información. Utilice el [operador ===](#language.operators.comparison) para probar el valor de retorno exacto de esta función.

## Errores/Excepciones

Se lanza una `ValueError` cuando `process_id` es un identificador de proceso no válido o cuando no se ha podido crear la máscara de CPU.

Si `process_id` es un proceso para el cual el usuario actual no tiene permiso autorizado, se emite un `E_WARNING`.

## Véase también

pcntl_setcpuaffinity
