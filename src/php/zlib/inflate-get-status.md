---
title: inflate_get_status
description: Devuelve el estado de descompresión
source_url: https://www.php.net/manual/es/function.inflate-get-status.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zlib/functions/inflate-get-status.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zlib
translation_status: ready
translation_reviewed: true
translation_revision: 56680aaa7
order: 108940
---

inflate_get_status

Devuelve el estado de descompresión

## Descripción

```php
inflate_get_status(InflateContext $context): int
```php

Generalmente devuelve `ZLIB_OK` o `ZLIB_STREAM_END`.

## Parámetros

`context`  

## Valores devueltos

Devuelve el estado de descompresión.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `context` ahora espera una instancia de `InflateContext`; anteriormente se esperaba un `resource`. |
