---
title: GearmanTask::unique
description: Obtiene el identificador único de la tarea
source_url: https://www.php.net/manual/es/gearmantask.unique.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmantask/unique.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25730
---

GearmanTask::unique

Obtiene el identificador único de la tarea

## Descripción

```php
public GearmanTask::unique(): false
```php

Devuelve el identificador único de la tarea. Este es asignado por el método `GearmanClient`, a diferencia del gestor de trabajos que es definido por el servidor de trabajos Gearman.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El identificador único, o `false` si no se ha asignado ningún identificador.

## Véase también

GearmanClient::do

GearmanClient::addTask
