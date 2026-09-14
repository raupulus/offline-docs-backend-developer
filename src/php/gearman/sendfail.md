---
title: GearmanJob::sendFail
description: Envía un estado de fallo
source_url: https://www.php.net/manual/es/gearmanjob.sendfail.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanjob/sendfail.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25480
---

GearmanJob::sendFail

Envía un estado de fallo

## Descripción

```php
public GearmanJob::sendFail(): bool
```php

Envía un estado de fallo para este trabajo, indicando que el trabajo ha fallado de forma inesperada (a diferencia de un error que emite una excepción).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

GearmanJob::sendException

GearmanJob::setReturn

GearmanJob::sendStatus

GearmanJob::sendWarning
