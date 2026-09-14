---
title: GearmanClient::doLowBackground
description: Ejecuta una tarea en prioridad baja en segundo plano
source_url: https://www.php.net/manual/es/gearmanclient.dolowbackground.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanclient/dolowbackground.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25090
---

GearmanClient::doLowBackground

Ejecuta una tarea en prioridad baja en segundo plano

## Descripción

```php
public GearmanClient::doLowBackground(string $function, string $workload, [string $unique]): string
```php

Ejecuta una tarea en prioridad baja en segundo plano, luego, devuelve el gestor de trabajos que podrá ser utilizado para recuperar el estado de la tarea en curso. Las tareas con prioridad normal y alta tendrán prioridad sobre aquellas con prioridad baja en la cola.

## Parámetros

`function`  
Una función registrada que el trabajador va a ejecutar

`workload`  
Datos serializados a analizar

`unique`  
Un identificador único utilizado para identificar una tarea particular

## Valores devueltos

El gestor de trabajos de la tarea enviada.

## Véase también

GearmanClient::doNormal

GearmanClient::doHigh

GearmanClient::doLow

GearmanClient::doBackground

GearmanClient::doHighBackground
