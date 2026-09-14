---
title: parallel\Channel::send
description: Compartir
source_url: https://www.php.net/manual/es/parallel-channel.send.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parallel/parallel/channel/send.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parallel
translation_status: ready
translation_reviewed: false
translation_revision: 57c7669a1
order: 60020
---

parallel\Channel::send

Compartir

## Descripción

```php
public parallel\Channel::send(mixed $value): void
```php

Envía el valor dado sobre este canal.

## Excepciones

> [!WARNING]
> Lanza una `parallel\Channel\Error\Closed` si el canal está cerrado.

> [!WARNING]
> Lanza una `parallel\Channel\Error\IllegalValue` si el valor es ilegal.
