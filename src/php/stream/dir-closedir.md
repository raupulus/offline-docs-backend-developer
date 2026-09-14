---
title: streamWrapper::dir_closedir
description: Cerrar un gestor de directorio
source_url: https://www.php.net/manual/es/streamwrapper.dir-closedir.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/streamwrapper/dir-closedir.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_revision: af4410a7e
order: 88330
---

streamWrapper::dir_closedir

Cerrar un gestor de directorio

## Descripción

```php
public streamWrapper::dir_closedir(): bool
```php

Este método es llamado en respuesta a `closedir`.

Cualquier recurso que fue bloqueado o asignado durante la apertura y utiliza el flujo de directorio, debería ser liberado.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`closedir`, streamWrapper::dir_opendir
