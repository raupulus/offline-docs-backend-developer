---
title: GearmanWorker::unregisterAll
description: Elimina todas las funciones de los servidores de trabajos
source_url: https://www.php.net/manual/es/gearmanworker.unregisterall.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanworker/unregisterall.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25940
---

GearmanWorker::unregisterAll

Elimina todas las funciones de los servidores de trabajos

## Descripción

```php
public GearmanWorker::unregisterAll(): bool
```php

Elimina todas las funciones previamente registradas, asegurando así que ningún trabajo será enviado al agente con estas funciones.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un valor de retorno estándar de Gearman.

## Véase también

GearmanWorker::register

GearmanWorker::unregister
