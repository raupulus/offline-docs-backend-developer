---
title: pcntl_setcpuaffinity
description: Define la afinidad de CPU de un proceso
source_url: https://www.php.net/manual/es/function.pcntl-setcpuaffinity.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/functions/pcntl-setcpuaffinity.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_reviewed: true
translation_revision: 74b623916
order: 61300
---

pcntl_setcpuaffinity

Define la afinidad de CPU de un proceso

## Descripción

```php
pcntl_setcpuaffinity([int $process_id], [array $cpu_ids]): bool
```php

Define la afinidad de CPU del `process_id` con el máscara de afinidad de CPU proporcionada por `cpu_ids`.

## Parámetros

`process_id`  
Si `null`, se utiliza el identificador del proceso actual.

`cpu_ids`  
El máscara de afinidad de CPU compuesto por uno o más identificadores de CPU a los que se vincula el proceso.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Se lanza una `TypeError` si uno de los identificadores de CPU de `cpu_ids` es inválido. Se lanza una `ValueError` si `process_id` es un identificador de proceso inválido o si el máscara de CPU no ha podido ser creado.

## Véase también

pcntl_getcpuaffinity
