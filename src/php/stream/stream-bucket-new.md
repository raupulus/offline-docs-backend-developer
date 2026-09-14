---
title: stream_bucket_new
description: Crea un nuevo compartimento para utilizarlo en el flujo actual
source_url: https://www.php.net/manual/es/function.stream-bucket-new.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-bucket-new.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: true
translation_revision: 32caa89e8
order: 87800
---

stream_bucket_new

Crea un nuevo compartimento para utilizarlo en el flujo actual

## Descripción

```php
stream_bucket_new(resource $stream, string $buffer): StreamBucket
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Esta función ahora retorna una instancia de `StreamBucket`; anteriormente, se retornaba una `stdClass`. |
