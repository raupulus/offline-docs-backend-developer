---
title: SessionUpdateTimestampHandlerInterface::validateId
description: Validar el ID
source_url: https://www.php.net/manual/es/sessionupdatetimestamphandlerinterface.validateid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/sessionupdatetimestamphandlerinterface/validateid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_reviewed: true
translation_revision: 601f6f4ce
order: 74140
---

SessionUpdateTimestampHandlerInterface::validateId

Validar el ID

## Descripción

```php
public SessionUpdateTimestampHandlerInterface::validateId(string $id): bool
```php

Valida un ID de sesión dado. Un ID de sesión es válido, si una sesión con este ID ya existe. Esta función se ejecuta automáticamente cuando se inicia una sesión, se proporciona un ID de sesión y [session.use_strict_mode](#ini.session.use-strict-mode) está activado.

## Parámetros

`id`  
El ID de sesión

## Valores devueltos

Devuelve `true` para un ID válido, `false` en caso contrario. Se debe tener en cuenta que este valor se devuelve internamente a PHP para su procesamiento.
