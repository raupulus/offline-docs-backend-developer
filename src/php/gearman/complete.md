---
title: GearmanJob::complete
description: Envía el resultado y el estado completo (obsoleto)
source_url: https://www.php.net/manual/es/gearmanjob.complete.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanjob/complete.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_revision: cf0a919c1
order: 25370
---

GearmanJob::complete

Envía el resultado y el estado completo (obsoleto)

## Descripción

```php
public GearmanJob::complete(string $result): bool
```php

Envía los datos que han resultado del proceso y actualiza el estado a completo para este trabajo.

> [!NOTE]
> Este método ha sido reemplazado por GearmanJob::sendComplete en la versión 0.6.0 de la extensión Gearman.

## Parámetros

`result`  
Los datos que han resultado en formato serializado.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

GearmanJob::sendFail

GearmanJob::setReturn
