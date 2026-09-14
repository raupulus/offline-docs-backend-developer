---
title: memory_get_peak_usage
description: Devuelve la cantidad máxima de memoria asignada por PHP
source_url: https://www.php.net/manual/es/function.memory-get-peak-usage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/memory-get-peak-usage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: true
translation_revision: 57015edfe
order: 39090
---

memory_get_peak_usage

Devuelve la cantidad máxima de memoria asignada por PHP

## Descripción

```php
memory_get_peak_usage([bool $real_usage]): int
```php

Devuelve la cantidad máxima de memoria, en bytes, que ha sido asignada al script PHP.

## Parámetros

`real_usage`  
Definir como `true` para obtener el tamaño real de la memoria asignada por el sistema. Si este argumento no está definido o vale `false`, solo se devolverá la memoria utilizada por `emalloc()`.

## Valores devueltos

Devuelve la cantidad de memoria, en bytes.

## Véase también

`memory_get_usage`, `memory_reset_peak_usage`, [memory_limit](#ini.memory-limit)
