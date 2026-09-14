---
title: parallel\Runtime::kill
description: Se une a la ejecución
source_url: https://www.php.net/manual/es/parallel-runtime.kill.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parallel/parallel/runtime/kill.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parallel
translation_status: ready
translation_reviewed: false
translation_revision: 57c7669a1
order: 60190
---

parallel\Runtime::kill

Se une a la ejecución

## Descripción

```php
public parallel\Runtime::kill(): void
```php

Intenta forzar la detención de la ejecución.

> [!NOTE]
> Las tareas programadas para la ejecución no se ejecutarán, la tarea en curso será interrumpida.

> [!WARNING]
> Las llamadas de funciones internas en curso no pueden ser interrumpidas.

## Excepciones

> [!WARNING]
> Lanza una `parallel\Runtime\Error\Closed` si `Runtime` ya estaba cerrado.
