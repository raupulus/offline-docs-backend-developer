---
title: parallel\Sync::set
description: Acceso
source_url: https://www.php.net/manual/es/parallel-sync.set.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parallel/parallel/sync/set.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parallel
translation_status: ready
translation_reviewed: false
translation_revision: 57c7669a1
order: 60250
---

parallel\Sync::set

Acceso

## Descripción

```php
public parallel\Sync::set(scalar $value)
```php

Establece atómicamente el valor del objeto de sincronización

## Excepciones

> [!WARNING]
> Lanza una `parallel\Sync\Error\IllegalValue` si `value` no es escalar.
