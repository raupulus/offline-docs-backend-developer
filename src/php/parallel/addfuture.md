---
title: parallel\Events::addFuture
description: Objetivo
source_url: https://www.php.net/manual/es/parallel-events.addfuture.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parallel/parallel/events/addfuture.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parallel
translation_status: ready
translation_reviewed: false
translation_revision: 57c7669a1
order: 60040
---

parallel\Events::addFuture

Objetivo

## Descripción

```php
public parallel\Events::addFuture(string $name, parallel\Future $future): void
```php

Observa los eventos en el `future` dado.

## Excepciones

> [!WARNING]
> Lanza una `parallel\Events\Error\Existence` si el objetivo con el nombre dado ya ha sido añadido.
