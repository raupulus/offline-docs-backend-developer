---
title: parallel\Future::value
description: Resolución
source_url: https://www.php.net/manual/es/parallel-future.value.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parallel/parallel/future/value.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parallel
translation_status: ready
translation_reviewed: false
translation_revision: 57c7669a1
order: 60130
---

parallel\Future::value

Resolución

## Descripción

```php
public parallel\Future::value(): mixed
```php

Devuelve (y espera si es necesario) el retorno de la tarea.

## Excepciones

> [!WARNING]
> Lanza una `parallel\Future\Error` si la espera ha fallado (error interno).

> [!WARNING]
> Lanza una `parallel\Future\Error\Killed` si la tarea ejecutada por `parallel\Runtime` ha sido interrumpida.

> [!WARNING]
> Lanza una `parallel\Future\Error\Cancelled` si la tarea ha sido cancelada.

> [!WARNING]
> Lanza una `parallel\Future\Error\Foreign` si la tarea ha levantado una excepción no reconocida.

> [!WARNING]
> Vuelve a lanzar una `Throwable` no capturada en la tarea.
