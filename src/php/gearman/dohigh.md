---
title: GearmanClient::doHigh
description: Ejecuta una sola tarea con prioridad alta
source_url: https://www.php.net/manual/es/gearmanclient.dohigh.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanclient/dohigh.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25050
---

GearmanClient::doHigh

Ejecuta una sola tarea con prioridad alta

## Descripción

```php
public GearmanClient::doHigh(string $function, string $workload, [string $unique]): string
```php

Ejecuta una sola tarea con prioridad alta y devuelve una representación del resultado en forma de `string`. Corresponde a las funciones `GearmanClient` y `GearmanWorker` acordar el formato del resultado. Las tareas con prioridad alta se ejecutarán antes que aquellas con prioridad normal o baja en la cola de espera.

## Parámetros

`function`  
Una función registrada que el trabajador va a ejecutar

`workload`  
Datos serializados a analizar

`unique`  
Un identificador único utilizado para identificar una tarea particular

## Valores devueltos

El resultado de la tarea en forma de `string`.

## Véase también

GearmanClient::doNormal

GearmanClient::doLow

GearmanClient::doBackground

GearmanClient::doHighBackground

GearmanClient::doLowBackground
