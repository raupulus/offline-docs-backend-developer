---
title: GearmanTask::functionName
description: Obtiene el nombre de la función asociada
source_url: https://www.php.net/manual/es/gearmantask.functionname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmantask/functionname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25630
---

GearmanTask::functionName

Obtiene el nombre de la función asociada

## Descripción

```php
public GearmanTask::functionName(): false
```php

Devuelve el nombre de la función asociada a esta tarea, es decir, la función llamada por el agente Gearman.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un nombre de función, o `false` si la tarea no ha sido creada aún.
