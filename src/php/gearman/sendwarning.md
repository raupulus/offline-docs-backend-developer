---
title: GearmanJob::sendWarning
description: Envía una alerta
source_url: https://www.php.net/manual/es/gearmanjob.sendwarning.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanjob/sendwarning.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25500
---

GearmanJob::sendWarning

Envía una alerta

## Descripción

```php
public GearmanJob::sendWarning(string $warning): bool
```php

Envía una alerta para este trabajo durante su ejecución.

## Parámetros

`warning`  
Un mensaje de alerta.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

GearmanJob::sendComplete

GearmanJob::sendException

GearmanJob::sendFail
