---
title: parallel\Sync::__construct
description: Construcción
source_url: https://www.php.net/manual/es/parallel-sync.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parallel/parallel/sync/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parallel
translation_status: ready
translation_reviewed: false
translation_revision: 57c7669a1
order: 60210
---

parallel\Sync::\_\_construct

Construcción

## Descripción

```php
public parallel\Sync::__construct()
```php

Construye un nuevo objeto de sincronización sin valor.

```php
public parallel\Sync::__construct(scalar $value)
```

Construye un nuevo objeto de sincronización que contiene el valor escalar dado.

## Excepciones

> [!WARNING]
> Lanza una `parallel\Sync\Error\IllegalValue` si `value` no es escalar.
