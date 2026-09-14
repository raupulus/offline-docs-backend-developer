---
title: parallel\Events\Input::remove
description: Entradas
source_url: https://www.php.net/manual/es/parallel-events-input.remove.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parallel/parallel/input/remove.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parallel
translation_status: ready
translation_reviewed: false
translation_revision: 57c7669a1
order: 60160
---

parallel\Events\Input::remove

Entradas

## Descripción

```php
public parallel\Events\Input::remove(string $target): void
```php

Elimina la entrada para el objetivo dado.

## Excepciones

> [!WARNING]
> Lanza una `parallel\Events\Input\Error\Existence` si la entrada para el objetivo no existe.
