---
title: GearmanClient::addTaskHighBackground
description: Añade una tarea de fondo de alta prioridad para ser ejecutada en paralelo
source_url: https://www.php.net/manual/es/gearmanclient.addtaskhighbackground.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanclient/addtaskhighbackground.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 24940
---

GearmanClient::addTaskHighBackground

Añade una tarea de fondo de alta prioridad para ser ejecutada en paralelo

## Descripción

```php
public GearmanClient::addTaskHighBackground(string $function_name, string $workload, [mixed $context], [string $unique_key]): GearmanTask
```php

Añade una tarea de fondo de alta prioridad para ser ejecutada en paralelo con otras tareas. Esta método debe ser llamado para que todas las tareas sean ejecutadas simultáneamente, luego GearmanClient::runTasks debe ser llamado para realizar el trabajo. Las tareas con alta prioridad serán seleccionadas de la cola antes que las de prioridad más baja.

## Parámetros

`function_name`  
Una función registrada que el trabajador va a ejecutar

`workload`  
Datos serializados a analizar

`context`  
Contexto de la aplicación a asociar con una tarea

`unique_key`  
Un identificador único utilizado para identificar una tarea particular

## Valores devueltos

Un objeto `GearmanTask` o `false` si la tarea no puede ser añadida.

## Véase también

GearmanClient::addTask

GearmanClient::addTaskHigh

GearmanClient::addTaskLow

GearmanClient::addTaskBackground

GearmanClient::addTaskLowBackground

GearmanClient::runTasks
