---
title: parallel\Events::setTimeout
description: Comportamiento
source_url: https://www.php.net/manual/es/parallel-events.settimeout.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parallel/parallel/events/settimeout.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parallel
translation_status: ready
translation_reviewed: false
translation_revision: 57c7669a1
order: 60090
---

parallel\Events::setTimeout

Comportamiento

## Descripción

Por omisión, cuando los eventos son interrogados, se produce un bloqueo (a nivel de PHP) hasta que el primer evento pueda ser devuelto: Definir el tiempo de espera provoca el lanzamiento de una excepción cuando el tiempo de espera es alcanzado.

Esto difiere de definir el modo de bloqueo a `false` con parallel\Events::setBlocking, que no provocará el lanzamiento de una excepción.

```php
public parallel\Events::setTimeout(int $timeout): void
```php

Define el tiempo de espera en microsegundos.

## Excepciones

> [!WARNING]
> Lanza una `parallel\Events\Error` si el bucle es no bloqueante.
