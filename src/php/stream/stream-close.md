---
title: streamWrapper::stream_close
description: Cerrar un recurso
source_url: https://www.php.net/manual/es/streamwrapper.stream-close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/streamwrapper/stream-close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: false
translation_revision: 7279eb69e
order: 88410
---

streamWrapper::stream_close

Cerrar un recurso

## Descripción

```php
public streamWrapper::stream_close(): void
```php

Este método es llamado en respuesta a `fclose`.

Todos los recursos que estaban bloqueados o asignados por la envoltura deberían ser liberados.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Véase también

`fclose`, streamWrapper::dir_closedir
