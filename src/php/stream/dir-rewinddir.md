---
title: streamWrapper::dir_rewinddir
description: Rebobina el gestor de directorio
source_url: https://www.php.net/manual/es/streamwrapper.dir-rewinddir.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/streamwrapper/dir-rewinddir.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_revision: af4410a7e
order: 88360
---

streamWrapper::dir_rewinddir

Rebobina el gestor de directorio

## Descripción

```php
public streamWrapper::dir_rewinddir(): bool
```php

Este método es llamado en respuesta a `rewinddir`.

Debería reiniciar la salida generada por streamWrapper::dir_readdir. Esto es: La siguiente llamada a streamWrapper::dir_readdir debería devolver la primera entrada en la ubicación devueta por streamWrapper::dir_opendir.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`rewinddir`, streamWrapper::dir_readdir
