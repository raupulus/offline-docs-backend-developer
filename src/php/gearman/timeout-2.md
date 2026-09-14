---
title: GearmanWorker::timeout
description: Obtiene el tiempo de espera de la actividad del socket I/O
source_url: https://www.php.net/manual/es/gearmanworker.timeout.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanworker/timeout.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: 330a38c4d
order: 25920
---

GearmanWorker::timeout

Obtiene el tiempo de espera de la actividad del socket I/O

## Descripción

```php
public GearmanWorker::timeout(): int
```php

Devuelve el tiempo de espera actual, en milisegundos, de la actividad del socket I/O.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un período de tiempo, en milisegundos. Un valor negativo indica que el tiempo de espera es infinito.

## Véase también

GearmanWorker::setTimeout
