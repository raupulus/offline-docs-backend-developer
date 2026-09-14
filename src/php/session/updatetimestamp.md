---
title: SessionUpdateTimestampHandlerInterface::updateTimestamp
description: Actualizar la marca de tiempo
source_url: https://www.php.net/manual/es/sessionupdatetimestamphandlerinterface.updatetimestamp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/sessionupdatetimestamphandlerinterface/updatetimestamp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_reviewed: true
translation_revision: 601f6f4ce
order: 74130
---

SessionUpdateTimestampHandlerInterface::updateTimestamp

Actualizar la marca de tiempo

## Descripción

```php
public SessionUpdateTimestampHandlerInterface::updateTimestamp(string $id, string $data): bool
```php

Actualiza la marca de tiempo de última modificación de la sesión. Esta función se ejecuta automáticamente cuando una sesión es actualizada.

## Parámetros

`id`  
El ID de sesión.

`data`  
Los datos de sesión.

## Valores devueltos

Devuelve `true` si la marca de tiempo ha sido actualizada, `false` en caso contrario. Se debe tener en cuenta que este valor es devuelto internamente a PHP para su procesamiento.
