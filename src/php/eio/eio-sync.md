---
title: eio_sync
description: Consignar el caché de buffer cache al disco
source_url: https://www.php.net/manual/es/function.eio-sync.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/functions/eio-sync.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_revision: 4e5389401
order: 17210
---

eio_sync

Consignar el caché de buffer cache al disco

## Descripción

```php
eio_sync([int $pri], [callable $callback], [mixed $data]): resource
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`eio_sync` devuelve un recurso de petición en caso de éxito, o `false` si ocurre un error.
