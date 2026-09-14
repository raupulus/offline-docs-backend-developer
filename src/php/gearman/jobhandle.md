---
title: GearmanTask::jobHandle
description: Obtiene el manejador de trabajos
source_url: https://www.php.net/manual/es/gearmantask.jobhandle.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmantask/jobhandle.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25660
---

GearmanTask::jobHandle

gearman_job_handle

Obtiene el manejador de trabajos

## Descripción

```php
public GearmanTask::jobHandle(): false
```php

Obtiene el manejador de trabajos para esta tarea.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El manejador de trabajos, o `false` si la tarea no ha sido creada aún.

## Véase también

GearmanClient::doJobHandle
