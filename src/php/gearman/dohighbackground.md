---
title: GearmanClient::doHighBackground
description: Ejecuta una tarea con prioridad alta en segundo plano
source_url: https://www.php.net/manual/es/gearmanclient.dohighbackground.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanclient/dohighbackground.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25060
---

GearmanClient::doHighBackground

Ejecuta una tarea con prioridad alta en segundo plano

## Descripción

```php
public GearmanClient::doHighBackground(string $function, string $workload, [string $unique]): string
```php

Ejecuta una tarea con prioridad alta en segundo plano, y devuelve un manejador de trabajo que puede ser utilizado para recuperar el estado de la tarea. Las tareas con prioridad alta serán ejecutadas antes que las normales y las bajas de la cola.

## Parámetros

`function`  
Una función registrada que el trabajador va a ejecutar

`workload`  
Datos serializados a analizar

`unique`  
Un identificador único utilizado para identificar una tarea particular

## Valores devueltos

El manejador de trabajo de la tarea añadida.

## Véase también

GearmanClient::doNormal

GearmanClient::doHigh

GearmanClient::doLow

GearmanClient::doBackground

GearmanClient::doLowBackground
