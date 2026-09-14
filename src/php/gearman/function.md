---
title: GearmanTask::function
description: Obtiene el nombre de la función asociada (obsoleto)
source_url: https://www.php.net/manual/es/gearmantask.function.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmantask/function.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_revision: cf0a919c1
order: 25620
---

GearmanTask::function

Obtiene el nombre de la función asociada (obsoleto)

## Descripción

```php
public GearmanTask::function(): string
```php

Retorna el nombre de la función que esta tarea tiene asociada con, por ejemplo, la función que el trabajador de Gearman llama.

> [!NOTE]
> Este método ha sido reemplazado por GearmanTask::functionName en la versión 0.6.0 de la extensión Gearman.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El nombre de la función.
