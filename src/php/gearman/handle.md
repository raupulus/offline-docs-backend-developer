---
title: GearmanJob::handle
description: Obtiene el manejador de trabajos
source_url: https://www.php.net/manual/es/gearmanjob.handle.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanjob/handle.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25430
---

GearmanJob::handle

Obtiene el manejador de trabajos

## Descripción

```php
public GearmanJob::handle(): false
```php

Devuelve el manejador de trabajos asignado por el servidor de trabajos.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un manejador de trabajos, o `false` si el trabajo no ha sido inicializado.

## Véase también

GearmanTask::jobHandle
