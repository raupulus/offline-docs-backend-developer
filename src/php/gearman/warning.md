---
title: GearmanJob::warning
description: Envía un aviso (obsoleto)
source_url: https://www.php.net/manual/es/gearmanjob.warning.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanjob/warning.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_revision: cf0a919c1
order: 25540
---

GearmanJob::warning

Envía un aviso (obsoleto)

## Descripción

```php
public GearmanJob::warning(string $warning): bool
```php

Envía un aviso para el trabajo mientras está en ejecución.

> [!NOTE]
> Este método ha sido reemplazado por GearmanJob::sendWarning en la versión 0.6.0 de la extensión Gearman.

## Parámetros

`warning`  
Un mensaje de aviso.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

GearmanJob::sendComplete

GearmanJob::sendException

GearmanJob::sendFail
