---
title: GearmanWorker::register
description: Registra una función en un servidor de trabajos
source_url: https://www.php.net/manual/es/gearmanworker.register.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanworker/register.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25860
---

GearmanWorker::register

Registra una función en un servidor de trabajos

## Descripción

```php
public GearmanWorker::register(string $function_name, [int $timeout]): bool
```php

Se registra un nombre de función con un servidor de trabajos con un tiempo máximo de ejecución opcional. Este tiempo especifica el número de segundos que el servidor debe esperar antes de marcar una tarea como fallida. Si este tiempo se establece en cero, no habrá ningún límite.

## Parámetros

`function_name`  
El nombre de la función a registrar con el servidor de trabajos.

`timeout`  
Un intervalo de tiempo, en segundos.

## Valores devueltos

Un valor de retorno estándar de Gearman.

## Véase también

GearmanWorker::unregister

GearmanWorker::unregisterAll
