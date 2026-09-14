---
title: GearmanJob::unique
description: Obtiene el identificador único
source_url: https://www.php.net/manual/es/gearmanjob.unique.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanjob/unique.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25530
---

GearmanJob::unique

Obtiene el identificador único

## Descripción

```php
public GearmanJob::unique(): false
```php

Devuelve el identificador único para este trabajo. El identificador es asignado por el cliente.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El identificador único, o `false` si el trabajo no ha sido inicializado.

## Véase también

GearmanClient::do

GearmanTask::uuid
