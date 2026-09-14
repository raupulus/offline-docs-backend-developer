---
title: GearmanJob::functionName
description: Obtiene el nombre de la función
source_url: https://www.php.net/manual/es/gearmanjob.functionname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanjob/functionname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25420
---

GearmanJob::functionName

Obtiene el nombre de la función

## Descripción

```php
public GearmanJob::functionName(): false
```php

Devuelve el nombre de la función para este trabajo. Es la función ejecutada por el agente para ejecutar el trabajo.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El nombre de la función, o `false` si el trabajo no ha sido inicializado.

## Véase también

GearmanTask::function
