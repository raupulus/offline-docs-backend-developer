---
title: GearmanJob::status
description: Envía el estado (obsoleto)
source_url: https://www.php.net/manual/es/gearmanjob.status.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanjob/status.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_revision: 330a38c4d
order: 25520
---

GearmanJob::status

Envía el estado (obsoleto)

## Descripción

```php
public GearmanJob::status(int $numerator, int $denominator): bool
```php

Envía información de estado al servidor de trabajo y a cualquier cliente a la escucha. Usar para especificar qué porcentaje del trabajo ha sido completado.

> [!NOTE]
> Este método ha sido reemplazado por GearmanJob::sendStatus en la versión 0.6.0 de la extensión Gearman.

## Parámetros

`numerator`  
El numerador del porcentaje completado, expresado como una fracción.

`denominator`  
El denominador del porcentaje completado, expresado como una fracción.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

GearmanClient::jobStatus

GearmanTask::taskDenominator

GearmanTask::taskNumerator
