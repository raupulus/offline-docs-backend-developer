---
title: Yac::info
description: Estado del caché
source_url: https://www.php.net/manual/es/yac.info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yac/yac/info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yac
translation_status: ready
translation_reviewed: false
translation_revision: d286e6182
order: 104360
---

Yac::info

Estado del caché

## Descripción

```php
public Yac::info(): array
```php

Obtener el estado del sistema de caché

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array, consistente con: "memory_size", "slots_memory_size", "values_memory_size", "segment_size", "segment_num", "miss", "hits", "fails", "kicks", "recycles", "slots_size", "slots_used"
