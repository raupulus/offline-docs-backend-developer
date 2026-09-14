---
title: GearmanClient::runTasks
description: Ejecuta una lista de tareas en paralelo
source_url: https://www.php.net/manual/es/gearmanclient.runtasks.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanclient/runtasks.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25190
---

GearmanClient::runTasks

Ejecuta una lista de tareas en paralelo

## Descripción

```php
public GearmanClient::runTasks(): bool
```php

Para un conjunto de tareas previamente añadidas con los métodos GearmanClient::addTask, GearmanClient::addTaskHigh, GearmanClient::addTaskLow, GearmanClient::addTaskBackground, GearmanClient::addTaskHighBackground, o GearmanClient::addTaskLowBackground, este método inicia la ejecución de las tareas en paralelo.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

GearmanClient::addTask
