---
title: parallel\Runtime::close
description: Se une graciosamente a la ejecución
source_url: https://www.php.net/manual/es/parallel-runtime.close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parallel/parallel/runtime/close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parallel
translation_status: ready
translation_reviewed: false
translation_revision: 57c7669a1
order: 60170
---

parallel\Runtime::close

Se une graciosamente a la ejecución

## Descripción

```php
public parallel\Runtime::close(): void
```php

Solicita que la ejecución se detenga.

> [!NOTE]
> Las tareas programadas para la ejecución se ejecutarán antes de que se produzca la detención.

## Excepciones

> [!WARNING]
> Lanza una `parallel\Runtime\Error\Closed` si `Runtime` ya estaba cerrado.
