---
title: parallel\Events::addChannel
description: Objetivo
source_url: https://www.php.net/manual/es/parallel-events.addchannel.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parallel/parallel/events/addchannel.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parallel
translation_status: ready
translation_reviewed: false
translation_revision: 57c7669a1
order: 60030
---

parallel\Events::addChannel

Objetivo

## Descripción

```php
public parallel\Events::addChannel(parallel\Channel $channel): void
```php

Observa los eventos en el `channel` dado.

## Excepciones

> [!WARNING]
> Lanza una `parallel\Events\Error\Existence` si el canal ya ha sido añadido.
