---
title: GearmanJob::sendStatus
description: Envía un estado
source_url: https://www.php.net/manual/es/gearmanjob.sendstatus.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanjob/sendstatus.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: 330a38c4d
order: 25490
---

GearmanJob::sendStatus

Envía un estado

## Descripción

```php
public GearmanJob::sendStatus(int $numerator, int $denominator): bool
```php

Envía información de estado al servidor de trabajos así como a todos los clientes que estén escuchando. Utilícese esta función para especificar el porcentaje de realización del trabajo actual.

## Parámetros

`numerator`  
El numerador de la tasa de realización, en forma de fracción.

`denominator`  
El denominador de la tasa de realización, en forma de fracción.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

GearmanClient::jobStatus

GearmanTask::taskDenominator

GearmanTask::taskNumerator
