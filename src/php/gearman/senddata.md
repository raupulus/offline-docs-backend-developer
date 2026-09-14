---
title: GearmanJob::sendData
description: Envía los datos para un trabajo en ejecución
source_url: https://www.php.net/manual/es/gearmanjob.senddata.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanjob/senddata.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25460
---

GearmanJob::sendData

Envía los datos para un trabajo en ejecución

## Descripción

```php
public GearmanJob::sendData(string $data): bool
```php

Envía los datos al servidor de trabajos (y a todos los clientes que escuchen) para este trabajo.

## Parámetros

`data`  
Datos serializados arbitrarios.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

GearmanJob::workload

GearmanTask::data
