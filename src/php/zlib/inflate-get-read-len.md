---
title: inflate_get_read_len
description: Devuelve el número de bytes leídos hasta el momento
source_url: https://www.php.net/manual/es/function.inflate-get-read-len.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zlib/functions/inflate-get-read-len.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zlib
translation_status: ready
translation_reviewed: true
translation_revision: e41806c30
order: 108930
---

inflate_get_read_len

Devuelve el número de bytes leídos hasta el momento

## Descripción

```php
inflate_get_read_len(InflateContext $context): int
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`context`  

## Valores devueltos

Devuelve el número de bytes leídos hasta el momento o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `context` ahora espera una instancia de `InflateContext`; anteriormente se esperaba un `resource`. |
