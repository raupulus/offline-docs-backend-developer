---
title: GearmanJob::data
description: Envía datos para un trabajo en ejecución (obsoleto)
source_url: https://www.php.net/manual/es/gearmanjob.data.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanjob/data.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_revision: cf0a919c1
order: 25390
---

GearmanJob::data

Envía datos para un trabajo en ejecución (obsoleto)

## Descripción

```php
public GearmanJob::data(string $data): bool
```php

Envía datos al servidor de trabajos (y a cualquier cliente a la escucha) para este trabajo.

> [!NOTE]
> Este método ha sido reemplazado por GearmanJob::sendData en la versión 0.6.0 de la extensión Gearman.

## Parámetros

`data`  
Datos arbitrarios serializados.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

GearmanJob::workload

GearmanTask::data
