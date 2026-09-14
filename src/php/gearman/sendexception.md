---
title: GearmanJob::sendException
description: Envía una excepción para un trabajo en ejecución
source_url: https://www.php.net/manual/es/gearmanjob.sendexception.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanjob/sendexception.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25470
---

GearmanJob::sendException

Envía una excepción para un trabajo en ejecución

## Descripción

```php
public GearmanJob::sendException(string $exception): bool
```php

Envía la excepción proporcionada durante la ejecución de este trabajo.

## Parámetros

`exception`  
Una descripción de excepción.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

GearmanJob::setReturn

GearmanJob::sendStatus

GearmanJob::sendWarning
