---
title: streamWrapper::dir_opendir
description: Abrir un gestor de directorio
source_url: https://www.php.net/manual/es/streamwrapper.dir-opendir.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/streamwrapper/dir-opendir.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_revision: dec1f8445
order: 88340
---

streamWrapper::dir_opendir

Abrir un gestor de directorio

## Descripción

```php
public streamWrapper::dir_opendir(string $path, int $options): bool
```php

Este método es llamado en respuesta a `opendir`.

## Parámetros

`path`  
Especifica la URL que fue pasada a `opendir`.

> [!NOTE]
> La URL se puede desmontar con `parse_url`.

`options`  

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`opendir`, streamWrapper::dir_closedir, `parse_url`
