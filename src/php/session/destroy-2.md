---
title: SessionHandlerInterface::destroy
description: Destruir una sesión
source_url: https://www.php.net/manual/es/sessionhandlerinterface.destroy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/sessionhandlerinterface/destroy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_reviewed: false
translation_revision: 601f6f4ce
order: 74050
---

SessionHandlerInterface::destroy

Destruir una sesión

## Descripción

```php
public SessionHandlerInterface::destroy(string $id): bool
```php

Destruye una sesión. Llamado por `session_regenerate_id` (con \$destroy = `true`), `session_destroy` y cuando `session_decode` falla.

## Parámetros

`id`  
El ID de sesión a ser destruido.

## Valores devueltos

El valor devuelto (habitualmente `true` en caso de éxito, `false` si ocurre un error). Tenga en cuenta que este valor es devuelto internamente a PHP para análisis.
