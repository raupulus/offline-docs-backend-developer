---
title: GearmanJob::fail
description: Envía el estado de fallo (obsoleto)
source_url: https://www.php.net/manual/es/gearmanjob.fail.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanjob/fail.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_revision: cf0a919c1
order: 25410
---

GearmanJob::fail

Envía el estado de fallo (obsoleto)

## Descripción

```php
public GearmanJob::fail(): bool
```php

Envía el estado de fallo para este trabajo, indicando que el trabajo ha fallado por razones conocidas (en contraposición a un fallo debido al lanzamiento de una excepción).

> [!NOTE]
> Este método ha sido reemplazado por GearmanJob::sendFail en la versión 0.6.0 de la extensión Gearman.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

GearmanJob::sendException

GearmanJob::setReturn

GearmanJob::sendStatus

GearmanJob::sendWarning
