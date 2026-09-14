---
title: GearmanWorker::error
description: Obtiene el último error ocurrido
source_url: https://www.php.net/manual/es/gearmanworker.error.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanworker/error.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25830
---

GearmanWorker::error

Obtiene el último error ocurrido

## Descripción

```php
public GearmanWorker::error(): string
```php

Devuelve el último error ocurrido, en forma de `string`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Una `string` legible por humanos que representa el último error ocurrido, o `false` si no hay mensaje de error disponible.

## Véase también

GearmanWorker::getErrno
