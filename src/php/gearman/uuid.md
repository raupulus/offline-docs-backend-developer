---
title: GearmanTask::uuid
description: Recupera el identificador único para una tarea (obsoleto)
source_url: https://www.php.net/manual/es/gearmantask.uuid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmantask/uuid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25740
---

GearmanTask::uuid

Recupera el identificador único para una tarea (obsoleto)

## Descripción

```php
public GearmanTask::uuid(): string
```php

Devuelve el identificador único para una tarea. Es asignado por el método `GearmanClient`, a diferencia del gestor de trabajos que es definido por el servidor de trabajos Gearman.

> [!NOTE]
> Este método ha sido reemplazado por el método GearmanTask::unique desde la versión 0.6.0 de la extensión Gearman.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El identificador único, o `false` si ningún identificador está asignado.

## Véase también

GearmanClient::do

GearmanClient::addTask
