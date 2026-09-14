---
title: GearmanJob::sendComplete
description: Envía el resultado junto con el estado completo
source_url: https://www.php.net/manual/es/gearmanjob.sendcomplete.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanjob/sendcomplete.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25450
---

GearmanJob::sendComplete

Envía el resultado junto con el estado completo

## Descripción

```php
public GearmanJob::sendComplete(string $result): bool
```php

Envía los datos del resultado junto con el estado completo actualizado para este trabajo.

## Parámetros

`result`  
Los datos serializados del resultado.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

GearmanJob::sendFail

GearmanJob::setReturn
