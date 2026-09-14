---
title: GearmanJob::exception
description: Envía una excepción para un trabajo en ejecución (obsoleto)
source_url: https://www.php.net/manual/es/gearmanjob.exception.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanjob/exception.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_revision: cf0a919c1
order: 25400
---

GearmanJob::exception

Envía una excepción para un trabajo en ejecución (obsoleto)

## Descripción

```php
public GearmanJob::exception(string $exception): bool
```php

Envía la excepción indicada cuando este trabajo está siendo ejecutado.

> [!NOTE]
> Este método ha sido reemplazado por GearmanJob::sendException en la versión 0.6.0 de la extensión Gearman.

## Parámetros

`exception`  
Descripción de la excepción.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

GearmanJob::setReturn

GearmanJob::sendStatus

GearmanJob::sendWarning
