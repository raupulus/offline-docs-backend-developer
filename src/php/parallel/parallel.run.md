---
title: parallel\run
description: Ejecución
source_url: https://www.php.net/manual/es/parallel.run.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parallel/functions/parallel.run.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parallel
translation_status: ready
translation_reviewed: false
translation_revision: 57c7669a1
order: 59960
---

parallel\run

Ejecución

## Descripción

```php
parallel\run(Closure $task): Future
```php

Programa `task` para ejecución en paralelo.

```php
parallel\run(Closure $task, array $argv): Future
```

Programa `task` para ejecución en paralelo, pasando `argv` a la ejecución.

## Planificación automática

Si un `\parallel\Runtime` creado y almacenado en caché por una llamada previa a `parallel\run` está inactivo, se utilizará para ejecutar la tarea. Si ningún `\parallel\Runtime` está inactivo, parallel creará y almacenará en caché un `\parallel\Runtime`.

> [!NOTE]
> Los objetos `\parallel\Runtime` creados por el desarrollador no se utilizan para la planificación automática.

## Véase también
