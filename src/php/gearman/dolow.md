---
title: GearmanClient::doLow
description: Ejecuta una sola tarea con prioridad baja
source_url: https://www.php.net/manual/es/gearmanclient.dolow.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanclient/dolow.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25080
---

GearmanClient::doLow

Ejecuta una sola tarea con prioridad baja

## Descripción

```php
public GearmanClient::doLow(string $function, string $workload, [string $unique]): string
```php

Ejecuta una sola tarea con prioridad baja y devuelve una representación en forma de `string` del resultado. Es responsabilidad de los métodos `GearmanClient` y `GearmanWorker` validar el formato del resultado. Las tareas con prioridad normal o alta serán tratadas con preferencia frente a las tareas con prioridad baja en la cola de espera.

## Parámetros

`function`  
Una función registrada que el trabajador va a ejecutar

`workload`  
Datos serializados a analizar

`unique`  
Un identificador único utilizado para identificar una tarea particular

## Valores devueltos

Una representación en forma de `string` del resultado de la tarea en curso.

## Véase también

GearmanClient::doNormal

GearmanClient::doHigh

GearmanClient::doBackground

GearmanClient::doHighBackground

GearmanClient::doLowBackground
