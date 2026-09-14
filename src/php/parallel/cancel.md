---
title: parallel\Future::cancel
description: Cancelación
source_url: https://www.php.net/manual/es/parallel-future.cancel.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parallel/parallel/future/cancel.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parallel
translation_status: ready
translation_reviewed: false
translation_revision: 57c7669a1
order: 60100
---

parallel\Future::cancel

Cancelación

## Descripción

```php
public parallel\Future::cancel(): bool
```php

Intenta cancelar la tarea.

> [!NOTE]
> Si la tarea está en ejecución, será interrumpida.

> [!WARNING]
> Las llamadas de funciones internas en curso no pueden ser interrumpidas.

## Excepciones

> [!WARNING]
> Lanza una `parallel\Future\Error\Killed` si la tarea ejecutada por `parallel\Runtime` ha sido interrumpida.

> [!WARNING]
> Lanza una `parallel\Future\Error\Cancelled` si la tarea ya ha sido cancelada.
